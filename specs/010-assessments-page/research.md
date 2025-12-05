# Research: Assessments & Projects Page

**Feature**: 010-assessments-page
**Date**: 2025-12-05
**Phase**: 0 - Outline & Research

## Research Questions Resolved

### 1. MDX Page Structure for Assessment Documentation

**Decision**: Use flat Markdown structure with H2 sections for each assessment, embedded Markdown tables for rubrics

**Rationale**:
- Docusaurus natively supports Markdown tables with excellent mobile responsiveness
- H2 headings automatically generate table of contents navigation
- No custom React components needed - reduces complexity and maintenance
- Tables are screen-reader accessible (better than custom UI)
- Standard GitHub Flavored Markdown is familiar to contributors

**Alternatives Considered**:
- Custom React component for assessment cards → Rejected: Overkill for static content, adds complexity
- Separate MDX file per assessment → Rejected: Spec requires single page for easy reference
- YAML/JSON data with component rendering → Rejected: Not needed for static, infrequently-changing content

**References**:
- Docusaurus Markdown Features: https://docusaurus.io/docs/markdown-features
- Markdown Tables: https://www.markdownguide.org/extended-syntax/#tables

---

### 2. Grading Rubric Table Format

**Decision**: Use 3-column Markdown tables: Criterion | Points | Description

**Rationale**:
- Clear, scannable format for students to understand evaluation criteria
- Point breakdown visible at-a-glance
- Description column provides detailed expectations
- Total row at bottom shows 100-point sum
- Markdown table syntax is simple and maintainable

**Example Format**:
```markdown
| Criterion | Points | Description |
|-----------|--------|-------------|
| Code Quality & Structure | 30 | Clean, well-organized code... |
| Functionality & Requirements | 40 | All required features... |
| Documentation | 20 | Clear README, comments... |
| Presentation/Demo | 10 | Effective demonstration... |
| **Total** | **100** | |
```

**Alternatives Considered**:
- 4-column with "Excellent/Good/Poor" criteria → Rejected: Too detailed, overwhelming for initial view
- Separate table per criterion with scoring levels → Rejected: Too verbose, spec requires concise rubrics
- Percentage-based rubric → Rejected: Points are clearer and add up to 100

---

### 3. Assessment Timeline Table Design

**Decision**: Use 4-column table: Week | Assessment | Module Coverage | Due Date

**Rationale**:
- Aligns with Weekly Schedule page structure (consistent UX)
- Week column allows quick lookup ("What's due in Week 7?")
- Module Coverage shows relationship to course modules
- Due Date provides clear deadline visibility
- Sortable/scannable format for planning

**Example Format**:
```markdown
| Week | Assessment | Module Coverage | Due Date |
|------|------------|-----------------|----------|
| 5 | ROS 2 Package Development | Module 1 Complete | End of Week 5 |
| 7 | Gazebo Simulation | Module 2 Complete | End of Week 7 |
| 10 | Isaac Perception Pipeline | Module 3 Complete | End of Week 10 |
| 13 | Capstone Project | All Modules Integrated | End of Week 13 |
```

**Alternatives Considered**:
- Gantt chart visual (Mermaid) → Rejected: Overkill for 4 assessments, spec emphasizes table format
- Separate section per assessment with inline week info → Rejected: Spec requires overview timeline table

---

### 4. Cross-Reference Link Strategy

**Decision**: Use Docusaurus-style relative links with descriptive text

**Rationale**:
- Docusaurus handles link resolution automatically
- Relative paths are deployment-environment agnostic
- Descriptive link text improves accessibility and SEO
- Links will be validated during build process

**Link Format**:
```markdown
[Weekly Course Schedule](/docs/weekly-schedule)
[Capstone: The Autonomous Humanoid](/docs/module4-vision-language-action/04-capstone-the-autonomous-humanoid)
```

**Alternatives Considered**:
- Absolute URLs → Rejected: Breaks in local development, not portable
- File path references → Rejected: Not clickable, poor UX

---

### 5. Accessibility and SEO Optimization

**Decision**: Use semantic HTML via Markdown, descriptive frontmatter, proper heading hierarchy

**Rationale**:
- Docusaurus automatically handles mobile responsiveness
- Proper H1 (title) → H2 (sections) → H3 (subsections) hierarchy for screen readers
- Frontmatter `description` field becomes meta description for SEO
- Table headers (`| Header |`) provide accessible context
- Standard Markdown generates semantic HTML

**Frontmatter Configuration**:
```yaml
---
id: assessments
title: Assessments & Projects
sidebar_position: 3
description: Comprehensive guide to all 4 course assessments including ROS 2 package development, Gazebo simulation, Isaac pipeline, and the capstone project with detailed grading rubrics.
---
```

**Alternatives Considered**:
- Custom meta tags via MDX → Rejected: Docusaurus frontmatter handles this natively
- ARIA labels on tables → Rejected: Markdown tables already accessible

---

## Content Structure Decisions

### Page Outline (Final)

1. **Front Matter** (id, title, sidebar_position, description)
2. **Introduction** (1-2 paragraphs: assessment philosophy, continuous evaluation)
3. **Assessment Timeline Table** (4 assessments mapped to weeks/modules)
4. **Assessment 1: ROS 2 Package Development Project**
   - Learning Objectives (3-4 bullets)
   - Project Requirements (4-6 specific deliverables)
   - Grading Rubric (100-point table)
   - Submission Guidelines (format, deadline, files)
5. **Assessment 2: Gazebo Simulation Implementation** (same structure)
6. **Assessment 3: Isaac-based Perception Pipeline** (same structure)
7. **Assessment 4: Capstone Project - The Autonomous Humanoid** (same structure + milestones)
8. **Submission & Academic Integrity** (brief section on policies)
9. **Cross-References** (links to Weekly Schedule, Capstone chapter)

**Estimated Length**: 2000-2500 words total

---

## Dependencies Verified

1. ✅ **Weekly Schedule Page** exists at `docs/weekly-schedule.mdx` (confirmed from previous implementation)
2. ✅ **Capstone Chapter** exists at `docs/module4-vision-language-action/04-capstone-the-autonomous-humanoid.mdx`
3. ✅ **Sidebar Configuration** in `sidebars.ts` supports standalone pages (confirmed from weekly-schedule implementation)
4. ✅ **Hackathon PDF** at `doc/Hackathon I.pdf` page 4 contains assessment requirements (verified)

---

## Best Practices Applied

1. **Content-First Design**: Start with information architecture, not visual design
2. **Progressive Disclosure**: Overview first (timeline table), then details (each assessment)
3. **Scannability**: Use tables, headings, bullet points for quick comprehension
4. **Consistency**: Match structure of Weekly Schedule page for familiar UX
5. **Accessibility**: Semantic HTML, proper heading hierarchy, table headers
6. **Maintainability**: Pure Markdown (no custom components) for easy updates by non-developers

---

## Research Complete

All technical unknowns resolved. Ready to proceed to Phase 1 (Data Model & Contracts).
