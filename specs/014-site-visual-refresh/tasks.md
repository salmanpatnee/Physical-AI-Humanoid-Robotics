# Tasks: Site Visual Refresh

**Input**: Design documents from `specs/014-site-visual-refresh/`

## Phase 1: User Story 1 - Branding and Visual Identity (Priority: P1) 🎯 MVP

**Goal**: Update the site's main branding elements.

**Independent Test**: The homepage can be loaded and visually inspected to confirm the new logo and hero background are displayed.

### Implementation for User Story 1

- [x] T001 [US1] [P] Update the `logo.src` property in `docusaurus.config.ts` to `img/logo.png`.
- [x] T002 [US1] Identify the Hero section component (likely `src/pages/index.js` or a similar file) and update its styling to use `static/img/humanoid.jpeg` as the background image.

**Checkpoint**: At this point, User Story 1 should be fully functional.

---

## Phase 2: User Story 2 - Improved Navigation and Discoverability (Priority: P1)

**Goal**: Make it easier for users to find documentation and explore course content.

**Independent Test**: The "Get Started" button navigates correctly, and the footer contains a complete list of module links.

### Implementation for User Story 2

- [x] T003 [US2] Update the "Get Started" button in the Hero section component to link to the `/docs` page.
- [x] T004 [US2] Modify the Footer component (find the relevant file, likely in `src/theme/Footer/`) to dynamically generate a list of all course modules and link to them.

**Checkpoint**: At this point, User Story 2 should be fully functional.

---

## Phase 3: User Story 3 - Enhanced Footer and Sidebar Aesthetics (Priority: P2)

**Goal**: Improve the visual polish of the site's footer and sidebar.

**Independent Test**: The copyright bar has a distinct background, and sidebar links have the new, polished styling.

### Implementation for User Story 3

- [x] T005 [US3] [P] Apply a distinct blue background color to the copyright bar in the footer. This may involve adding a class in the Footer component and styling it in `src/css/custom.css`.
- [x] T006 [US3] Add CSS rules to `src/css/custom.css` to style the sidebar navigation links with a subtle border, a subtle border-radius, and a grayish text color.

**Checkpoint**: At this point, User Story 3 should be fully functional.

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and cleanup.

- [x] T007 Visually inspect all changed elements to ensure they render correctly in both light and dark modes.
- [x] T008 [P] Verify that the `quickstart.md` documentation is accurate.
- [x] T009 Run `npx docusaurus build` to ensure the production build completes without errors.

---

## Dependencies & Execution Order

- **User Stories 1, 2, and 3** are largely independent and can be worked on in parallel.
- **Polish (Phase 4)** depends on all user stories being complete.