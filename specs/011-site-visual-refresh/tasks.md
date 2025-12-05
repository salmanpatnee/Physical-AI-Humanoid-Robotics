---
description: "Task list for feature implementation: Site Visual Refresh"
---

# Tasks: Site Visual Refresh

**Input**: Design documents from `specs/011-site-visual-refresh/`
**Prerequisites**: plan.md, spec.md, research.md

**Tests**: No new tests were requested for this feature. Existing tests should be run for regression checking.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Phase 1: Setup

**Purpose**: Ensure the development environment is ready.

- [ ] T001 Verify that the Docusaurus development server can be started with `npm run start`.

---

## Phase 2: User Story 1 - Branding and Navigation Refresh (Priority: P1) 🎯 MVP

**Goal**: Update the site's main branding, navigation, and color scheme to create a more professional and consistent user experience.

**Independent Test**: Start the development server and visually confirm that the site title, header links, footer links, and primary color scheme match the specification.

### Implementation for User Story 1

- [ ] T002 [P] [US1] In `docusaurus.config.ts`, update the `title` property to "Physical AI & Humanoid Robotics".
- [ ] T003 [P] [US1] In `docusaurus.config.ts`, remove the "Blog" and "GitHub" link objects from the `themeConfig.navbar.items` array.
- [ ] T004 [P] [US1] In `docusaurus.config.ts`, find the main documentation link in `themeConfig.navbar.items` and ensure its `to` property is set to `/docs`.
- [ ] T005 [P] [US1] In `docusaurus.config.ts`, replace the existing links in `themeConfig.footer.links` with a new "Modules" section containing links to the four course modules as defined in the spec.
- [ ] T006 [P] [US1] In `src/css/custom.css`, update the `--ifm-color-primary` and its related shades (`-light`, `-dark`, etc.) with the gray color palette defined in `research.md`.

**Checkpoint**: At this point, User Story 1 should be fully functional and visually verifiable.

---

## Phase 3: User Story 2 - Improve Learning Goals Readability (Priority: P2)

**Goal**: Enhance the readability of the "Learning Goals" component.

**Independent Test**: Navigate to a page that includes the `LearningGoals` component and visually confirm that its styling has been improved according to the research document (e.g., better spacing, padding).

### Implementation for User Story 2

- [ ] T007 [US2] Identify the stylesheet for the `LearningGoals` component. Based on the project structure, this is likely `src/components/LearningGoals/index.tsx` (if using inline styles or CSS-in-JS) or a linked `.css` / `.module.css` file in the same directory.
- [ ] T008 [US2] In the stylesheet identified in T007, apply the CSS changes outlined in `research.md` (e.g., increase `padding`, set `line-height` to 1.7, etc.).

**Checkpoint**: At this point, User Stories 1 and 2 should both be complete and visually correct.

---

## Phase 4: Polish & Validation

**Purpose**: Final verification and cleanup.

- [ ] T009 Run `npm run start` and perform a full visual inspection of the site to ensure all changes from US1 and US2 are correctly implemented and look cohesive.
- [ ] T010 Run existing end-to-end tests to check for any regressions in site functionality.

---

## Dependencies & Execution Order

### Phase Dependencies
- **Setup (Phase 1)**: Must be completed first.
- **User Stories (Phase 2 & 3)**: Depend on Setup completion.
- **Polish (Phase 4)**: Depends on all User Stories being complete.

### User Story Dependencies
- **User Story 1 (P1)**: Can start after Setup. No dependencies on other stories.
- **User Story 2 (P2)**: Can start after Setup. No dependencies on other stories.

### Parallel Opportunities
- Once Setup is complete, US1 and US2 can be worked on in parallel by different developers.
- Within US1, tasks T002, T003, T004, T005, and T006 can theoretically be worked on in parallel as they modify different parts of their respective files, though a single developer would likely perform them sequentially.

---

## Implementation Strategy

### MVP First (User Story 1 Only)
1. Complete Phase 1: Setup.
2. Complete all tasks in Phase 2 for User Story 1.
3. **STOP and VALIDATE**: Visually inspect the site to confirm all branding, navigation, and theme changes are correct. This completes the MVP.

### Incremental Delivery
1. Complete and validate the MVP (US1).
2. Complete all tasks in Phase 3 for User Story 2.
3. **STOP and VALIDATE**: Visually inspect the `LearningGoals` component.
4. Complete Phase 4: Polish & Validation.
