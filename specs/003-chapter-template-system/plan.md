# Implementation Plan: Reusable Chapter Template System

**Branch**: `003-chapter-template-system` | **Date**: 2025-12-04 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/003-chapter-template-system/spec.md`

## Summary

This plan outlines the technical implementation for a reusable chapter template system within the Docusaurus-based 'Physical AI & Humanoid Robotics Textbook'. The system will enforce consistency across all chapters using a flexible template that supports four content types (tutorial, concept, lab, reference). It includes custom MDX/React components for learning elements like `<LearningGoals>`, `<Prerequisites>`, `<KeyTakeaways>`, and an interactive `<ExerciseBlock>`. Chapter metadata will be validated against a JSON Schema using AJV during the build process to ensure structural integrity.

## Technical Context

**Language/Version**: TypeScript (for Docusaurus and React components)
**Primary Dependencies**: Docusaurus 3, React 18, MDX, AJV
**Storage**: N/A (Content is stored as `.mdx` files in the git repository)
**Testing**: Jest (for component and schema validation logic), Playwright (for E2E tests of component interactivity)
**Target Platform**: Web (via Docusaurus static site generation)
**Project Type**: Docusaurus project (single `src` directory structure)
**Performance Goals**: Docusaurus build time should not increase by more than 10% after integrating the new components and validation logic for 50+ chapters.
**Constraints**: Components must be server-side rendered (SSR) compatible as per Docusaurus 3 MDX architecture. The `<ExerciseBlock>` must be accessible, using semantic HTML like `<details>`.
**Scale/Scope**: The system must support 50+ chapters and be easily extensible for new components or chapter types.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Principle I: Deterministic Generation**: PASS. The system uses templates and schema validation, ensuring consistent output from the same source files.
- **Principle II: Reproducibility**: PASS. The entire site, including templated chapters, can be rebuilt from the source code.
- **Principle III: Composability**: PASS. The feature is built around modular React components (`<LearningGoals>`, etc.) designed for reuse.
- **Principle IV: Human Override & Oversight**: PASS. Authors (humans) create and edit the `.mdx` content directly, maintaining full control.
- **Principle V: Anti-Hallucination Mandate**: PASS. All content is human-written; the system only provides structure and formatting.

## Project Structure

### Documentation (this feature)

```text
specs/003-chapter-template-system/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   ├── ChapterMetadata.schema.json
│   └── component-props.ts
└── tasks.md             # Phase 2 output (created by /sp.tasks)
```

### Source Code (repository root)

```text
src/
├── components/
│   ├── LearningGoals/
│   │   ├── index.tsx
│   │   └── styles.module.css
│   ├── Prerequisites/
│   │   ├── index.tsx
│   │   └── styles.module.css
│   ├── KeyTakeaways/
│   │   ├── index.tsx
│   │   └── styles.module.css
│   └── ExerciseBlock/
│       ├── index.tsx
│       └── styles.module.css
├── theme/
│   └── MDXComponents.ts   # Mapping custom components to MDX
└── plugins/
    └── chapter-validation/  # Custom Docusaurus plugin for AJV schema validation
        ├── index.js
        └── schemas.js

tests/
└── unit/
    ├── components/
    │   └── ExerciseBlock.test.tsx
    └── plugins/
        └── chapter-validation.test.js
```

**Structure Decision**: The project is a single Docusaurus web application. New functionality will be added by creating new React components in `src/components`, registering them for MDX usage in `src/theme`, and adding a custom Docusaurus plugin for build-time validation in `src/plugins`. This aligns with Docusaurus best practices.

## Complexity Tracking

No constitutional violations detected or justified.