---
id: 003
title: Implementation Plan Creation
stage: plan
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5
feature: 001-ai-native-homepage
branch: 001-ai-native-homepage
user: user
command: /sp.plan
labels: ["planning", "architecture", "docusaurus", "react", "homepage"]
links:
  spec: ../../specs/001-ai-native-homepage/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-ai-native-homepage/plan.md
  - specs/001-ai-native-homepage/research.md
  - specs/001-ai-native-homepage/data-model.md
  - specs/001-ai-native-homepage/quickstart.md
  - specs/001-ai-native-homepage/contracts/components.ts
  - CLAUDE.md (updated with agent context)
tests:
  - None (planning phase - no tests yet)
---

## Prompt

Now write the technical prompt using /sp.plan

## Response snapshot

Created comprehensive implementation plan for Physical AI Humanoid Robotics landing page with complete Phase 0 (Research) and Phase 1 (Design & Contracts) deliverables.

**Planning Artifacts Created:**

1. **plan.md** - Complete implementation plan including:
   - Technical Context: TypeScript 5.6.2, Docusaurus 3.9.2, React 19.0, Node >=20.0
   - Constitution Check: All gates passed (deterministic generation, reproducibility, composability, etc.)
   - Project Structure: Detailed file organization for new homepage components
   - Complexity Tracking: No violations detected
   - Phase 0: Research unknowns identified (6 items)
   - Phase 1: Data model and contracts defined
   - Phase 2: Task generation (deferred to /sp.tasks command)
   - Implementation Strategy: Phased rollout (P1 Hero → P2 Spectrum/Differentiators → P3 Maturity/Transformation → Polish)
   - Open Questions & Risks documented
   - Dependencies & Prerequisites identified

2. **research.md** - Resolved all 6 technical unknowns:
   - Responsive Design: CSS Modules + Docusaurus breakpoints, mobile-first
   - Accessibility: Semantic HTML + ARIA + WCAG 2.1 AA compliance
   - Hero Background: CSS background-image, WebP + JPEG fallback, image-set()
   - State Management: Stateless components (no state required per spec)
   - Icons/Images: Lucide React + custom SVGs for robotics themes
   - SEO: Docusaurus Layout + Open Graph/Twitter Card meta tags

3. **data-model.md** - Defined 5 core entities:
   - HeroSectionData: title, tagline, ctaText, ctaLink, backgroundImage
   - SpectrumCardData: id, title, description, icon, order (exactly 3 cards)
   - DifferentiatorCardData: id, title, description, icon, order (minimum 4 cards)
   - MaturityLevelData: level (0-5), title, description, characteristics[] (exactly 6 cards)
   - TransformationSectionData: heading, content
   - Data relationships and validation rules documented

4. **contracts/components.ts** - TypeScript interfaces for:
   - All data entity types
   - Component prop interfaces (HeroSectionProps, SpectrumCardProps, DifferentiatorCardProps, MaturityCardProps, TransformationSectionProps)
   - Container component props (RoboticsSpectrumProps, BookDifferentiatorsProps, MaturityLevelsProps)
   - Utility types and type guards
   - Complete JSDoc comments with usage examples

5. **quickstart.md** - Developer guide covering:
   - Prerequisites and development setup
   - Project structure overview
   - Common development tasks (modify content, add/remove cards, change styling, replace images, update SEO)
   - Testing strategies (manual, automated Lighthouse, Playwright)
   - Deployment instructions (GitHub Pages, Netlify, Vercel)
   - Troubleshooting common issues
   - Best practices and quick reference commands

6. **Agent Context Updated** - CLAUDE.md updated with:
   - Language: TypeScript 5.6.2, Node.js >=20.0
   - Database: Static files (no database required)
   - Project type information

**Technical Approach:**

- **Stack**: Docusaurus 3.9.2 static site generator with React 19.0 and TypeScript 5.6
- **Components**: Modular, reusable components under `src/components/Homepage/`
- **Styling**: CSS Modules co-located with components, mobile-first responsive design
- **Icons**: Lucide React for standard icons, custom SVGs for robotics-specific imagery
- **State**: Stateless components (per constitution principle)
- **Accessibility**: WCAG 2.1 AA compliance, semantic HTML, ARIA labels
- **Performance**: Target <2s page load, Lighthouse score 90+ performance, 95+ accessibility
- **SEO**: Open Graph and Twitter Card meta tags for social sharing

**Project Structure Decision:**

Selected "Web application" structure for Docusaurus static site. New homepage components organized under `src/components/Homepage/` with each major section in its own directory:
- HeroSection/
- RoboticsSpectrum/
- BookDifferentiators/
- MaturityLevels/
- TransformationSection/

Each directory contains: index.tsx (component), styles.module.css (styles), *Config.ts (content data).

**Constitution Compliance:**

✅ All gates passed:
- Deterministic Generation: Static React components
- Reproducibility: Version-controlled, component-based
- Composability: Modular components for reuse
- Human Oversight: All decisions documented, deployment requires approval
- Anti-Hallucination: All content from spec or requires human input

**Research Decisions Summary:**

| Area | Decision | Rationale |
|------|----------|-----------|
| Responsive Design | CSS Modules + mobile-first | Native Docusaurus approach |
| Accessibility | Semantic HTML + ARIA | WCAG 2.1 AA compliance |
| Hero Images | WebP + JPEG, image-set() | <2s load, retina support |
| State | Stateless components | No interactivity in spec |
| Icons | Lucide React + custom SVGs | Tree-shakeable, robotics-themed |
| SEO | Docusaurus Layout + OG tags | Built-in support, social optimization |

**Data Model Highlights:**

- 5 entity types with validation rules
- Fixed cardinalities: 1 hero, 3 spectrum, 4+ differentiators, 6 maturity levels, 1 transformation
- Static configuration in TypeScript (no database)
- TypeScript interfaces ensure type safety

**Implementation Strategy:**

Phased rollout aligned with spec priorities:
1. **Phase 1**: Hero Section (P1) - Core structure and CTA
2. **Phase 2**: Content Sections (P2) - Spectrum and Differentiators
3. **Phase 3**: Advanced Sections (P3) - Maturity Levels and Transformation
4. **Phase 4**: Polish & Optimization - Responsiveness, accessibility, performance

**Open Questions:**

1. Content text finalization (placeholders vs. actual content)
2. Icon assets availability (Lucide sufficient or need custom designs)
3. Maturity level interactivity (static cards per spec, but confirming no expansion needed)

**Risks & Mitigations:**

- Image assets not available → Use placeholders, document requirements
- Content not finalized → Use spec content, create clear placeholders
- Accessibility issues → Early testing, semantic HTML, Lighthouse audits
- Responsive layout challenges → Mobile-first design, test on devices
- Performance degradation → Optimize images, lazy loading, monitor scores

## Outcome

- ✅ Impact: Created complete implementation plan with all Phase 0 research and Phase 1 design artifacts. Provides clear technical roadmap for implementing Physical AI Humanoid Robotics landing page in Docusaurus. All unknowns resolved, component interfaces defined, developer guide created.
- 🧪 Tests: No tests at planning phase. Testing strategy defined in plan.md for implementation phase.
- 📁 Files: Created 5 planning artifacts (plan.md, research.md, data-model.md, contracts/components.ts, quickstart.md) and updated 1 file (CLAUDE.md). Total 438 lines of plan, 346 lines of research, 256 lines of data model, 328 lines of contracts, 537 lines of quickstart.
- 🔁 Next prompts: Ready for `/sp.tasks` to generate actionable, testable implementation tasks based on this plan
- 🧠 Reflection: Planning phase successfully completed with comprehensive technical decisions. All 6 research questions resolved with clear rationale. Component architecture is modular and reusable. Constitution compliance verified. Static, stateless approach aligns with Docusaurus philosophy and constitutional principles.

## Evaluation notes (flywheel)

- Failure modes observed: None - planning phase completed smoothly. All research questions had clear answers based on Docusaurus best practices and web standards.
- Graders run and results (PASS/FAIL): Constitution Check - PASSED all gates. Research decisions all have clear rationale and alternatives considered.
- Prompt variant (if applicable): Standard /sp.plan command workflow
- Next experiment (smallest change to try): Consider adding Storybook for component development isolation and visual testing (not in current scope but useful for component-heavy projects). Also consider adding Zod schemas for runtime config validation if content will come from external sources in future.
