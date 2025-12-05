# Tasks: Weekly Course Schedule Page

**Input**: Design documents from `specs/009-weekly-breakdown/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md

**Tests**: No automated tests were requested in the specification. Human validation is defined by the "Independent Test" criteria in `spec.md`.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel.
- **[Story]**: Which user story this task belongs to (e.g., US1, US2).
- Include exact file paths in descriptions.

## Phase 1: Setup

**Purpose**: Create the initial file for the new schedule page.

- [ ] T001 Create the new file `docs/weekly-schedule.mdx`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Add the basic page structure required by all user stories.

- [ ] T002 Add the Docusaurus frontmatter (id, title, description) to `docs/weekly-schedule.mdx`.
- [ ] T003 Add the main page H1 title and a brief introductory paragraph to `docs/weekly-schedule.mdx`.

---

## Phase 3: User Story 1 - Weekly Schedule Navigation (Priority: P1) 🎯 MVP

**Goal**: Display a 13-week course schedule mapping each week to modules, topics, and activities, allowing users to plan their learning journey.

**Independent Test**: The Docusaurus site can be launched, and the "Course Schedule" page can be accessed, showing all 13 weeks with their content clearly organized and with clickable links.

### Implementation for User Story 1

> **Content Source Note**: All content for the following tasks (**T004-T009**) must be transcribed directly from the "Weekly Breakdown" section on page 3 of `doc/Hackathon I.pdf`.

- [ ] T004 [US1] Create the parent Markdown table or structure for the 13-week breakdown in `docs/weekly-schedule.mdx`.
- [ ] T005 [P] [US1] Populate the content for **Weeks 1-2** (Introduction) into the schedule structure in `docs/weekly-schedule.mdx`.
- [ ] T006 [P] [US1] Populate the content for **Weeks 3-5** (Module 1) into the schedule, ensuring chapter links are clickable and prerequisite notes are included, in `docs/weekly-schedule.mdx`.
- [ ] T007 [P] [US1] Populate the content for **Weeks 6-7** (Module 2) into the schedule in `docs/weekly-schedule.mdx`.
- [ ] T008 [P] [US1] Populate the content for **Weeks 8-10** (Module 3) into the schedule in `docs/weekly-schedule.mdx`.
- [ ] T009 [P] [US1] Populate the content for **Weeks 11-13** (Module 4 & Capstone) into the schedule, including details on progressive capstone development, in `docs/weekly-schedule.mdx`.

**Checkpoint**: User Story 1 is functional. The page displays the full 13-week text-based schedule.

---

## Phase 4: User Story 2 - Timeline Visualization (Priority: P2)

**Goal**: Display a visual timeline or table showing how the 4 modules map to the 13-week structure for quick comprehension.

**Independent Test**: The Course Schedule page includes a visual component (e.g., a Mermaid diagram) clearly showing the relationship between weeks and modules.

### Implementation for User Story 2

- [ ] T010 [US2] Add a new section titled "Course Timeline" at the top of `docs/weekly-schedule.mdx`.
- [ ] T011 [US2] Implement a Mermaid.js Gantt chart or a Markdown table under the "Course Timeline" section to visualize the module-to-week mapping as defined in `FR-005`. This should be added to `docs/weekly-schedule.mdx`.

**Checkpoint**: User Stories 1 and 2 are functional. The page displays the full schedule and the visual timeline.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final integration, validation, and documentation.

- [ ] T012 Modify `sidebars.ts` to add a link to the new schedule page, positioned after the "Introduction" and before "Module 1".
- [ ] T013 Manually validate that the Docusaurus site builds successfully and all links on the `docs/weekly-schedule.mdx` page are functional.
- [ ] T014 Run validation steps from `specs/009-weekly-breakdown/quickstart.md` to ensure the page is accessible and appears as expected.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)** & **Foundational (Phase 2)** must be completed first.
- **User Story 1 (Phase 3)** depends on Phase 2 completion.
- **User Story 2 (Phase 4)** depends on Phase 3 completion, as it adds to the same file.
- **Polish (Phase 5)** depends on all user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Is the base and has no dependencies on other stories.
- **User Story 2 (P2)**: Has a hard dependency on User Story 1, as it modifies the page created in US1. They cannot be worked on in parallel.

### Parallel Opportunities

- Within User Story 1, the population of different week groups (**T005-T009**) can be done in parallel as they are independent content additions to the same file (though merge care is needed).

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational
3.  Complete Phase 3: User Story 1
4.  Complete Phase 5: Polish (specifically tasks T012 and T013 to make the page visible and validate it)
5.  **STOP and VALIDATE**: The site now has a functional, text-based schedule page. This is the minimum viable product.

### Incremental Delivery

1.  Deliver the MVP as described above.
2.  Later, complete Phase 4 (User Story 2) to add the visual timeline enhancement.
