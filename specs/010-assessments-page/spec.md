# Feature Specification: Assessments & Projects Page

**Feature Branch**: `010-assessments-page`
**Created**: 2025-12-05
**Status**: Draft
**Input**: Create a dedicated Assessment & Projects page (docs/assessments.mdx) that documents all 4 course assessments from the Hackathon PDF. The page must include: 1) Overview of assessment philosophy and timeline, 2) Detailed requirements for Assessment 1 (ROS 2 Package Development - Week 5), 3) Detailed requirements for Assessment 2 (Gazebo Simulation Implementation - Week 7), 4) Detailed requirements for Assessment 3 (Isaac-based Perception Pipeline - Week 10), 5) Detailed requirements for Assessment 4 (Capstone: Simulated Humanoid with Conversational AI - Week 13). Each assessment needs clear learning objectives, project requirements, grading rubric with point breakdown, submission guidelines, and evaluation criteria. The page should be positioned in the sidebar after Weekly Schedule and before Module 1. Use the assessment information from doc/Hackathon I.pdf page 4 as the authoritative source.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - View Assessment Overview and Timeline (Priority: P1) 🎯 MVP

As a student, I want to view all course assessments with their timelines and weights in one place, so that I can plan my study schedule and understand the overall evaluation structure for the quarter.

**Why this priority**: This is the foundation that provides students with clarity on what's expected throughout the course. Without this overview, students cannot effectively plan their time or understand the course structure. This is the minimum viable content that must exist before any detailed assessment documentation.

**Independent Test**: The Docusaurus site can be accessed, the "Assessments & Projects" page is visible in the sidebar (positioned after Weekly Schedule, before Module 1), and displays an overview table showing all 4 assessments with their due dates and relative weights.

**Acceptance Scenarios**:

1. **Given** I am a student viewing the course website, **When** I navigate to the sidebar, **Then** I should see an "Assessments & Projects" link positioned between "Weekly Course Schedule" and "Module 1".
2. **Given** I click on the Assessments & Projects link, **When** the page loads, **Then** I should see an overview section explaining the assessment philosophy and a timeline table showing all 4 assessments with their week numbers.
3. **Given** I am planning my quarter, **When** I review the assessment timeline, **Then** I should clearly understand that assessments are evenly distributed (Weeks 5, 7, 10, 13) to allow continuous skill-building rather than end-loaded evaluation.
4. **Given** I am an instructor, **When** I share this page with students, **Then** they should be able to understand the full assessment structure without needing additional documentation.

---

### User Story 2 - Understand ROS 2 Package Development Project Requirements (Priority: P2)

As a student in Week 3-5, I want to see detailed requirements, learning objectives, and grading criteria for Assessment 1 (ROS 2 Package Development), so that I can prepare my project submission and understand exactly what is expected.

**Why this priority**: This is the first assessment students will encounter, making it critical for setting expectations. Students need clear rubrics to guide their work and avoid surprises during evaluation. This must be delivered before students begin Module 1.

**Independent Test**: The Assessment 1 section on the page contains complete project requirements, a point-based grading rubric, submission guidelines, and clear learning objectives that align with Module 1 content.

**Acceptance Scenarios**:

1. **Given** I am starting Week 3 (Module 1), **When** I navigate to the Assessment 1 section, **Then** I should see specific project requirements (e.g., "Create a ROS 2 package with publisher/subscriber nodes") that directly relate to the Module 1 chapters.
2. **Given** I am working on my ROS 2 project, **When** I review the grading rubric, **Then** I should see a clear point breakdown (e.g., Code Quality: 30 pts, Functionality: 40 pts, Documentation: 20 pts, Presentation: 10 pts) that helps me prioritize my work.
3. **Given** I have completed my project, **When** I check the submission guidelines, **Then** I should know the exact format (e.g., GitHub repository link), deadline (end of Week 5), and any required documentation.
4. **Given** I am preparing for the assessment, **When** I review the learning objectives, **Then** I should understand that this assessment evaluates my mastery of ROS 2 fundamentals (nodes, topics, services, URDF, launch files).

---

### User Story 3 - Understand Gazebo Simulation Implementation Requirements (Priority: P2)

As a student in Week 6-7, I want to see detailed requirements and grading criteria for Assessment 2 (Gazebo Simulation Implementation), so that I can successfully complete the Module 2 project demonstrating physics simulation skills.

**Why this priority**: The second assessment builds on Module 2 (Digital Twin) and requires clear technical specifications for simulation environments. Students need to understand the specific simulation features (collisions, gravity, sensors) they must demonstrate.

**Independent Test**: The Assessment 2 section contains complete project requirements for creating a Gazebo simulation environment, including specific physics features, sensor integrations, and grading rubric.

**Acceptance Scenarios**:

1. **Given** I am starting Week 6 (Module 2), **When** I navigate to the Assessment 2 section, **Then** I should see requirements for building a simulated world in Gazebo with specific elements (obstacles, physics simulation, sensor data).
2. **Given** I am building my simulation, **When** I review the technical requirements, **Then** I should understand which sensors I need to simulate (LiDAR, depth cameras, IMUs) and how they should integrate with my robot model.
3. **Given** I want to maximize my grade, **When** I check the grading rubric, **Then** I should see point allocations for simulation quality, physics accuracy, sensor integration, and documentation.
4. **Given** I am preparing my submission, **When** I review the deliverables, **Then** I should know I need to provide simulation files, a demo video or screenshots, and documentation of my simulation setup.

---

### User Story 4 - Understand Isaac-based Perception Pipeline Requirements (Priority: P2)

As a student in Week 8-10, I want to see detailed requirements and grading criteria for Assessment 3 (Isaac-based Perception Pipeline), so that I can successfully implement GPU-accelerated perception using NVIDIA Isaac tools.

**Why this priority**: This assessment represents the most technically advanced project before the capstone, requiring students to work with Isaac Sim/Isaac ROS. Clear requirements help students navigate the complexity of GPU-accelerated perception and synthetic data generation.

**Independent Test**: The Assessment 3 section contains complete project requirements for deploying an Isaac ROS perception pipeline, including VSLAM, object detection, and grading rubric.

**Acceptance Scenarios**:

1. **Given** I am starting Week 8 (Module 3), **When** I navigate to the Assessment 3 section, **Then** I should see requirements for implementing a perception pipeline using Isaac Sim or Isaac ROS with specific components (VSLAM, object detection, or navigation).
2. **Given** I am configuring my pipeline, **When** I review the technical requirements, **Then** I should understand the expected inputs (sensor data), processing steps (GPU-accelerated perception), and outputs (navigation commands or object classifications).
3. **Given** I have hardware constraints, **When** I check the requirements, **Then** I should see guidance on minimum GPU requirements (RTX GPU) and options for cloud-based development if local hardware is insufficient.
4. **Given** I am preparing for evaluation, **When** I review the grading rubric, **Then** I should see criteria for perception accuracy, pipeline performance, integration quality, and documentation.

---

### User Story 5 - Understand Capstone Project Requirements (Priority: P1) 🎯 MVP

As a student approaching Week 11-13, I want to see comprehensive requirements, milestones, and evaluation criteria for the Capstone Project (Autonomous Humanoid with Conversational AI), so that I can plan and execute the final integrative project that demonstrates mastery of all course concepts.

**Why this priority**: The capstone is the culminating assessment that integrates all four modules. Students need this information early (ideally from Week 1) to understand the end goal and plan their learning trajectory. This is MVP alongside the overview because it defines the ultimate learning objective.

**Independent Test**: The Assessment 4 section contains complete capstone requirements describing the end-to-end system (voice command → planning → navigation → object manipulation), implementation milestones for Weeks 11-13, and a comprehensive grading rubric.

**Acceptance Scenarios**:

1. **Given** I am starting the course, **When** I navigate to the Capstone section, **Then** I should see a clear description of the final project: "A simulated humanoid robot that receives a voice command, plans a path, navigates obstacles, identifies an object using computer vision, and manipulates it."
2. **Given** I am in Week 11 (capstone planning), **When** I review the milestones, **Then** I should see a breakdown: Week 11 (Planning & Design), Week 12 (Development & Integration), Week 13 (Testing & Presentation).
3. **Given** I am building my capstone system, **When** I check the technical requirements, **Then** I should understand the required integrations: voice-to-action (Whisper), cognitive planning (LLMs), perception (Isaac/computer vision), navigation (Nav2), and manipulation.
4. **Given** I am preparing for the final presentation, **When** I review the grading rubric, **Then** I should see criteria for system integration (30 pts), functionality (30 pts), innovation/complexity (20 pts), presentation (10 pts), documentation (10 pts).
5. **Given** I want to reference the capstone details, **When** I scroll to Assessment 4, **Then** I should see a cross-reference link to the detailed Capstone chapter in Module 4.

---

### Edge Cases

- How should the page handle students who join mid-quarter and may have missed earlier assessments?
- What guidance should be provided for students who fail an assessment and need to resubmit?
- Should there be late submission policies documented on this page, or is that handled separately?
- How should the page address hardware limitations (e.g., students without RTX GPUs for Isaac Sim)?
- Should there be guidance for students forming teams (if assessments allow group work)?

## Assumptions

- All 4 assessments are individual projects unless explicitly stated otherwise in the course syllabus.
- Assessment weights are equal (25% each) unless otherwise specified by the instructor.
- Submission is via a course management system (LMS) or GitHub, not through the Docusaurus site itself.
- The page is informational/documentation only - no interactive submission forms or grade tracking.
- Students have access to the required hardware (RTX GPU, Jetson kits, etc.) as documented in the Hardware Requirements section of the PDF.
- Grading rubrics provided are templates that instructors may customize based on specific cohort needs.
- Assessment requirements align with the learning outcomes documented in the Weekly Schedule page.
- Late submission policies, academic integrity guidelines, and resubmission rules are handled by institutional policies (not documented on this page unless specified).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A new MDX page MUST be created at `docs/assessments.mdx` with comprehensive documentation of all 4 course assessments.
- **FR-002**: The page MUST include an **Assessment Philosophy & Timeline** section explaining the pedagogical approach (continuous assessment, skill-building, integration of concepts) and a timeline table showing Week, Assessment, Module Coverage, and Due Date.
- **FR-003**: The page MUST document **Assessment 1: ROS 2 Package Development Project** with:
  - Learning objectives (mastery of ROS 2 nodes, topics, services, URDF, launch files)
  - Project requirements (create custom ROS 2 package, implement publisher/subscriber, write launch files, include URDF robot model)
  - Grading rubric with point breakdown (total 100 points suggested: Code Quality 30, Functionality 40, Documentation 20, Presentation 10)
  - Submission guidelines (format, deadline, required files)
- **FR-004**: The page MUST document **Assessment 2: Gazebo Simulation Implementation** with:
  - Learning objectives (physics simulation, sensor integration, world-building)
  - Project requirements (create simulated world in Gazebo, implement physics features like collisions/gravity, simulate sensors like LiDAR/depth cameras/IMUs)
  - Grading rubric with point breakdown (total 100 points suggested: Simulation Quality 30, Physics Accuracy 25, Sensor Integration 25, Documentation 20)
  - Submission guidelines
- **FR-005**: The page MUST document **Assessment 3: Isaac-based Perception Pipeline** with:
  - Learning objectives (GPU-accelerated perception, VSLAM, synthetic data generation, Isaac platform proficiency)
  - Project requirements (deploy Isaac ROS perception pipeline, implement VSLAM or object detection, demonstrate GPU acceleration)
  - Grading rubric with point breakdown (total 100 points suggested: Perception Accuracy 30, Pipeline Performance 25, Integration Quality 25, Documentation 20)
  - Hardware requirements note (RTX GPU required, cloud alternatives acceptable)
  - Submission guidelines
- **FR-006**: The page MUST document **Assessment 4: Capstone Project - The Autonomous Humanoid** with:
  - Learning objectives (end-to-end system integration, multi-modal interaction, VLA pipeline)
  - Project description (simulated humanoid robot: voice command → cognitive planning → navigation → object identification → manipulation)
  - Implementation milestones (Week 11: Planning, Week 12: Development, Week 13: Testing & Presentation)
  - Technical requirements (integrate Whisper for voice, LLMs for planning, Isaac/CV for perception, Nav2 for navigation, manipulation control)
  - Grading rubric with point breakdown (total 100 points suggested: System Integration 30, Functionality 30, Innovation/Complexity 20, Presentation 10, Documentation 10)
  - Cross-reference link to the detailed Capstone chapter in Module 4
- **FR-007**: Each assessment section MUST include:
  - **Learning Objectives**: What skills/knowledge are being evaluated
  - **Project Requirements**: Specific deliverables and technical expectations
  - **Grading Rubric**: Point-based breakdown showing how work will be evaluated
  - **Submission Guidelines**: Format, deadline, required files/documentation
- **FR-008**: The page MUST be added to `sidebars.ts` with `sidebar_position: 3` (after Weekly Schedule which is position 2, before Module 1).
- **FR-009**: The page MUST include proper frontmatter (id, title, sidebar_position, description) and pass Docusaurus validation.
- **FR-010**: Assessment descriptions MUST align with the content of their corresponding modules (Assessment 1 with Module 1, Assessment 2 with Module 2, etc.).
- **FR-011**: The page MUST cross-reference the Weekly Schedule page (link to weekly-schedule.mdx) to show which weeks correspond to which assessments.

### Key Entities

- **Assessment**: Represents one of the 4 course evaluations, with attributes: number (1-4), name (e.g., "ROS 2 Package Development"), module mapping (which module it evaluates), due week (5, 7, 10, or 13), weight (percentage of final grade), learning objectives, requirements, rubric.
- **Grading Rubric**: Point-based evaluation criteria for an assessment, with attributes: criterion name (e.g., "Code Quality"), point allocation (e.g., 30/100), description of expectations.
- **Milestone**: Specific checkpoints within the Capstone project, with attributes: week number, milestone name (Planning/Development/Testing), deliverables.
- **Learning Objective**: Skill or knowledge area being evaluated, mapped to specific module content (e.g., "Master ROS 2 pub/sub communication" maps to Module 1, Chapter 2).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The Docusaurus site builds successfully with the new assessments page included, with no build errors or broken links.
- **SC-002**: The assessments page appears in the sidebar at `sidebar_position: 3` (after "Weekly Course Schedule", before "Module 1: The Robotic Nervous System").
- **SC-003**: All 4 assessments are documented with complete sections (Learning Objectives, Requirements, Grading Rubric, Submission Guidelines) totaling at least 500 words per assessment.
- **SC-004**: Each grading rubric includes a point-based breakdown totaling 100 points with at least 4 evaluation criteria per assessment.
- **SC-005**: The page includes at least 2 cross-reference links: one to the Weekly Schedule page and one to the Module 4 Capstone chapter.
- **SC-006**: User testing (3 students + 1 instructor) confirms that the assessment requirements are clear, rubrics are actionable, and the page structure is easy to navigate.
- **SC-007**: The page passes Docusaurus validation (frontmatter correctness, no markdown syntax errors, all internal links functional).
- **SC-008**: The assessment timeline table clearly shows the distribution of assessments across the 13-week quarter with week numbers and module associations.

## Out of Scope

- Interactive submission forms or file upload functionality (students submit via LMS or GitHub, not through this page).
- Automated grading tools or rubric calculators.
- Grade tracking, progress dashboards, or student-specific assessment history.
- Peer review functionality or collaborative assessment features.
- Detailed solution examples or sample submissions (those may be provided separately by instructors).
- Late submission policies, resubmission rules, or academic integrity statements (assumed to be covered by institutional policies).
- Downloadable assessment templates or starter code repositories (may be added as a future enhancement).

## Dependencies

- The Weekly Schedule page (`docs/weekly-schedule.mdx`) must exist and be accessible for cross-referencing.
- Module 4 Capstone chapter (`docs/module4-vision-language-action/04-capstone-the-autonomous-humanoid.mdx`) must exist for linking from Assessment 4.
- All 4 modules (Modules 1-4) must have complete chapter content to ensure assessment requirements align with learning materials.
- The sidebar configuration (`sidebars.ts`) must support adding a standalone page at position 3.
- The Hackathon PDF (`doc/Hackathon I.pdf` page 4) is the authoritative source for assessment names and descriptions.

## Risks

- **Risk 1**: Grading rubrics may be too generic or not specific enough for different instructor preferences. **Mitigation**: Frame rubrics as "suggested templates" and encourage instructors to customize based on cohort needs. Include a note at the top of the page stating rubrics are customizable.
- **Risk 2**: Students may find the capstone requirements overwhelming if presented all at once in Week 1. **Mitigation**: Break capstone into clear milestones (Weeks 11-13) and emphasize that prior assessments build the necessary skills progressively.
- **Risk 3**: Hardware requirements for Assessment 3 (RTX GPU) may not be available to all students. **Mitigation**: Explicitly document cloud-based alternatives (AWS/Azure GPU instances) and reference the Hardware Requirements section from the PDF.
- **Risk 4**: Assessment requirements may become outdated if module content changes. **Mitigation**: Include version date in frontmatter and establish a review cycle (e.g., quarterly) to ensure alignment with module updates.
- **Risk 5**: Students may miss this page if the sidebar position is not prominent. **Mitigation**: Position at sidebar_position 3 (immediately after Weekly Schedule, before modules begin) and cross-reference from the Weekly Schedule page.

## Notes

- This page directly addresses a significant gap identified in the Hackathon readiness report ("Assessments Section: Missing").
- The 4 assessments from the PDF (page 4) are: ROS 2 package development, Gazebo simulation implementation, Isaac-based perception pipeline, Capstone (simulated humanoid with conversational AI).
- Assessment timing aligns with the Weekly Schedule: Week 5 (end of Module 1), Week 7 (end of Module 2), Week 10 (end of Module 3), Week 13 (end of capstone).
- The page should be referenced from the introduction page and weekly schedule page for maximum visibility.
- Consider adding a "Frequently Asked Questions" section if common student questions emerge after initial deployment.
