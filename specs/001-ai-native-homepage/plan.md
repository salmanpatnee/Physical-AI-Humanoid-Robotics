# Implementation Plan: Physical AI Humanoid Robotics Landing Page

**Branch**: `001-ai-native-homepage` | **Date**: 2025-12-05 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-ai-native-homepage/spec.md`

## Summary

Update the Docusaurus homepage to showcase the Physical AI Humanoid Robotics book with a comprehensive landing page featuring: hero section with book title and CTA, robotics development spectrum cards, book differentiator cards, implementation maturity levels (0-5), transformation journey content, and updated footer. The page must be fully responsive, accessible (WCAG 2.1 AA), and optimized for engagement.

**Technical Approach**: Refactor existing React/TypeScript homepage components in Docusaurus 3.9.2, creating modular, reusable components for each section (HeroSection, SpectrumCards, DifferentiatorCards, MaturityLevels, TransformationSection). Use CSS modules for styling, maintain Docusaurus theming integration, and ensure mobile-first responsive design.

## Technical Context

**Language/Version**: TypeScript 5.6.2, Node.js >=20.0
**Primary Dependencies**:
- Docusaurus 3.9.2 (static site generator)
- React 19.0.0 (UI framework)
- MDX 3.0.0 (markdown with JSX)
- Prism React Renderer 2.3.0 (code syntax highlighting)
- clsx 2.0.0 (conditional classNames utility)

**Storage**: Static files (no database required)
**Testing**: Playwright 1.57.0 for E2E testing
**Target Platform**: Web (static site), GitHub Pages deployment, modern browsers (>0.5% usage, not IE)
**Project Type**: Web application (static documentation site with custom landing page)
**Performance Goals**:
- Page load time <2 seconds (Lighthouse Performance score 90+)
- Time to Interactive (TTI) <3 seconds
- First Contentful Paint (FCP) <1 second
- Lighthouse Accessibility score 95+

**Constraints**:
- Must maintain Docusaurus theming and navigation integration
- Responsive breakpoints: mobile (375px), tablet (768px), desktop (1024px+)
- WCAG 2.1 AA compliance for accessibility
- SEO meta tags for all sections
- No external API dependencies

**Scale/Scope**:
- Single landing page with 6 major sections
- ~10-15 React components (including sub-components)
- 3 spectrum cards, 4+ differentiator cards, 6 maturity level cards
- Estimated 500-800 lines of TypeScript/TSX
- 200-300 lines of CSS modules

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Article I: Core Principles Compliance

| Principle | Status | Notes |
|-----------|--------|-------|
| **Deterministic Generation** | ✅ PASS | Static React components with deterministic rendering; no runtime data fetching |
| **Reproducibility** | ✅ PASS | Component-based architecture allows full reproducibility; version-controlled source |
| **Composability** | ✅ PASS | Modular component design (HeroSection, SpectrumCards, etc.) enables reuse |
| **Human Override & Oversight** | ✅ PASS | All design decisions documented; human approval required for deployment |
| **Anti-Hallucination Mandate** | ✅ PASS | All content derived from specification; no AI-generated content in production code |

### Article IV: Quality Standards Compliance

| Standard | Status | Implementation |
|----------|--------|----------------|
| **Markdown Correctness** | ✅ PASS | Using MDX for any markdown content; TypeScript for component logic |
| **Docusaurus Structure** | ✅ PASS | Homepage at `src/pages/index.tsx`; components in `src/components/` |
| **Front-Matter Format** | N/A | Not applicable - homepage is TSX, not markdown |
| **Deterministic Output** | ✅ PASS | React components produce consistent output from same props |
| **Consistent Naming** | ✅ PASS | Following existing conventions: PascalCase for components, camelCase for utilities |

### Article V: Folder Structure Compliance

**Current Structure (Preserved)**:
```
src/
├── components/           # Reusable React components
│   ├── ExerciseBlock/
│   ├── HomepageFeatures/ # Will be extended
│   ├── KeyTakeaways/
│   ├── LearningGoals/
│   └── Prerequisites/
├── css/                  # Global styles
│   └── custom.css
├── pages/                # Docusaurus pages
│   ├── index.tsx         # Homepage (will be updated)
│   ├── index.module.css  # Homepage styles
│   └── markdown-page.md
├── plugins/              # Custom Docusaurus plugins
│   └── chapter-validation/
└── theme/                # Theme customizations
```

**New Structure (To Be Added)**:
```
src/components/
├── Homepage/                      # New: Homepage-specific components
│   ├── HeroSection/
│   │   ├── index.tsx
│   │   └── styles.module.css
│   ├── RoboticsSpectrum/
│   │   ├── index.tsx
│   │   ├── SpectrumCard.tsx
│   │   └── styles.module.css
│   ├── BookDifferentiators/
│   │   ├── index.tsx
│   │   ├── DifferentiatorCard.tsx
│   │   └── styles.module.css
│   ├── MaturityLevels/
│   │   ├── index.tsx
│   │   ├── MaturityCard.tsx
│   │   └── styles.module.css
│   └── TransformationSection/
│       ├── index.tsx
│       └── styles.module.css
```

### Article VI: AI Behavior Governance

| Requirement | Status | Notes |
|-------------|--------|-------|
| **Strict Spec Adherence** | ✅ PASS | All requirements from spec.md will be implemented as specified |
| **Content from Source Material** | ✅ PASS | All text content will be provided from spec or require human input |
| **Deterministic Outputs** | ✅ PASS | React components are deterministic |
| **Flag Ambiguities** | ✅ PASS | Marked in Technical Context and research.md |
| **No Self-Expansion** | ✅ PASS | No modifications to spec; only implementation per spec |
| **No Test Generation** | ✅ PASS | Tests only created if explicitly requested in tasks phase |

**Gates Summary**: ✅ **ALL GATES PASSED** - Ready for Phase 0 research

## Project Structure

### Documentation (this feature)

```text
specs/001-ai-native-homepage/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (to be generated)
├── data-model.md        # Phase 1 output (to be generated)
├── quickstart.md        # Phase 1 output (to be generated)
├── contracts/           # Phase 1 output (to be generated)
│   └── components.ts    # Component props interfaces
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
# Web application structure (Docusaurus site)
src/
├── components/
│   ├── Homepage/                      # New: Landing page components
│   │   ├── HeroSection/
│   │   │   ├── index.tsx              # Hero section component
│   │   │   └── styles.module.css      # Hero styles
│   │   ├── RoboticsSpectrum/
│   │   │   ├── index.tsx              # Spectrum section container
│   │   │   ├── SpectrumCard.tsx       # Individual spectrum card
│   │   │   └── styles.module.css      # Spectrum styles
│   │   ├── BookDifferentiators/
│   │   │   ├── index.tsx              # Differentiators section container
│   │   │   ├── DifferentiatorCard.tsx # Individual differentiator card
│   │   │   └── styles.module.css      # Differentiator styles
│   │   ├── MaturityLevels/
│   │   │   ├── index.tsx              # Maturity section container
│   │   │   ├── MaturityCard.tsx       # Individual maturity level card
│   │   │   └── styles.module.css      # Maturity styles
│   │   └── TransformationSection/
│   │       ├── index.tsx              # Transformation content section
│   │       └── styles.module.css      # Transformation styles
│   └── [existing components...]       # ExerciseBlock, KeyTakeaways, etc.
├── css/
│   └── custom.css                     # Global styles (may need updates)
├── pages/
│   ├── index.tsx                      # Homepage (MODIFIED: integrate new sections)
│   └── index.module.css               # Homepage layout styles (MODIFIED)
└── theme/                             # Docusaurus theme overrides (if needed)

static/
└── img/
    └── homepage/                      # New: Homepage-specific images
        ├── hero-bg.jpg                # Hero background image
        ├── spectrum-*.svg             # Spectrum card icons/images
        ├── differentiator-*.svg       # Differentiator card icons
        └── maturity-*.svg             # Maturity level icons

tests/
└── e2e/
    └── homepage.spec.ts               # New: Playwright E2E tests for homepage
```

**Structure Decision**: Selected "Web application" structure as this is a Docusaurus-based static documentation site. The existing structure is preserved, with new homepage components added under `src/components/Homepage/` for clear organization and separation of concerns. Each major homepage section gets its own directory with component and styles co-located for maintainability.

## Complexity Tracking

> No constitutional violations detected. This section intentionally left empty.

## Phase 0: Research & Technical Decisions

**Status**: ✅ READY TO EXECUTE

**Unknowns to Research**:

1. **Responsive Design Patterns for Docusaurus**
   - Question: What are the best practices for responsive layouts in Docusaurus 3.x?
   - Research: Docusaurus responsive breakpoints, CSS modules patterns, mobile-first approach
   - Decision criteria: Consistency with existing Docusaurus components, accessibility

2. **Accessibility Best Practices for Card-Based Layouts**
   - Question: How to ensure WCAG 2.1 AA compliance for card grids (spectrum, differentiators, maturity)?
   - Research: ARIA labels, semantic HTML, keyboard navigation, screen reader compatibility
   - Decision criteria: Lighthouse accessibility score 95+, keyboard-only navigation support

3. **Hero Section Background Image Optimization**
   - Question: Best approach for responsive background images in Docusaurus?
   - Research: Image formats (WebP, JPEG), lazy loading, srcset for different resolutions
   - Decision criteria: <2s load time, support for retina displays

4. **Component State Management**
   - Question: Do any sections require state (e.g., expanded cards, active maturity level)?
   - Research: React hooks for minimal stateful interactions if needed
   - Decision criteria: Keep components stateless where possible per constitution

5. **Icon/Image Assets Strategy**
   - Question: Source for robotics-themed icons (spectrum, differentiators, maturity levels)?
   - Research: Icon libraries (Heroicons, Lucide, custom SVGs), Docusaurus static asset handling
   - Decision criteria: Scalable SVGs, consistent visual style, small file sizes

6. **SEO and Meta Tags**
   - Question: How to optimize SEO for the landing page in Docusaurus?
   - Research: Docusaurus SEO plugin, meta tags, Open Graph, structured data
   - Decision criteria: Proper meta description, OG tags, Twitter cards

**Research Outputs**: research.md (to be generated)

## Phase 1: Design & Contracts

**Status**: PENDING (after Phase 0 complete)

### Data Model

**Entities to Define** (in data-model.md):

1. **SpectrumCardData**
   - Fields: title, description, order, iconPath
   - Represents one of three robotics development paradigms

2. **DifferentiatorCardData**
   - Fields: title, description, iconPath, order
   - Represents a unique book benefit/feature

3. **MaturityLevelData**
   - Fields: level (0-5), title, description, characteristics[]
   - Represents one organizational maturity stage

4. **HeroSectionData**
   - Fields: title, tagline, ctaText, ctaLink, backgroundImage
   - Hero section configuration

5. **TransformationSectionData**
   - Fields: heading, content (markdown/JSX)
   - Transformation journey content

### API Contracts

**Component Interfaces** (in contracts/components.ts):

```typescript
// Hero Section
interface HeroSectionProps {
  title: string;
  tagline: string;
  ctaText: string;
  ctaLink: string;
  backgroundImage?: string;
}

// Spectrum Card
interface SpectrumCardProps {
  title: string;
  description: string;
  icon: React.ComponentType<React.SVGProps<SVGSVGElement>>;
  order: number;
}

// Differentiator Card
interface DifferentiatorCardProps {
  title: string;
  description: string;
  icon: React.ComponentType<React.SVGProps<SVGSVGElement>>;
}

// Maturity Level Card
interface MaturityLevelCardProps {
  level: number;
  title: string;
  description: string;
  characteristics: string[];
}

// Transformation Section
interface TransformationSectionProps {
  heading: string;
  content: React.ReactNode;
}
```

**No external APIs required** - all data is static and configured in component props.

### Quickstart Guide

To be created in quickstart.md covering:
- How to run the development server
- How to modify homepage content (card text, images, etc.)
- How to add/remove differentiator or maturity cards
- How to test responsive layouts
- How to deploy to GitHub Pages

## Phase 2: Task Generation

**Status**: NOT STARTED (handled by `/sp.tasks` command)

Tasks will be generated based on this plan in the `/sp.tasks` phase, breaking down implementation into:
- Component creation tasks (one per major section)
- Styling and responsiveness tasks
- Accessibility implementation tasks
- Image asset integration tasks
- Testing tasks (if explicitly requested)
- Documentation update tasks

## Open Questions & Risks

### Open Questions (to be resolved in Phase 0)

1. **Content Text**: Do we have finalized text for all card descriptions, or should placeholders be used initially?
   - **Impact**: Affects whether we can complete implementation or need content review phase
   - **Resolution**: Check with stakeholders during task execution

2. **Icon Assets**: Are robotics-themed icons available, or do we need to source/create them?
   - **Impact**: May need design phase for custom icons
   - **Resolution**: Research icon libraries in Phase 0

3. **Maturity Level Detail**: Should maturity levels be expandable/interactive, or static cards?
   - **Impact**: Affects component complexity and state management
   - **Resolution**: Review spec - no interactivity specified, keep static per simplicity principle

### Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Image assets not available** | High - blocks hero section | Use placeholder images initially; document asset requirements |
| **Content not finalized** | Medium - delays completion | Use spec-provided content; create clear placeholders for missing text |
| **Accessibility issues** | High - blocks deployment | Early accessibility testing; use semantic HTML; automated Lighthouse checks |
| **Responsive layout challenges** | Medium - UX impact | Mobile-first design; test on actual devices; use Docusaurus patterns |
| **Performance degradation** | Medium - user experience | Optimize images; lazy loading; monitor Lighthouse performance score |

## Implementation Strategy

### Phased Rollout

**Phase 1: Core Structure** (P1 - Hero Section)
- Implement HeroSection component
- Integrate with homepage
- Test responsiveness and accessibility
- **Deliverable**: Functioning hero with title, tagline, CTA

**Phase 2: Content Sections** (P2 - Spectrum & Differentiators)
- Implement RoboticsSpectrum component with 3 cards
- Implement BookDifferentiators component with 4+ cards
- **Deliverable**: Two major content sections functional

**Phase 3: Advanced Sections** (P3 - Maturity & Transformation)
- Implement MaturityLevels component with 6 level cards
- Implement TransformationSection component
- **Deliverable**: All sections complete

**Phase 4: Polish & Optimization**
- Responsive refinements across all breakpoints
- Accessibility audit and fixes
- Performance optimization (image lazy loading, etc.)
- Footer updates (if needed)
- **Deliverable**: Production-ready landing page

### Testing Strategy

**Manual Testing**:
- Visual QA on mobile (375px), tablet (768px), desktop (1024px+)
- Cross-browser testing (Chrome, Firefox, Safari)
- Keyboard navigation testing
- Screen reader testing (NVDA/JAWS)

**Automated Testing** (if requested in tasks phase):
- Playwright E2E tests for user scenarios from spec
- Lighthouse CI for performance/accessibility scores
- Visual regression testing (optional)

### Deployment Checklist

- [ ] All acceptance scenarios from spec pass
- [ ] Lighthouse Performance score ≥90
- [ ] Lighthouse Accessibility score ≥95
- [ ] Responsive on all three breakpoints
- [ ] No console errors or warnings
- [ ] All images have alt text
- [ ] SEO meta tags present
- [ ] GitHub Pages build succeeds
- [ ] Human review and approval

## Dependencies & Prerequisites

**External Dependencies**:
- None (all dependencies already in package.json)

**Asset Dependencies**:
- Hero background image (humanoid robotics themed)
- 3 spectrum card icons/images
- 4+ differentiator card icons
- 6 maturity level icons
- All images must be optimized and responsive-ready

**Human Input Required**:
- Final approval of content text for all cards
- Design review of layout and styling
- Accessibility review
- Final deployment approval

## Next Steps

1. ✅ **Complete**: `/sp.plan` - This implementation plan
2. **Next**: Generate research.md (Phase 0) - Resolve all open technical questions
3. **Then**: Generate data-model.md and contracts/ (Phase 1) - Define component interfaces
4. **Then**: `/sp.tasks` - Generate actionable, testable implementation tasks
5. **Finally**: Implementation and deployment per tasks

---

**Plan Status**: ✅ **COMPLETE AND VALIDATED**
**Constitution Compliance**: ✅ **ALL GATES PASSED**
**Ready for**: Phase 0 Research (research.md generation)
