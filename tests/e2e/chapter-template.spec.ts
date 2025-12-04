import { test, expect } from '@playwright/test';

test.describe('Chapter Template Example', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/docs/99-chapter-template-example/');
  });

  test('should display the chapter title', async ({ page }) => {
    await expect(page.locator('h1')).toContainText('Chapter Template Example');
  });

  test('should display LearningGoals component', async ({ page }) => {
    await expect(page.locator('text=Learning Goals')).toBeVisible();
  });

  test('should display Prerequisites component', async ({ page }) => {
    await expect(page.locator('text=Prerequisites')).toBeVisible();
  });

  test('should display KeyTakeaways component', async ({ page }) => {
    await expect(page.locator('text=Key Takeaways')).toBeVisible();
  });

  test('should display ExerciseBlock with question', async ({ page }) => {
    await expect(
      page.locator('text=What is the primary advantage of using a reusable chapter template system?')
    ).toBeVisible();
  });

  test('should reveal hints progressively in ExerciseBlock', async ({ page }) => {
    // Check that hints are initially collapsed
    const hint1Details = page.locator('details:has-text("Hint 1")');
    const hint2Details = page.locator('details:has-text("Hint 2")');
    const hint3Details = page.locator('details:has-text("Hint 3")');

    // Check hints are present
    await expect(hint1Details).toBeVisible();
    await expect(hint2Details).toBeVisible();
    await expect(hint3Details).toBeVisible();

    // Initially, hint content should not be visible (collapsed)
    await expect(
      page.locator('text=Think about what happens when multiple authors contribute to a book.')
    ).toBeHidden();

    // Click on Hint 1 to reveal it
    await hint1Details.locator('summary').click();
    await expect(
      page.locator('text=Think about what happens when multiple authors contribute to a book.')
    ).toBeVisible();

    // Click on Hint 2 to reveal it
    await hint2Details.locator('summary').click();
    await expect(
      page.locator('text=Consider the benefits of standardization across different chapters.')
    ).toBeVisible();

    // Click on Hint 3 to reveal it
    await hint3Details.locator('summary').click();
    await expect(
      page.locator('text=It helps maintain a uniform structure and style throughout the entire book.')
    ).toBeVisible();
  });

  test('should reveal solution when clicked in ExerciseBlock', async ({ page }) => {
    const solutionDetails = page.locator('details:has-text("Solution")');

    // Check solution summary is present
    await expect(solutionDetails).toBeVisible();

    // Initially, solution content should not be visible (collapsed)
    await expect(page.locator('text=The primary advantage is')).toBeHidden();

    // Click on Solution to reveal it
    await solutionDetails.locator('summary').click();
    await expect(page.locator('text=The primary advantage is')).toBeVisible();
    await expect(page.locator('text=consistency')).toBeVisible();
  });

  test('should have accessible details/summary elements', async ({ page }) => {
    // Check that all interactive elements are details elements for accessibility
    const detailsElements = page.locator('details');
    const count = await detailsElements.count();

    // Should have 3 hints + 1 solution = 4 details elements
    expect(count).toBeGreaterThanOrEqual(4);

    // Check that details elements have summary children
    for (let i = 0; i < count; i++) {
      const detail = detailsElements.nth(i);
      const summary = detail.locator('summary');
      await expect(summary).toBeVisible();
    }
  });
});
