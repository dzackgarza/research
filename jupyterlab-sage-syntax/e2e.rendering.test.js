import { test, expect } from '@playwright/test';

const fixtureUrl = 'http://localhost:8888/lab/tree/test_docstring_preview.py';

async function openFixture(page) {
  await page.goto(fixtureUrl, { waitUntil: 'domcontentloaded' });
  await page.locator('#jp-main-dock-panel').waitFor({ state: 'attached', timeout: 30000 });
  await page.waitForFunction(
    () =>
      [...document.querySelectorAll('.cm-editor')].some(editor => {
        const rect = editor.getBoundingClientRect();
        const style = getComputedStyle(editor);
        return (
          rect.width > 0 &&
          rect.height > 0 &&
          style.display !== 'none' &&
          style.visibility !== 'hidden' &&
          editor.querySelector('.cm-docstring-math-block mjx-container') !== null
        );
      }),
    undefined,
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

test('multiline math source is hidden after the display widget is inserted', async ({ page }) => {
  await openFixture(page);
  const editor = await activeEditor(page);

  await expect(editor.locator('.cm-docstring-math-block')).toHaveCount(1);
  await expect(
    editor.locator('.cm-docstring-math-block mjx-container[jax="CHTML"] mjx-math')
  ).toHaveCount(1);

  const hiddenSource = editor.locator('.cm-docstring-math-hidden');
  const states = await hiddenSource.evaluateAll(elements =>
    elements.map(element => {
      const style = getComputedStyle(element);
      const rect = element.getBoundingClientRect();
      return {
        display: style.display,
        visibility: style.visibility,
        width: rect.width,
        height: rect.height
      };
    })
  );

  expect(states).toHaveLength(2);
  expect(states, 'raw multiline math source must not be rendered').toEqual(
    states.map(state => ({ ...state, display: 'none', width: 0, height: 0 }))
  );
});
