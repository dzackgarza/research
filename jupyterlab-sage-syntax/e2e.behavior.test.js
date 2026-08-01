import { test, expect } from '@playwright/test';

const fixtureUrl = 'http://localhost:8888/lab/tree/test_docstring_preview.py';
const sourceFixtureUrl =
  'http://localhost:8888/lab/tree/src/dzack_research/preamble/categories/modules/framed/framed_free_modules.sage';

async function openFixture(
  page,
  url = fixtureUrl,
  previewSelector = '.cm-docstring-math-block mjx-container'
) {
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await page.locator('#jp-main-dock-panel').waitFor({ state: 'attached', timeout: 30000 });
  await page.waitForFunction(
    selector =>
      [...document.querySelectorAll('.cm-editor')].some(editor => {
        const rect = editor.getBoundingClientRect();
        const style = getComputedStyle(editor);
        return (
          rect.width > 0 &&
          rect.height > 0 &&
          style.display !== 'none' &&
          editor.querySelector(selector) !== null
        );
      }),
    previewSelector,
    { timeout: 30000 }
  );
}

async function activeEditor(page) {
  const editorIndex = await page.locator('.cm-editor').evaluateAll(editors => {
    const visible = editors
      .map((editor, index) => ({ editor, index }))
      .filter(({ editor }) => {
        const rect = editor.getBoundingClientRect();
        const style = getComputedStyle(editor);
        return (
          rect.width > 0 &&
          rect.height > 0 &&
          style.display !== 'none' &&
          style.visibility !== 'hidden'
        );
      });

    if (visible.length !== 1) {
      throw new Error(`expected one visible CodeMirror editor, found ${visible.length}`);
    }
    return visible[0].index;
  });

  return page.locator('.cm-editor').nth(editorIndex);
}

test.describe('JupyterLab Sage docstring preview behavior', () => {
  test('replaces the complete multiline display formula in the active editor', async ({ page }) => {
    await openFixture(page);
    const editor = await activeEditor(page);

    const displayMath = editor.locator('.cm-docstring-math-block');
    await expect(displayMath).toHaveCount(1);
    await expect(displayMath.locator('mjx-container[jax="CHTML"] mjx-math')).toHaveCount(1);

    const displayBox = await displayMath.boundingBox();
    expect(displayBox?.width).toBeGreaterThan(0);
    expect(displayBox?.height).toBeGreaterThan(0);

    const sourceFragments = editor.locator('.cm-docstring-math-hidden');
    await expect(sourceFragments).toHaveCount(2);
    const sourceStates = await sourceFragments.evaluateAll(elements =>
      elements.map(element => {
        const style = getComputedStyle(element);
        const rect = element.getBoundingClientRect();
        return { display: style.display, width: rect.width, height: rect.height };
      })
    );

    for (const state of sourceStates) {
      expect(state.display).toBe('none');
      expect(state.width).toBe(0);
      expect(state.height).toBe(0);
    }
  });

  test('typesets inline math in the active editor instead of leaving source delimiters', async ({ page }) => {
    await openFixture(page);
    const editor = await activeEditor(page);

    const inlineMath = editor.locator('.cm-docstring-math-inline');
    await expect(inlineMath).toHaveCount(1);
    await expect(inlineMath.locator('mjx-container[jax="CHTML"] mjx-math mjx-mi')).toHaveCount(1);

    const inlineBox = await inlineMath.boundingBox();
    expect(inlineBox?.width).toBeGreaterThan(0);
    expect(inlineBox?.height).toBeGreaterThan(0);
  });

  test('renders reST inline literals with the code treatment in the active editor', async ({ page }) => {
    await openFixture(page);
    const editor = await activeEditor(page);

    const inlineCode = editor.locator('.cm-docstring-inline-code');
    await expect(inlineCode).toHaveCount(2);
    const codeStyles = await inlineCode.evaluateAll(elements =>
      elements.map(element => {
        const style = getComputedStyle(element);
        const rect = element.getBoundingClientRect();
        return {
          width: rect.width,
          height: rect.height,
          paddingLeft: parseFloat(style.paddingLeft),
          paddingRight: parseFloat(style.paddingRight),
          borderTopWidth: parseFloat(style.borderTopWidth)
        };
      })
    );

    for (const style of codeStyles) {
      expect(style.width).toBeGreaterThan(0);
      expect(style.height).toBeGreaterThan(0);
      expect(style.paddingLeft).toBeGreaterThan(0);
      expect(style.paddingRight).toBeGreaterThan(0);
      expect(style.borderTopWidth).toBeGreaterThan(0);
    }
  });

  test('applies Python token highlighting inside reST inline literals', async ({ page }) => {
    await openFixture(page);
    const editor = await activeEditor(page);

    const inlineCode = editor.locator('.cm-docstring-inline-code', {
      hasText: 'FreeModuleOnSet'
    });
    await expect(inlineCode).toHaveCount(1);

    const tokens = inlineCode.locator('[class*="tok-"]');
    await expect(tokens).toHaveCount(6);
    const tokenData = await tokens.evaluateAll(elements =>
      elements.map(element => ({
        text: element.textContent,
        className: element.className,
        color: getComputedStyle(element).color
      }))
    );

    expect(tokenData.map(token => token.text)).toEqual([
      'FreeModuleOnSet',
      '(',
      'R',
      ',',
      'S',
      ')'
    ]);
    expect(tokenData[0].className).toContain('tok-variableName');
    expect(tokenData[0].className).toContain('tok-function');
    expect(tokenData[1].className).toContain('tok-punctuation');
    expect(tokenData[0].color).not.toBe(tokenData[2].color);
    const themeColors = await inlineCode.evaluate(element => {
      const probe = document.createElement('span');
      element.append(probe);
      const resolve = name => {
        probe.style.color = `var(${name})`;
        return getComputedStyle(probe).color;
      };
      const colors = {
        function: resolve('--jp-mirror-editor-def-color'),
        variable: resolve('--jp-mirror-editor-variable-color')
      };
      probe.remove();
      return colors;
    });
    expect(tokenData[0].color).toBe(themeColors.function);
    expect(tokenData[2].color).toBe(themeColors.variable);
  });

  test('does not add horizontal padding around inline math', async ({ page }) => {
    await openFixture(page, sourceFixtureUrl, '.cm-docstring-math-inline mjx-container');
    const editor = await activeEditor(page);
    const line = editor.locator('.cm-line').filter({ hasText: 'The set' });
    const inlineMath = line.locator('.cm-docstring-math-inline');

    await expect(inlineMath).toHaveCount(1);
    const spacing = await inlineMath.evaluate(element => {
      const style = getComputedStyle(element);
      return {
        paddingLeft: parseFloat(style.paddingLeft),
        paddingRight: parseFloat(style.paddingRight),
        marginLeft: parseFloat(style.marginLeft),
        marginRight: parseFloat(style.marginRight)
      };
    });

    expect(spacing).toEqual({
      paddingLeft: 0,
      paddingRight: 0,
      marginLeft: 0,
      marginRight: 0
    });
  });
});
