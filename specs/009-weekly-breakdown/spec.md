# Feature Specification: Weekly Course Schedule Page

**Feature Branch**: `009-weekly-schedule-page`
**Created**: 2025-12-05
**Status**: Draft
**Input**: Hackathon PDF requirement: "Weekly Breakdown - Weeks 1-13 with specific topics and timeline mapping to the 4 modules"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Weekly Schedule Navigation (Priority: P1)

As a student or instructor, I want to view a 13-week course schedule that maps each week to specific module topics and learning activities, so that I can plan my learning journey and track progress throughout the quarter.

**Why this priority**: The Hackathon PDF explicitly requires a weekly breakdown (Weeks 1-13) that is currently missing from the book. This is critical for academic course planning and aligns with the "Quarter Overview" structure in the PDF.

**Independent Test**: The Docusaurus site can be launched, and a "Course Schedule" page can be accessed showing all 13 weeks organized chronologically with clear mapping to the 4 modules.

**Acceptance Scenarios**:

1. **Given** the Docusaurus site is running, **When** I navigate to the Course Schedule page, **Then** I should see a 13-week breakdown with weeks grouped by module.
2. **Given** I am viewing Week 3-5 (ROS 2 Fundamentals), **When** I read the content, **Then** I should see specific topics like "Nodes, topics, services, and actions" mapped to Module 1 chapters.
3. **Given** I am an instructor planning a semester, **When** I review the schedule, **Then** each week should indicate which module chapters to cover and what hands-on activities are expected.
4. **Given** I am at Week 8 (NVIDIA Isaac), **When** I view that week's content, **Then** I should see clear connections to Module 3 chapters with learning objectives.

---

### User Story 2 - Timeline Visualization (Priority: P2)

As a reader, I want to see a visual timeline or table showing how the 4 modules map to the 13-week structure, so that I can quickly understand the course pacing and module distribution.

**Why this priority**: Visual representation improves comprehension of course structure and helps students/instructors plan resources and time allocation.

**Independent Test**: The Course Schedule page includes a visual component (table, timeline, or Mermaid diagram) showing the relationship between weeks and modules.

**Acceptance Scenarios**:

1. **Given** I am viewing the Course Schedule, **When** I see the timeline section, **Then** it should clearly show that Module 1 covers Weeks 3-5, Module 2 covers Weeks 6-7, etc.
2. **Given** I am planning my study schedule, **When** I review the visual timeline, **Then** I should be able to quickly identify which weeks are assessment/project weeks.
3. **Given** I need to understand module weight, **When** I view the timeline, **Then** I should see that Module 3 (Isaac) spans the longest period (Weeks 8-10).

### Edge Cases

- What if a student wants to accelerate and complete multiple weeks in one week? Should the schedule indicate dependencies?
- How will the schedule handle holidays or breaks in an academic setting?
- Should there be links from weekly topics back to specific chapter pages?
- What if the 13-week schedule doesn't align perfectly with the 4 modules (17 chapters total)?

## Assumptions

- The 13-week breakdown from the Hackathon PDF is the authoritative source for the schedule structure.
- Each week maps to specific learning activities (readings, labs, projects) but the book focuses on conceptual content, not detailed assignment instructions.
- The schedule page will be a standalone MDX page accessible from the main navigation or introduction.
- Module 4 includes the Capstone project as a multi-week effort (implied in PDF).
- The weekly schedule should reference existing chapter content without duplicating it.

## Clarifications

### Session 2025-12-05

- Q: Should the weekly schedule page include direct links to specific chapters, or just reference them by name? → A: Include clickable links to chapters for easy navigation.
- Q: Should each week include estimated hours/workload, or just topic descriptions? → A: Include estimated hours per week (from PDF: "10 hours/week × 12 weeks" suggests ~10 hours/week standard).
- Q: Should the schedule distinguish between lecture content vs. hands-on lab time? → A: Yes, indicate "Topics" (reading) vs. "Activities" (hands-on) for each week.
- Q: Where should this page appear in the sidebar - before modules, after introduction, or as a separate section? → A: Place after Introduction, before Module 1, as "Course Structure" or "Weekly Schedule".

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A new MDX page MUST be created at `docs/weekly-schedule.md` or `docs/course-structure.md` with comprehensive 13-week breakdown.
- **FR-002**: The page MUST map each of the 13 weeks to specific module chapters and topics from the Hackathon PDF.
- **FR-003**: The schedule MUST include:
  - **Weeks 1-2**: Introduction to Physical AI (foundational concepts)
  - **Weeks 3-5**: ROS 2 Fundamentals (Module 1)
  - **Weeks 6-7**: Robot Simulation with Gazebo (Module 2)
  - **Weeks 8-10**: NVIDIA Isaac Platform (Module 3)
  - **Weeks 11-12**: Humanoid Robot Development (Module 3 advanced + Module 4 intro)
  - **Week 13**: Conversational Robotics & Capstone (Module 4)
- **FR-004**: Each week entry MUST include:
  - Week number and title
  - Primary module(s) covered
  - Specific topics/chapters to read
  - Hands-on activities or labs
  - Estimated time commitment
- **FR-005**: The page MUST include a visual timeline (table or Mermaid diagram) showing module-to-week mapping.
- **FR-006**: Chapter references MUST be clickable links to the actual chapter pages.
- **FR-007**: The page MUST be added to the sidebar configuration in `sidebars.ts` with appropriate position (after Introduction, before Module 1).

### Key Entities *(include if feature involves data)*

- **Week**: Represents one week of the 13-week course, with week number, title, module mapping, topics, activities, and time estimate.
- **Module Mapping**: Relationship between weeks and modules (e.g., Weeks 3-5 → Module 1).
- **Topic**: Specific learning subject within a week (e.g., "ROS 2 Nodes and Topics").
- **Activity**: Hands-on exercise or lab associated with a week (e.g., "Build ROS 2 package with Python").

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The Docusaurus site builds successfully with the new weekly schedule page included.
- **SC-002**: The weekly schedule page appears in the sidebar at the correct position (after Introduction, before Module 1).
- **SC-003**: All 13 weeks from the Hackathon PDF are represented with complete information (title, topics, activities, time estimate).
- **SC-004**: A visual timeline (table or diagram) is present showing the module-to-week relationship.
- **SC-005**: At least 80% of chapter references are correctly linked to their respective chapter pages.
- **SC-006**: User testing (5 readers) confirms that the schedule is clear, accurate, and useful for course planning.
- **SC-007**: The page includes proper frontmatter (id, title, sidebar_position, description) and passes Docusaurus validation.

## Out of Scope

- Creating detailed assignment instructions or grading rubrics for each week (this is covered separately in assessments).
- Implementing an interactive calendar or scheduling tool (this is a static content page).
- Adding progress tracking or completion checkboxes for students (future enhancement).
- Translating the schedule to other languages or time zones.
- Creating printable PDF versions of the schedule (can be added later).

## Open Questions

- **OQ-001**: Should the schedule include prerequisite checks (e.g., "Before Week 8, ensure you have completed Module 1-2")? → Suggested: Yes, add prerequisites for major transitions.
- **OQ-002**: Should there be a "catch-up week" or buffer week built into the 13-week schedule? → Suggested: No, keep aligned with PDF's 13-week structure.
- **OQ-003**: Should the Capstone project span multiple weeks explicitly, or is it just part of Week 13? → Suggested: Weeks 11-13 should indicate progressive Capstone development.

## Dependencies

- Existing module chapters must be in place (Modules 1-4 with all chapters).
- Sidebar configuration must support adding standalone pages.
- Hackathon PDF content must be accurately transcribed into the weekly breakdown.

## Risks

- **Risk 1**: The 13-week schedule might not perfectly align with the 17 total chapters (4+4+4+5 = 17 chapters vs. 13 weeks). Mitigation: Some weeks will cover multiple chapters, others will focus on projects/integration.
- **Risk 2**: Students might find the rigid weekly structure inflexible for self-paced learning. Mitigation: Clearly label the schedule as "recommended" and note that self-paced learners can adjust.
- **Risk 3**: Links to chapters might break if chapter URLs change. Mitigation: Use relative paths and test links during build validation.

## Technical Approach (Optional)

- Create a single MDX page with Markdown tables for the weekly breakdown.
- Use a Mermaid gantt chart or timeline for visual representation.
- Use custom MDX components (like `<WeekBlock>`) if needed for consistent formatting.
- Reference chapters using standard Docusaurus link syntax: `[Chapter Title](../module1/chapter-file.mdx)`.

## Notes

- This feature directly addresses a gap identified in the Hackathon readiness report.
- The weekly schedule from the PDF is authoritative and should be transcribed verbatim, then enhanced with links and formatting.
- This page will serve as a "roadmap" for the entire course and should be prominently featured.
