import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Accessibility Contrast Tests', () => {
  test.beforeEach(async ({ page }) => {
    // Start the dev server manually before running tests
    await page.goto('http://localhost:3000/a11y-test');
  });

  test('should not have any automatically detectable WCAG A or AA violations in light mode', async ({ page }) => {
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('should not have any automatically detectable WCAG A or AA violations in dark mode', async ({ page }) => {
    // Toggle to dark mode
    await page.emulateMedia({ colorScheme: 'dark' });

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('should meet color contrast requirements for all text in light mode', async ({ page }) => {
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2aa'])
      .include('body')
      .analyze();

    const contrastViolations = accessibilityScanResults.violations.filter(
      violation => violation.id === 'color-contrast'
    );

    expect(contrastViolations).toEqual([]);
  });

  test('should meet color contrast requirements for all text in dark mode', async ({ page }) => {
    await page.emulateMedia({ colorScheme: 'dark' });

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2aa'])
      .include('body')
      .analyze();

    const contrastViolations = accessibilityScanResults.violations.filter(
      violation => violation.id === 'color-contrast'
    );

    expect(contrastViolations).toEqual([]);
  });

  test('primary buttons should have sufficient contrast', async ({ page }) => {
    const button = page.locator('.button--primary').first();
    await expect(button).toBeVisible();

    const accessibilityScanResults = await new AxeBuilder({ page })
      .include('.button--primary')
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('navigation links should have sufficient contrast', async ({ page }) => {
    const accessibilityScanResults = await new AxeBuilder({ page })
      .include('.navbar')
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('code blocks should have sufficient contrast', async ({ page }) => {
    const accessibilityScanResults = await new AxeBuilder({ page })
      .include('code, pre')
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });
});
