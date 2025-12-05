# Implementation Plan: Site Visual Refresh

**Branch**: `011-site-visual-refresh` | **Date**: 2025-12-05 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `specs/011-site-visual-refresh/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This feature implements a site-wide visual refresh. The technical approach involves updating the `docusaurus.config.ts` file to change the site title, modify header navigation links, and update footer links. It also requires changing the primary color variable in `src/css/custom.css` to a gray theme and improving the readability of the `LearningGoals` React component by adjusting its stylesheet.

## Technical Context

**Language/Version**: TypeScript, CSS
**Primary Dependencies**: Docusaurus v3, React
**Storage**: N/A
**Testing**: Playwright (for existing e2e tests). Unit testing framework for components is not explicitly defined.
**Target Platform**: Web (via GitHub Pages)
**Project Type**: Web application
**Performance Goals**: Maintain fast page load times and high Lighthouse scores (as per spec SC-004).
**Constraints**: All changes must be consistent across the site and must not negatively impact existing functionality or accessibility.
**Scale/Scope**: The changes are global, affecting shared components like the header, footer, and site-wide CSS.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Determinism**: PASS. Changes are in configuration and CSS, which are deterministic.
- **Reproducibility**: PASS. All changes will be committed to git.
- **Composability**: PASS. Changes are to existing modular components.
- **Human Oversight**: PASS. This plan is subject to human review.
- **Anti-Hallucination**: PASS. All changes are based on the user's explicit request.

All constitution gates pass.

## Project Structure

### Documentation (this feature)

```text
specs/011-site-visual-refresh/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

The implementation will modify existing files within the standard Docusaurus project structure.

```text
.
├── docusaurus.config.ts      # Main site configuration (title, navbar, footer)
└── src/
    ├── css/
    │   └── custom.css        # Site-wide custom styles (primary color)
    └── components/
        └── LearningGoals/
            └── index.tsx     # Or an associated style file for this component
```

**Structure Decision**: The plan is to modify existing files within the established Docusaurus architecture. No new files or structural changes are required for the core implementation.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| *None*      | -          | -                                   |
