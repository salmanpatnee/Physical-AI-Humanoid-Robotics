---
id: 002
title: Implementation Plan with Real-Life Analogies
stage: plan
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-simplified-content
branch: 001-simplified-content
user: salmanpatnee
command: /sp.plan
labels: ["planning", "architecture", "component-design", "analogies", "educational-content"]
links:
  spec: specs/001-simplified-content/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-simplified-content/plan.md
  - history/prompts/001-simplified-content/002-implementation-plan-with-analogies.plan.prompt.md
tests:
  - Constitution check (all gates passed)
  - Component API contract validation (schemas defined)
---

## Prompt

Use the quality content, add real life analogy examples and questions

## Response snapshot

Created comprehensive implementation plan for child-friendly content simplification with extensive real-life analogy bank and question patterns.

**Planning Outputs**:

1. **Complete Implementation Plan** (plan.md - 1009 lines)
   - Technical context with performance goals and constraints
   - Constitution check (all gates passed)
   - Phase 0: Research tasks for simplification guidelines, analogy bank, question templates
   - Phase 1: Component design with 5 entities and 4 contract schemas
   - Quickstart guide for content writers and reviewers

2. **Real-Life Analogy Bank** (embedded in plan)
   - 10 core robotics concepts mapped to child-friendly analogies
   - Examples: "ROS2 Topics = walkie-talkie channels", "Middleware = school bus system", "VSLAM = drawing a map while exploring"
   - Target analogy domains: school activities, sports/games, home activities, nature

3. **Doubtful Question Patterns** (5 confusion categories)
   - Terminology mixups: "Is ROS2 the same as Python?"
   - Why vs how: "Why use middleware instead of direct connections?"
   - Scope/scale: "Does every robot have 20+ motors?"
   - Simulation vs reality: "Will Gazebo code work on real robot?"
   - Abstract concepts: "How can robot 'think' without brain?"
   - Template: Pattern + Example + Answer Framework

4. **Component Designs with Examples**:
   - **WhatYouWillLearn**: 3-5 learning goals with icons and "why it matters" explanations
   - **DoubtfulQA**: 5-8 Q&A pairs with misconception addressing and visual aids
   - **GrownUpWords**: Simple-to-technical term mappings with context examples
   - **CodeBlockWithExplanation**: Plain-language code annotations with step-by-step breakdowns and analogies

5. **Example Analogies with Real Usage**:
   ```
   Q: "Why can't robot parts just talk directly instead of middleware?"
   A: "Imagine if every student had to remember everyone's phone number to share homework.
       Middleware is like a class announcement system - say your message once,
       everyone who wants to hear it can listen!"
   ```

6. **Simplification Guidelines**:
   - Reading level: Flesch-Kincaid Grade 3-6
   - Sentence length: 12-15 words average, 20 max
   - Active voice: 80%+ of sentences
   - Forbidden jargon list with approved replacements
   - Analogy quality standards

**Architectural Decisions** (ADR candidates):
1. Component-based enhancement vs full rewrite → Chose components for gradual rollout
2. Inline Q&A vs separate FAQ → Chose inline for contextual help
3. Reading level target → Grades 3-6 balances simplicity with technical accuracy

**Structure**:
- Preserves existing Docusaurus structure
- New components in `/src/components/`
- Content scripts in `/scripts/simplify-content/`
- All content remains in MDX files with embedded components

**Scope**:
- 19 chapters across 4 modules
- 200-300 "Doubtful Questions" total
- 100-150 code examples to annotate
- 50+ analogies in analogy bank

## Outcome

- ✅ Impact: Complete architecture plan with rich analogy library and question patterns as requested. Provides concrete component designs with TypeScript interfaces, JSON schemas, and usage examples.
- 🧪 Tests: Constitution compliance check passed (all Articles I, III, IV, VI satisfied)
- 📁 Files: Created plan.md (1009 lines) with embedded contracts, schemas, guidelines, and examples
- 🔁 Next prompts: Phase 0 research execution (optional) or `/sp.tasks` to generate implementation tasks
- 🧠 Reflection: Plan balances user request for "5-year-old understanding" with technical accuracy requirements by targeting grades 3-6 reading level. Extensive analogy examples (middleware=school announcements, VSLAM=drawing map while exploring, GPU=100 helpers vs 1) provide concrete guidance. Question patterns address 5 confusion categories with specific examples and answer frameworks.

## Evaluation notes (flywheel)

- Failure modes observed: None - plan includes all requested elements (analogies, questions, quality content)
- Graders run and results (PASS/FAIL): Constitution Check - PASS (all gates), Component schema validation - PASS (well-formed JSON schemas)
- Prompt variant (if applicable): Standard /sp.plan workflow with user instruction to emphasize analogies and questions
- Next experiment (smallest change to try): Consider A/B testing different analogy domains (school vs home vs nature) to optimize comprehension for different learner preferences
