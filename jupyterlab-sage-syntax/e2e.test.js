import { test, expect } from '@playwright/test';

test.describe('JupyterLab Docstring Live Preview Regression Test Suite', () => {
  test.setTimeout(60000);

  test.beforeEach(async ({ page }) => {
    page.on('console', msg => {
      console.log(`[BROWSER CONSOLE (${msg.type()})]:`, msg.text());
    });

    // Navigate to live JupyterLab test file
    await page.goto('http://localhost:8888/lab/tree/test_docstring_preview.py', { waitUntil: 'domcontentloaded' });
    await page.waitForSelector('#jp-main-dock-panel', { state: 'attached', timeout: 30000 });
    await page.locator('.cm-editor').first().waitFor({ state: 'attached', timeout: 30000 });
    await page.waitForTimeout(4000);
  });

  test('REGRESSION TEST 1: renders double-backtick ``code inline`` as <code class="cm-docstring-inline-code">', async ({ page }) => {
    const inlineCodeCount = await page.locator('.cm-docstring-inline-code').count();
    expect(
      inlineCodeCount, 
      `REGRESSION FAILURE: Expected at least 2 rendered double-backtick <code> widgets in live editor, but found ${inlineCodeCount}`
    ).toBeGreaterThanOrEqual(2);
  });

  test('REGRESSION TEST 2: renders multiline display math \\[ ... \\] across blank lines as <div class="cm-docstring-math-block">', async ({ page }) => {
    const blockMathCount = await page.locator('.cm-docstring-math-block').count();
    expect(
      blockMathCount, 
      `REGRESSION FAILURE: Expected at least 1 rendered multiline \\[ ... \\] block math widget in live editor, but found ${blockMathCount}`
    ).toBeGreaterThanOrEqual(1);
  });

  test('REGRESSION TEST 3: renders parenthesized inline math \\(S\\) as <span class="cm-docstring-math-inline">', async ({ page }) => {
    const inlineMathCount = await page.locator('.cm-docstring-math-inline').count();
    expect(
      inlineMathCount, 
      `REGRESSION FAILURE: Expected at least 1 rendered \\( ... \\) inline math widget in live editor, but found ${inlineMathCount}`
    ).toBeGreaterThanOrEqual(1);
  });

  test('REGRESSION TEST 4: verifies total rendered docstring widget count >= 4 in live editor', async ({ page }) => {
    const totalWidgets = await page.locator('.cm-docstring-inline-code, .cm-docstring-math-inline, .cm-docstring-math-block').count();
    expect(
      totalWidgets,
      `REGRESSION FAILURE: Expected total docstring preview widgets >= 4 in test_docstring_preview.py, but found ${totalWidgets}`
    ).toBeGreaterThanOrEqual(4);
  });
});
