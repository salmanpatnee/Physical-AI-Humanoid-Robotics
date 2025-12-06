# Tasks: Project-Wide Theme & Color Palette

**Input**: Design documents from `specs/013-project-color-theme/`
**Prerequisites**: plan.md, spec.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the necessary files and add dependencies.

- [ ] T001 [P] Add a contrast-checking dev dependency (e.g., `a11y-contrast-checker`) to `package.json`.
- [ ] T002 [P] Create the main theme file at `src/css/custom.css`.
- [ ] T003 [P] Create the module-to-color mapping file at `src/theme/ModuleColorMap.json`.
- [ ] T004 [P] Create the directory `src/theme/ModuleBadge/` for the new component.
- [ ] T005 Update `docusaurus.config.ts` to register the `src/css/custom.css` stylesheet in the `themeConfig`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Define the core color palette that all other themeing depends on.

- [ ] T006 Define the light-mode color palette as CSS variables under the `:root` selector in `src/css/custom.css`.
- [ ] T007 Define the dark-mode color palette by overriding the root variables under the `[data-theme="dark"]` selector in `src/css/custom.css`.

**Checkpoint**: Foundation ready. Light and dark palettes are defined.

---

## Phase 3: User Story 1 - Consistent and Accessible Visual Theme (Priority: P1) 🎯 MVP

**Goal**: Apply the new color variables to all common UI elements for a consistent look and feel, ensuring accessibility.

**Independent Test**: The site can be visually inspected in both light and dark modes. All common elements (text, backgrounds, links, code blocks) use the new theme. An automated contrast check passes.

### Implementation for User Story 1

- [ ] T008 [US1] Apply theme color variables to global Docusaurus elements (e.g., `--ifm-color-primary`, `--ifm-background-color`) in `src/css/custom.css`.
- [ ] T009 [US1] [P] Style the navbar to use the new theme colors in `src/css/custom.css`.
- [ ] T010 [US1] [P] Style the footer to use the new theme colors in `src/css/custom.css`.
- [ ] T011 [US1] [P] Style primary buttons and links to use the new theme colors in `src/css/custom.css`.
- [ ] T012 [US1] Update the Prism code block theme in `docusaurus.config.ts` to a theme compatible with the new palette (e.g., `theme: 'dracula'`).
- [ ] T013 [US1] Create a temporary test page at `src/pages/a11y-test.mdx` that includes all standard Docusaurus components and text styles to serve as a visual checklist.
- [ ] T014 [US1] Add a new script to `package.json` named `test:contrast` that runs the chosen contrast checker against the `a11y-test.mdx` page.

**Checkpoint**: At this point, User Story 1 should be fully functional. The site should have a consistent and accessible theme.

---

## Phase 4: User Story 2 - Clear Module Identification (Priority: P2)

**Goal**: Implement a component that visually distinguishes content belonging to different course modules.

**Independent Test**: The `<ModuleBadge>` component can be used in an MDX file and renders with the correct background color based on the `module` prop.

### Implementation for User Story 2

- [ ] T015 [US2] Populate `src/theme/ModuleColorMap.json` with mappings from module IDs to CSS color variables (e.g., `"module-1": "var(--primary)"`).
- [ ] T016 [US2] Implement the `<ModuleBadge>` component in `src/theme/ModuleBadge/index.js`. It should read the `module` prop, look up the color in `ModuleColorMap.json`, and apply it as an inline style or class.
- [ ] T017 [US2] [P] Add basic styling for the component in `src/theme/ModuleBadge/styles.module.css` (e.g., padding, border-radius).
- [ ] T018 [US2] Add examples of the `<ModuleBadge>` for each module to the test page at `src/pages/a11y-test.mdx` to verify its functionality.

**Checkpoint**: User Stories 1 AND 2 should now both work.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and cleanup.

- [ ] T019 Run the `test:contrast` script and fix any identified accessibility violations.
- [ ] T020 Start the development server (`npm run start`) and perform a full visual review of the site in both light and dark modes.
- [ ] T021 [P] Validate that the `quickstart.md` documentation for `<ModuleBadge>` is accurate.
- [ ] T022 Remove the temporary test page at `src/pages/a11y-test.mdx`.
- [ ] T023 Ensure the production build completes without errors by running `npx docusaurus build`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)** & **Foundational (Phase 2)** must be completed first.
- **User Story 1 (Phase 3)** depends on Phase 1 & 2.
- **User Story 2 (Phase 4)** depends on Phase 1 & 2.
- **Polish (Phase 5)** depends on all user stories being complete.

### User Story Dependencies

- **User Story 1 & 2** are largely independent and could be worked on in parallel after Phase 2 is complete, although US2 benefits from the test page created in US1.

### Parallel Opportunities

- Most tasks in Phase 1 can run in parallel.
- After Phase 2, work on US1 (theming common elements) and US2 (implementing the badge component) can happen concurrently.
- Within US1, styling different elements (navbar, footer, etc.) can be done in parallel as they modify the same file but likely different sections.
