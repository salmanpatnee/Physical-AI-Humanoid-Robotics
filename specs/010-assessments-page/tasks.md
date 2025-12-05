# Tasks: Assessments & Projects Page

**Input**: Design documents from `specs/010-assessments-page/`
**Prerequisites**: `plan.md`, `spec.md`, `data-model.md`, `quickstart.md`

**Tests**: No automated tests were explicitly requested. Manual validation is covered in `quickstart.md`.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup

**Purpose**: Create the initial file for the new assessments page.

- [ ] T001 Create the new file `docs/assessments.mdx`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Add the basic page structure required for content.

- [ ] T002 Add Docusaurus frontmatter (id, title, sidebar_position, description) to `docs/assessments.mdx`.
- [ ] T003 Add main H1 title and introductory assessment philosophy section to `docs/assessments.mdx`.

---

## Phase 3: User Story 1 - View Assessment Overview and Timeline (P1) 🎯 MVP

**Goal**: Display an overview of all 4 assessments with their timelines and weights.

**Independent Test**: The Docusaurus site is accessible, the "Assessments & Projects" page is visible in the sidebar (positioned after Weekly Schedule, before Module 1), and displays an overview table showing all 4 assessments with their week numbers.

### Implementation for User Story 1

- [ ] T004 [US1] Create the Assessment Timeline table showing Week, Assessment, Module Coverage, and Due Date in `docs/assessments.mdx`.

---

## Phase 4: User Story 2 - Understand ROS 2 Package Development Project Requirements (P2)

**Goal**: Document detailed requirements for Assessment 1 (ROS 2 Package Development).

**Independent Test**: The Assessment 1 section on the page contains complete project requirements, a point-based grading rubric, submission guidelines, and clear learning objectives that align with Module 1 content.

### Implementation for User Story 2

- [ ] T005 [US2] Add Assessment 1 section ("ROS 2 Package Development Project") with its H2 title to `docs/assessments.mdx`.
- [ ] T006 [P] [US2] Add Learning Objectives for Assessment 1 to `docs/assessments.mdx`.
- [ ] T007 [P] [US2] Add Project Requirements for Assessment 1 to `docs/assessments.mdx`.
- [ ] T008 [P] [US2] Add Grading Rubric for Assessment 1 (100 points, 4+ criteria) to `docs/assessments.mdx`.
- [ ] T009 [P] [US2] Add Submission Guidelines for Assessment 1 to `docs/assessments.mdx`.

---

## Phase 5: User Story 3 - Understand Gazebo Simulation Implementation Requirements (P2)

**Goal**: Document detailed requirements for Assessment 2 (Gazebo Simulation Implementation).

**Independent Test**: The Assessment 2 section contains complete project requirements for creating a Gazebo simulation environment, including specific physics features, sensor integrations, and grading rubric.

### Implementation for User Story 3

- [ ] T010 [US3] Add Assessment 2 section ("Gazebo Simulation Implementation") with its H2 title to `docs/assessments.mdx`.
- [ ] T011 [P] [US3] Add Learning Objectives for Assessment 2 to `docs/assessments.mdx`.
- [ ] T012 [P] [US3] Add Project Requirements for Assessment 2 to `docs/assessments.mdx`.
- [ ] T013 [P] [US3] Add Grading Rubric for Assessment 2 (100 points, 4+ criteria) to `docs/assessments.mdx`.
- [ ] T014 [P] [US3] Add Submission Guidelines for Assessment 2 to `docs/assessments.mdx`.

---

## Phase 6: User Story 4 - Understand Isaac-based Perception Pipeline Requirements (P2)

**Goal**: Document detailed requirements for Assessment 3 (Isaac-based Perception Pipeline).

**Independent Test**: The Assessment 3 section contains complete project requirements for deploying an Isaac ROS perception pipeline, including VSLAM, object detection, and grading rubric.

### Implementation for User Story 4

- [ ] T015 [US4] Add Assessment 3 section ("Isaac-based Perception Pipeline") with its H2 title to `docs/assessments.mdx`.
- [ ] T016 [P] [US4] Add Learning Objectives for Assessment 3 to `docs/assessments.mdx`.
- [ ] T017 [P] [US4] Add Project Requirements for Assessment 3 to `docs/assessments.mdx`.
- [ ] T018 [P] [US4] Add Grading Rubric for Assessment 3 (100 points, 4+ criteria) to `docs/assessments.mdx`.
- [ ] T019 [P] [US4] Add Hardware Requirements Note for Assessment 3 to `docs/assessments.mdx`.
- [ ] T020 [P] [US4] Add Submission Guidelines for Assessment 3 to `docs/assessments.mdx`.

---

## Phase 7: User Story 5 - Understand Capstone Project Requirements (P1) 🎯 MVP

**Goal**: Document comprehensive requirements for the Capstone Project (Assessment 4).

**Independent Test**: The Assessment 4 section contains complete capstone requirements describing the end-to-end system (voice command → planning → navigation → object manipulation), implementation milestones for Weeks 11-13, and a comprehensive grading rubric.

### Implementation for User Story 5

- [ ] T021 [US5] Add Assessment 4 section ("Capstone Project - The Autonomous Humanoid") with its H2 title to `docs/assessments.mdx`.
- [ ] T022 [P] [US5] Add Learning Objectives for Assessment 4 to `docs/assessments.mdx`.
- [ ] T023 [P] [US5] Add Project Description for Assessment 4 to `docs/assessments.mdx`.
- [ ] T024 [P] [US5] Add Implementation Milestones for Assessment 4 (Weeks 11-13) to `docs/assessments.mdx`.
- [ ] T025 [P] [US5] Add Technical Requirements for Assessment 4 to `docs/assessments.mdx`.
- [ ] T026 [P] [US5] Add Grading Rubric for Assessment 4 (100 points, 4+ criteria) to `docs/assessments.mdx`.
- [ ] T027 [P] [US5] Add Submission Guidelines for Assessment 4 to `docs/assessments.mdx`.
- [ ] T028 [P] [US5] Add Cross-reference link to Module 4 Capstone chapter within Assessment 4 section in `docs/assessments.mdx`.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final integration, validation, and documentation.

- [ ] T029 Modify `sidebars.ts` to add a link to "assessments" with `sidebar_position: 3`.
- [ ] T030 Add a cross-reference link to the Weekly Schedule page in `docs/assessments.mdx`.
- [ ] T031 Manually validate Docusaurus site builds successfully and all internal links are functional.
- [ ] T032 Run validation steps from `specs/010-assessments-page/quickstart.md` to ensure page is accessible and appears as expected.

---

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: No dependencies - can start immediately.
-   **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories.
-   **User Story 1 (Phase 3)**: Depends on Foundational phase completion.
-   **User Story 5 (Phase 7)**: This is another P1 story and can theoretically run in parallel with US1 after Foundational phase, or sequentially. Given its complexity, it's placed after other P2 stories in this sequential flow.
-   **User Stories 2, 3, 4 (Phases 4, 5, 6)**: All depend on Foundational phase completion. They are P2 stories and can be done in any order relative to each other, but after P1 stories for a sequential flow.
-   **Polish (Phase 8)**: Depends on all user stories being complete.

### User Story Dependencies

-   **User Story 1 (P1)**: Can start after Foundational (Phase 2). No dependencies on other stories.
-   **User Story 2 (P2)**: Can start after Foundational (Phase 2). No dependencies on other stories.
-   **User Story 3 (P2)**: Can start after Foundational (Phase 2). No dependencies on other stories.
-   **User Story 4 (P2)**: Can start after Foundational (Phase 2). No dependencies on other stories.
-   **User Story 5 (P1)**: Can start after Foundational (Phase 2). Integrates concepts from all modules, so ideally done when those are understood, but implementation of *this page* is independent.

### Parallel Opportunities

-   All tasks marked `[P]` within an Implementation section for a User Story can run in parallel. For example, within User Story 2 (T006-T009) can be done in parallel as they concern different sub-sections of the same MDX file content.
-   Once Foundational phase completes, User Story 1 and User Story 5 (both P1) could be worked on in parallel by different team members.
-   After P1 stories, P2 stories (US2, US3, US4) can be worked on in parallel.

---

## Parallel Example: User Story 2 Implementation

```bash
# All these tasks involve adding different sections to the same docs/assessments.mdx file,
# so they can be worked on concurrently, but require careful merging.

- [P] T006 [US2] Add Learning Objectives for Assessment 1 to docs/assessments.mdx.
- [P] T007 [US2] Add Project Requirements for Assessment 1 to docs/assessments.mdx.
- [P] T008 [US2] Add Grading Rubric for Assessment 1 (100 points, 4+ criteria) to docs/assessments.mdx.
- [P] T009 [US2] Add Submission Guidelines for Assessment 1 to docs/assessments.mdx.
```

---

## Implementation Strategy

### MVP First (User Story 1 and User Story 5)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational
3.  Complete Phase 3: User Story 1 (Overview and Timeline)
4.  Complete Phase 7: User Story 5 (Capstone Project - Comprehensive requirements) - This is a P1 and crucial.
5.  Complete relevant tasks from Phase 8: Polish (T029 for sidebar, T030 for cross-reference, T031-T032 for validation of P1 stories).
6.  **STOP and VALIDATE**: Test the MVP (Overview + Capstone) independently.
7.  Deploy/demo if ready.

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready.
2.  Add User Story 1 → Test independently → Deploy/Demo (MVP 1: Overview).
3.  Add User Story 5 → Test independently → Deploy/Demo (MVP 2: Overview + Capstone).
4.  Add User Story 2 → Test independently → Deploy/Demo.
5.  Add User Story 3 → Test independently → Deploy/Demo.
6.  Add User Story 4 → Test independently → Deploy/Demo.
7.  Complete remaining Polish tasks.
8.  Each story adds value without breaking previous stories.
