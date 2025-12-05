# Research: Physical AI Humanoid Robotics Landing Page

**Feature**: 001-ai-native-homepage
**Date**: 2025-12-05
**Status**: ✅ Complete

## Purpose

This document consolidates research findings for all technical unknowns identified in plan.md Phase 0. Each research item includes the decision made, rationale, alternatives considered, and implementation guidance.

---

## Research Item 1: Responsive Design Patterns for Docusaurus

**Question**: What are the best practices for responsive layouts in Docusaurus 3.x?

### Decision

Use **CSS Modules with Docusaurus-native breakpoints** combined with mobile-first design approach and CSS Grid/Flexbox for layouts.

### Rationale

1. **Docusaurus 3.x uses Infima CSS framework** which provides standard breakpoints:
   - Mobile: `< 996px`
   - Desktop: `>= 996px`
   - Additional custom breakpoints can be defined via CSS variables

2. **CSS Modules are the recommended approach** in Docusaurus for component-specific styles:
   - Co-located with components (`.module.css` files)
   - Scoped styling prevents conflicts
   - Works seamlessly with Docusaurus build system

3. **Mobile-first approach** aligns with Docusaurus philosophy:
   - Define base styles for mobile
   - Use `@media (min-width: ...)` for larger screens
   - Ensures performance on mobile devices

### Implementation Guidance

```css
/* Component styles.module.css */
.container {
  /* Mobile-first base styles */
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

@media (min-width: 768px) {
  .container {
    /* Tablet styles */
    padding: 2rem;
    flex-direction: row;
    gap: 2rem;
  }
}

@media (min-width: 996px) {
  .container {
    /* Desktop styles (Docusaurus breakpoint) */
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

### Alternatives Considered

1. **Tailwind CSS**: Popular utility-first framework
   - **Rejected**: Adds dependency; conflicts with Docusaurus/Infima; steeper learning curve for content editors

2. **Styled Components**: CSS-in-JS solution
   - **Rejected**: Runtime overhead; not Docusaurus standard; increases bundle size

3. **Global CSS with BEM**: Traditional approach
   - **Rejected**: Harder to maintain; scope conflicts; CSS Modules preferred in React

---

## Research Item 2: Accessibility Best Practices for Card-Based Layouts

**Question**: How to ensure WCAG 2.1 AA compliance for card grids (spectrum, differentiators, maturity)?

### Decision

Use **semantic HTML with proper ARIA labels**, **keyboard navigation support**, and **sufficient color contrast**. Implement landmark regions and heading hierarchy.

### Rationale

1. **Semantic HTML as foundation**:
   - Use `<section>`, `<article>`, `<nav>` appropriately
   - Proper heading hierarchy (h1 → h2 → h3)
   - Lists (`<ul>`, `<li>`) for card containers

2. **ARIA labels for enhanced context**:
   - `aria-label` or `aria-labelledby` for sections
   - `role="region"` with `aria-labelledby` for major page sections
   - `aria-describedby` for card descriptions if needed

3. **Keyboard navigation**:
   - Ensure tab order is logical
   - Interactive elements (CTA buttons) must be keyboard accessible
   - Focus indicators visible (`outline` property)

4. **Color contrast**:
   - Text-to-background ratio ≥4.5:1 for normal text (WCAG AA)
   - Text-to-background ratio ≥3:1 for large text
   - Icons should not rely solely on color to convey meaning

### Implementation Guidance

```tsx
// Accessible card grid structure
<section
  className={styles.spectrumSection}
  aria-labelledby="spectrum-heading"
>
  <h2 id="spectrum-heading">Robotics Development Spectrum</h2>
  <ul className={styles.cardGrid} role="list">
    {cards.map((card) => (
      <li key={card.id} className={styles.cardItem}>
        <article className={styles.card}>
          <div className={styles.iconContainer} aria-hidden="true">
            <card.Icon />
          </div>
          <h3>{card.title}</h3>
          <p>{card.description}</p>
        </article>
      </li>
    ))}
  </ul>
</section>
```

**Key Accessibility Checklist**:
- ✅ Proper heading hierarchy (h1 for page, h2 for sections, h3 for cards)
- ✅ Landmark regions with labels
- ✅ Decorative icons marked with `aria-hidden="true"`
- ✅ Interactive elements keyboard accessible
- ✅ Focus indicators visible
- ✅ Color contrast meets WCAG AA standards
- ✅ Screen reader tested (NVDA/JAWS)

### Alternatives Considered

1. **Table-based layout for cards**:
   - **Rejected**: Not semantic for card content; harder to make responsive; poor screen reader experience

2. **Div soup with extensive ARIA**:
   - **Rejected**: Semantic HTML is preferred; less ARIA needed with proper HTML5 elements

---

## Research Item 3: Hero Section Background Image Optimization

**Question**: Best approach for responsive background images in Docusaurus?

### Decision

Use **CSS `background-image` with multiple image sources via `image-set()`** and serve **WebP with JPEG fallback**. Place optimized images in `/static/img/homepage/`.

### Rationale

1. **CSS background-image approach**:
   - Allows text overlay without complex positioning
   - Easy to control background size/position
   - Works well with Docusaurus static asset handling

2. **WebP format with fallback**:
   - WebP offers ~30% smaller file size vs JPEG at same quality
   - Broad browser support (96%+ as of 2024)
   - JPEG fallback for older browsers

3. **Responsive images via CSS `image-set()`**:
   - Serve different image sizes for different screen widths
   - Reduces bandwidth on mobile devices
   - Native CSS feature, no JavaScript required

4. **Lazy loading not needed for hero**:
   - Hero is above-the-fold (should load immediately)
   - Use `loading="lazy"` for images lower on page

### Implementation Guidance

**Image Optimization**:
- Generate multiple sizes: 400w (mobile), 800w (tablet), 1600w (desktop), 3200w (retina)
- Compress WebP to quality 80-85
- Compress JPEG to quality 75-80
- Tools: ImageOptim, Squoosh, Sharp

**CSS Implementation**:
```css
/* HeroSection styles.module.css */
.hero {
  background-image: image-set(
    url('/img/homepage/hero-bg-400.webp') 400w,
    url('/img/homepage/hero-bg-800.webp') 800w,
    url('/img/homepage/hero-bg-1600.webp') 1600w,
    url('/img/homepage/hero-bg-3200.webp') 3200w
  );
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

/* Fallback for browsers without image-set support */
.hero {
  background-image: url('/img/homepage/hero-bg-1600.jpg');
}

@supports (background-image: image-set(url('/test.webp') 1x)) {
  .hero {
    background-image: image-set(
      url('/img/homepage/hero-bg-400.webp') 400w,
      url('/img/homepage/hero-bg-800.webp') 800w,
      url('/img/homepage/hero-bg-1600.webp') 1600w
    );
  }
}
```

**File Structure**:
```
static/img/homepage/
├── hero-bg-400.webp
├── hero-bg-800.webp
├── hero-bg-1600.webp
├── hero-bg-3200.webp
└── hero-bg-1600.jpg (fallback)
```

### Alternatives Considered

1. **HTML `<img>` with `srcset`**:
   - **Rejected**: Harder to overlay text; requires positioning hacks; CSS background is cleaner for hero sections

2. **Inline SVG background**:
   - **Rejected**: Not suitable for photographic/complex imagery (robotics hero image)

3. **JavaScript-based lazy loading**:
   - **Rejected**: Unnecessary for above-the-fold content; adds complexity

---

## Research Item 4: Component State Management

**Question**: Do any sections require state (e.g., expanded cards, active maturity level)?

### Decision

**Keep all components stateless**. No interactive state management needed based on spec requirements.

### Rationale

1. **Spec does not require interactivity**:
   - All cards are static content displays
   - No expand/collapse behavior specified
   - No active/hover state persistence needed

2. **Simplicity per Constitution principle**:
   - Stateless components are easier to test
   - Deterministic rendering (Article I)
   - No client-side state to manage

3. **CSS-only interactions sufficient**:
   - Hover effects via CSS `:hover` pseudo-class
   - No need for onClick handlers or useState hooks

### Implementation Guidance

**Stateless Component Pattern**:
```tsx
// MaturityCard.tsx (example)
interface MaturityCardProps {
  level: number;
  title: string;
  description: string;
  characteristics: string[];
}

export function MaturityCard({
  level,
  title,
  description,
  characteristics
}: MaturityCardProps) {
  return (
    <article className={styles.card}>
      <div className={styles.levelBadge}>Level {level}</div>
      <h3>{title}</h3>
      <p>{description}</p>
      <ul>
        {characteristics.map((char, idx) => (
          <li key={idx}>{char}</li>
        ))}
      </ul>
    </article>
  );
}
```

**CSS Hover Effects**:
```css
.card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}
```

### Future Considerations

If interactivity is needed later (e.g., expandable cards):
- Use React `useState` hook for component-local state
- Consider `useReducer` if state logic becomes complex
- For global state (unlikely), Docusaurus context or Zustand library

**Current Decision**: No state management required for MVP.

---

## Research Item 5: Icon/Image Assets Strategy

**Question**: Source for robotics-themed icons (spectrum, differentiators, maturity levels)?

### Decision

Use **Lucide React icons** as primary icon library, supplemented with **custom robotics SVGs** for specific imagery.

### Rationale

1. **Lucide React benefits**:
   - Tree-shakeable (only import icons you use)
   - React components (no img tags needed)
   - Consistent design language
   - 1000+ icons including tech/industry themes
   - Actively maintained, good accessibility support
   - No additional dependencies (can be added to package.json)

2. **Custom SVGs for robotics-specific imagery**:
   - Humanoid robot illustrations
   - Physical AI system diagrams
   - Maturity level progress indicators
   - Source: custom design or royalty-free (unDraw, Storyset, etc.)

3. **SVG format advantages**:
   - Scalable (works at any size)
   - Small file size
   - Easy to style with CSS (color, size)
   - Accessible (can add `<title>` and `<desc>` elements)

### Implementation Guidance

**Install Lucide React**:
```bash
npm install lucide-react
```

**Usage in Components**:
```tsx
import { Bot, Brain, Cpu, Zap } from 'lucide-react';

// In component
<Bot className={styles.icon} size={48} aria-hidden="true" />
```

**Icon Mapping for Sections**:

**Robotics Spectrum (3 cards)**:
- Traditional: `Settings` or `Cog` icon
- AI-Enhanced: `Brain` or `Cpu` icon
- Physical AI: `Bot` or custom robot SVG

**Book Differentiators (4+ cards)**:
- Hands-on Learning: `Wrench` or `Tool` icon
- Real-world Applications: `Globe` or `Building` icon
- Cutting-edge Content: `Zap` or `Sparkles` icon
- Community Support: `Users` or `MessageCircle` icon

**Maturity Levels (6 cards)**:
- Levels 0-5: Numbered badges with `TrendingUp`, `BarChart`, or custom progress icons

**Custom SVG Storage**:
```
static/img/homepage/icons/
├── robot-traditional.svg
├── robot-enhanced.svg
├── robot-physical-ai.svg
└── maturity-badge-*.svg
```

### Alternatives Considered

1. **Heroicons**: Popular icon library
   - **Rejected**: Not available as React components out-of-box; requires additional setup

2. **Font Awesome**: Classic icon library
   - **Rejected**: Larger bundle size; font-based icons have accessibility issues; paid tier for some icons

3. **Material Icons**: Google's icon library
   - **Rejected**: Material Design style may not match Docusaurus theme; less flexible styling

4. **All custom SVGs**: Full custom design
   - **Rejected**: Time-consuming; Lucide provides 80% of needed icons; custom SVGs for remaining 20%

---

## Research Item 6: SEO and Meta Tags

**Question**: How to optimize SEO for the landing page in Docusaurus?

### Decision

Use **Docusaurus `<Layout>` component with `title` and `description` props**, add **Open Graph and Twitter Card meta tags**, and ensure proper **semantic HTML structure**.

### Rationale

1. **Docusaurus Layout component handles basic SEO**:
   - Automatically generates `<title>` and `<meta name="description">` tags
   - Inherits site-wide SEO config from `docusaurus.config.ts`
   - No additional plugins required for basic SEO

2. **Open Graph (OG) tags for social sharing**:
   - Facebook, LinkedIn, and other platforms use OG tags
   - Preview cards when page is shared on social media
   - Increases click-through rates

3. **Twitter Card tags for Twitter/X**:
   - Specific tags for Twitter's card format
   - Better-looking previews on Twitter

4. **Semantic HTML for search engines**:
   - Proper heading hierarchy (h1, h2, h3)
   - Landmark regions (header, main, section, footer)
   - Structured content helps search engines understand page structure

### Implementation Guidance

**Homepage Component (`src/pages/index.tsx`)**:
```tsx
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';

export default function Home() {
  const pageTitle = 'Physical AI Humanoid Robotics | Master ROS2, Isaac Sim, VLA';
  const pageDescription =
    'Comprehensive course on Physical AI and Humanoid Robotics. Learn ROS2, Isaac Sim, Vision-Language-Action models, and build intelligent robotic systems from scratch.';
  const pageImage = '/img/homepage/og-image.jpg'; // 1200x630px recommended
  const pageUrl = 'https://your-domain.com/'; // Update with actual URL

  return (
    <Layout
      title={pageTitle}
      description={pageDescription}
    >
      <Head>
        {/* Open Graph tags */}
        <meta property="og:title" content={pageTitle} />
        <meta property="og:description" content={pageDescription} />
        <meta property="og:image" content={pageUrl + pageImage} />
        <meta property="og:url" content={pageUrl} />
        <meta property="og:type" content="website" />

        {/* Twitter Card tags */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content={pageTitle} />
        <meta name="twitter:description" content={pageDescription} />
        <meta name="twitter:image" content={pageUrl + pageImage} />

        {/* Additional SEO tags */}
        <meta name="keywords" content="physical ai, humanoid robotics, ros2, isaac sim, vla, robotics course" />
        <link rel="canonical" href={pageUrl} />
      </Head>

      {/* Page content */}
      <HeroSection />
      <main>
        {/* ... other sections ... */}
      </main>
    </Layout>
  );
}
```

**OG Image Requirements**:
- Size: 1200x630px (Facebook/LinkedIn optimal)
- Format: JPEG or PNG
- File size: <1MB
- Content: Feature book title, tagline, key visual (robot)
- Location: `static/img/homepage/og-image.jpg`

**Additional SEO Checklist**:
- ✅ Unique, descriptive page title (<60 characters)
- ✅ Meta description (150-160 characters)
- ✅ OG image (1200x630px)
- ✅ Canonical URL
- ✅ Proper heading hierarchy (one h1, multiple h2s)
- ✅ Alt text for all images
- ✅ Fast page load (<2s)
- ✅ Mobile-friendly (responsive design)

### Alternatives Considered

1. **Docusaurus SEO plugin**: Third-party plugin
   - **Rejected**: Not needed; built-in Layout component sufficient for our needs

2. **Structured data (JSON-LD)**: Rich snippets
   - **Deferred**: Can be added later if needed for course schema; not critical for MVP

3. **Sitemap generation**: XML sitemap
   - **Already handled**: Docusaurus automatically generates sitemap.xml

---

## Summary of Decisions

| Research Item | Decision | Key Rationale |
|---------------|----------|---------------|
| **Responsive Design** | CSS Modules + Docusaurus breakpoints, mobile-first | Native Docusaurus approach; no additional dependencies |
| **Accessibility** | Semantic HTML + ARIA labels + keyboard nav | WCAG 2.1 AA compliance; Lighthouse score 95+ |
| **Hero Background** | CSS background-image, WebP + JPEG, image-set() | Optimal performance; <2s load time; retina support |
| **State Management** | Stateless components (no state) | Spec doesn't require interactivity; simplicity principle |
| **Icons/Images** | Lucide React + custom SVGs | Tree-shakeable; consistent style; robotics-themed customs |
| **SEO** | Docusaurus Layout + OG/Twitter tags | Built-in support; social sharing optimization |

---

## Implementation Readiness

**Status**: ✅ **ALL RESEARCH COMPLETE**

All technical unknowns from plan.md Phase 0 have been resolved. Ready to proceed to Phase 1: Design & Contracts.

**Next Steps**:
1. Generate data-model.md (define data structures)
2. Generate contracts/components.ts (TypeScript interfaces)
3. Generate quickstart.md (developer guide)
4. Update agent context (if applicable)
5. Proceed to `/sp.tasks` for task generation

---

**Research Completed**: 2025-12-05
**Reviewed By**: AI Agent (Phase 0)
**Approval Required**: Human review before proceeding to Phase 1
