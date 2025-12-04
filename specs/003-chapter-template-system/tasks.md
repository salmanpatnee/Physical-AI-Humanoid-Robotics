# Tasks: Reusable Chapter Template System

**Input**: Design documents from `specs/003-chapter-template-system/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the directory structure for the new components and plugins.

- [ ] T001 [P] Create directory `src/plugins/chapter-validation/` for the validation plugin.
- [ ] T002 [P] Create directory `src/components/LearningGoals/` for the LearningGoals component.
- [ ] T003 [P] Create directory `src/components/Prerequisites/` for the Prerequisites component.
- [ ] T004 [P] Create directory `src/components/KeyTakeaways/` for the KeyTakeaways component.
- [ ] T005 [P] Create directory `src/components/ExerciseBlock/` for the ExerciseBlock component.
- [ ] T006 [P] Create directory `tests/unit/plugins/` for plugin unit tests.
- [ ] T007 [P] Create directory `tests/unit/components/` for component unit tests.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement the build-time metadata validation to ensure all chapters adhere to the defined schema.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [ ] T008 Install AJV dependency: `npm install ajv`.
- [ ] T009 Create the basic structure for the Docusaurus plugin in `src/plugins/chapter-validation/index.js`.
- [ ] T010 Implement the plugin's `contentLoaded` lifecycle hook to read document frontmatter in `src/plugins/chapter-validation/index.js`.
- [ ] T011 [P] Load the schema from `specs/003-chapter-template-system/contracts/ChapterMetadata.schema.json` into the plugin.
- [ ] T012 Implement the validation logic using AJV against the frontmatter for each document in `src/plugins/chapter-validation/index.js`.
- [ ] T013 Ensure the Docusaurus build fails with a clear error message if a chapter's frontmatter is invalid.
- [ ] T014 [P] Write a unit test in `tests/unit/plugins/chapter-validation.test.js` to verify the validation logic with valid and invalid metadata.
- [ ] T015 Register the new plugin in `docusaurus.config.ts`.

**Checkpoint**: Foundation ready. The build process now validates all chapter frontmatter.

---

## Phase 3: User Story 1 - Author a New Chapter (Priority: P1) 🎯 MVP

**Goal**: Enable authors to use basic structural components to write a consistently formatted chapter.

**Independent Test**: An author can create a `.mdx` chapter using `<LearningGoals>`, `<Prerequisites>`, and `<KeyTakeaways>` components, and see it rendered correctly.

### Implementation for User Story 1

- [ ] T016 [P] [US1] Create the React component for `<LearningGoals>` in `src/components/LearningGoals/index.tsx`.
- [ ] T017 [P] [US1] Add basic styling for the LearningGoals component in `src/components/LearningGoals/styles.module.css`.
- [ ] T018 [P] [US1] Create the React component for `<Prerequisites>` in `src/components/Prerequisites/index.tsx`.
- [ ] T019 [P] [US1] Add basic styling for the Prerequisites component in `src/components/Prerequisites/styles.module.css`.
- [ ] T020 [P] [US1] Create the React component for `<KeyTakeaways>` in `src/components/KeyTakeaways/index.tsx`.
- [ ] T021 [P] [US1] Add basic styling for the KeyTakeaways component in `src/components/KeyTakeaways/styles.module.css`.
- [ ] T022 Register the new components in `src/theme/MDXComponents.ts` to make them globally available in MDX files.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Utilize Specialized Content Blocks (Priority: P2)

**Goal**: Provide authors with an interactive `<ExerciseBlock>` component.

**Independent Test**: An author can add an `<ExerciseBlock>` to a chapter with hints and a solution, and a user can click to reveal hints one by one.

### Tests for User Story 2

- [ ] T023 [P] [US2] Write unit tests for the `<ExerciseBlock>` in `tests/unit/components/ExerciseBlock.test.tsx` to verify hint-reveal logic.

### Implementation for User Story 2

- [ ] T024 [US2] Create the `<ExerciseBlock>` React component in `src/components/ExerciseBlock/index.tsx`.
- [ ] T025 [US2] Implement the component state to manage revealed hints using the `<details>` and `<summary>` HTML elements for accessibility.
- [ ] T026 [US2] Add styling for the ExerciseBlock component in `src/components/ExerciseBlock/styles.module.css`.
- [ ] T027 [US2] Update `src/theme/MDXComponents.ts` to include the `ExerciseBlock` component.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Finalize the feature with a complete example and end-to-end testing.

- [ ] T028 Create a full example chapter `docs/99-chapter-template-example/index.mdx` that uses all new components (`LearningGoals`, `Prerequisites`, `KeyTakeaways`, `ExerciseBlock`).
- [ ] T029 Write a Playwright E2E test to navigate to the example chapter and verify the `<ExerciseBlock>`'s interactive hint-reveal functionality.
- [ ] T030 Review and refine styles for all new components to ensure they are visually consistent and polished.
- [ ] T031 Validate the feature by following the steps in `specs/003-chapter-template-system/quickstart.md`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup (T001). BLOCKS all user stories.
- **User Stories (Phase 3 & 4)**: Depend on Foundational (Phase 2) completion.
- **Polish (Phase 5)**: Depends on all user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Phase 2.
- **User Story 2 (P2)**: Can start after Phase 2. It is independent of US1.

### Parallel Opportunities

- All Setup tasks (T001-T007) can run in parallel.
- Once Foundational (Phase 2) is complete, US1 and US2 can be implemented in parallel.
- Within US1, the three components (T016-T021) can be developed in parallel.
