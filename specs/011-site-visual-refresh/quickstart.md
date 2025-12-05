# Quickstart Guide: Site Visual Refresh

This guide outlines the development steps required to implement the site visual refresh.

### 1. Update Docusaurus Configuration

**File**: `docusaurus.config.ts`

-   **Site Title**: Locate the `title` property and change its value to `"Physical AI & Humanoid Robotics"`.
-   **Navbar Links**:
    -   Find the `navbar.items` array.
    -   Remove the array entries for the "Blog" and "GitHub" links.
    -   Find the item for the "Docs" link (usually `label: 'Tutorial'` or `label: 'Docs'`) and ensure its `to` property is set to `/docs`.
-   **Footer Links**:
    -   Locate the `footer.links` array.
    -   Remove the existing link objects.
    -   Add a new link object with the title "Modules" and an `items` array containing links to the four modules as specified in the `spec.md` assumptions.

### 2. Update Color Theme

**File**: `src/css/custom.css`

-   Find the `:root` selector.
-   Change the value of the `--ifm-color-primary` CSS variable to `#607d8b`.
-   Update the related `--ifm-color-primary-` variables (`-light`, `-lighter`, `-dark`, `-darker`) with the corresponding values from `research.md`.

### 3. Improve LearningGoals Component Readability

**File**: Find the stylesheet associated with the `LearningGoals` component (e.g., `src/components/LearningGoals/styles.module.css` or similar).

-   Apply the CSS changes outlined in `research.md`:
    -   Increase `padding`.
    -   Increase `line-height`.
    -   Ensure `font-size` is adequate.
    -   Add `margin-bottom` to list items.

### 4. Run and Verify

-   Start the Docusaurus development server (`npm run start`).
-   Visually inspect all changes in the browser to confirm they match the specification.
-   Run any existing tests to ensure no regressions have been introduced.
