# Quickstart Guide: Physical AI Humanoid Robotics Landing Page

**Feature**: 001-ai-native-homepage
**Date**: 2025-12-05
**For**: Developers implementing or modifying the homepage

## Overview

This guide helps you get started with developing, modifying, and deploying the Physical AI Humanoid Robotics landing page. The homepage is built with Docusaurus 3.9.2, React 19, and TypeScript 5.6.

---

## Prerequisites

- **Node.js**: >= 20.0
- **npm**: >= 9.0 (comes with Node.js)
- **Git**: For version control
- **Code Editor**: VS Code recommended (with TypeScript extensions)

---

## Development Setup

### 1. Install Dependencies

```bash
# From repository root
npm install
```

This installs Docusaurus, React, TypeScript, and all required dependencies.

### 2. Start Development Server

```bash
npm run start
```

- **URL**: http://localhost:3000
- **Live Reload**: Enabled (changes reflect immediately)
- **Port**: 3000 (default, can be changed with `--port` flag)

```bash
# Use custom port
npm run start -- --port 3001
```

### 3. Build for Production

```bash
npm run build
```

- **Output Directory**: `/build`
- **Static Files**: Fully optimized HTML, CSS, JS
- **Deployment Ready**: Can be served from any static host

### 4. Serve Production Build Locally

```bash
npm run serve
```

- **URL**: http://localhost:3000
- **Purpose**: Test production build before deployment

---

## Project Structure

### Homepage-Specific Files

```
src/
├── components/
│   └── Homepage/                      # All homepage components
│       ├── HeroSection/
│       │   ├── index.tsx              # Hero component
│       │   ├── heroConfig.ts          # Hero content data
│       │   └── styles.module.css      # Hero styles
│       ├── RoboticsSpectrum/
│       │   ├── index.tsx              # Spectrum container
│       │   ├── SpectrumCard.tsx       # Individual card
│       │   ├── spectrumConfig.ts      # Spectrum data
│       │   └── styles.module.css
│       ├── BookDifferentiators/
│       │   ├── index.tsx
│       │   ├── DifferentiatorCard.tsx
│       │   ├── differentiatorsConfig.ts
│       │   └── styles.module.css
│       ├── MaturityLevels/
│       │   ├── index.tsx
│       │   ├── MaturityCard.tsx
│       │   ├── maturityConfig.ts
│       │   └── styles.module.css
│       └── TransformationSection/
│           ├── index.tsx
│           ├── transformationConfig.ts
│           └── styles.module.css
├── pages/
│   ├── index.tsx                      # Main homepage (imports all sections)
│   └── index.module.css               # Homepage layout styles
└── css/
    └── custom.css                     # Global styles (if needed)

static/
└── img/
    └── homepage/                      # Homepage images
        ├── hero-bg-*.webp/jpg         # Hero background (multiple sizes)
        ├── og-image.jpg               # Social sharing image
        └── icons/
            ├── spectrum-*.svg         # Spectrum card icons
            ├── differentiator-*.svg   # Differentiator icons
            └── maturity-*.svg         # Maturity level icons
```

---

## Common Development Tasks

### Task 1: Modify Homepage Content

**To change hero section text**:

1. Open `src/components/Homepage/HeroSection/heroConfig.ts`
2. Edit the `heroData` object:

```typescript
export const heroData: HeroSectionData = {
  title: "Your New Title",
  tagline: "Your new tagline or value proposition",
  ctaText: "Get Started",
  ctaLink: "/docs/intro",
  backgroundImage: "/img/homepage/hero-bg.jpg"
};
```

3. Save the file
4. Development server will auto-reload with changes

**To change card descriptions**:

- **Spectrum cards**: Edit `src/components/Homepage/RoboticsSpectrum/spectrumConfig.ts`
- **Differentiator cards**: Edit `src/components/Homepage/BookDifferentiators/differentiatorsConfig.ts`
- **Maturity levels**: Edit `src/components/Homepage/MaturityLevels/maturityConfig.ts`

### Task 2: Add/Remove Cards

**To add a differentiator card**:

1. Open `src/components/Homepage/BookDifferentiators/differentiatorsConfig.ts`
2. Add a new object to the `differentiatorCards` array:

```typescript
import { NewIcon } from 'lucide-react';

export const differentiatorCards: DifferentiatorCardData[] = [
  // ... existing cards
  {
    id: "new-feature",
    title: "New Feature",
    description: "Description of the new benefit...",
    icon: NewIcon,
    order: 5
  }
];
```

3. Import icon from Lucide React or use custom SVG
4. Save and view changes in browser

**To remove a card**: Simply delete its entry from the config array.

**Note**: Spectrum and maturity level cards have fixed counts per spec (3 and 6 respectively). Changing these counts requires spec review.

### Task 3: Change Colors and Styling

**Component-specific styling**:

1. Locate the component's `.module.css` file (e.g., `HeroSection/styles.module.css`)
2. Modify CSS classes:

```css
.hero {
  background-color: var(--ifm-color-primary);
  /* Change colors, spacing, etc. */
}
```

**Global color scheme**:

1. Edit `docusaurus.config.ts`
2. Modify CSS variables in `themeConfig.colorMode`:

```typescript
theme: {
  customCss: './src/css/custom.css',
}
```

3. Or edit `src/css/custom.css` directly:

```css
:root {
  --ifm-color-primary: #2e8555;
  --ifm-color-primary-dark: #29784c;
  /* ... more colors */
}
```

### Task 4: Replace Images

**Hero background image**:

1. Place optimized images in `static/img/homepage/`:
   - `hero-bg-400.webp` (mobile)
   - `hero-bg-800.webp` (tablet)
   - `hero-bg-1600.webp` (desktop)
   - `hero-bg-1600.jpg` (fallback)

2. Ensure images are referenced correctly in `HeroSection/styles.module.css`

**Image optimization tips**:
- Use WebP format for smaller file sizes
- Compress images (quality 80-85 for WebP, 75-80 for JPEG)
- Generate multiple sizes for responsive loading
- Tools: Squoosh (web), ImageOptim (Mac), Sharp (Node.js)

**Card icons**:

- Use Lucide React icons (import from `lucide-react`)
- Or place custom SVGs in `static/img/homepage/icons/`
- Reference in config files: `icon: MyIconComponent`

### Task 5: Update SEO Metadata

**Edit** `src/pages/index.tsx`:

```tsx
export default function Home() {
  const pageTitle = 'Your SEO Title';
  const pageDescription = 'Your meta description (150-160 chars)';
  const pageImage = '/img/homepage/og-image.jpg';

  return (
    <Layout title={pageTitle} description={pageDescription}>
      <Head>
        <meta property="og:title" content={pageTitle} />
        <meta property="og:description" content={pageDescription} />
        <meta property="og:image" content={pageImage} />
        {/* ... more meta tags */}
      </Head>
      {/* ... page content */}
    </Layout>
  );
}
```

**Create OG image**:
- Size: 1200x630px
- Format: JPEG or PNG
- Location: `static/img/homepage/og-image.jpg`
- Content: Book title, tagline, visual (robot)

---

## Testing

### Manual Testing Checklist

**Responsive Design**:
```bash
# Open in browser, use DevTools (F12)
# Test at these widths:
- 375px (mobile)
- 768px (tablet)
- 1024px (desktop)
- 1440px (large desktop)
```

**Accessibility**:
1. Keyboard navigation (Tab key through all interactive elements)
2. Screen reader testing (NVDA on Windows, VoiceOver on Mac)
3. Color contrast (use browser DevTools Lighthouse audit)

**Browser Compatibility**:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

### Automated Testing (Lighthouse)

```bash
# Install Lighthouse CLI
npm install -g @lighthouse-ci/cli

# Run production build
npm run build
npm run serve

# Run Lighthouse audit (in another terminal)
lhci autorun --collect.url=http://localhost:3000
```

**Target Scores**:
- Performance: ≥90
- Accessibility: ≥95
- Best Practices: ≥90
- SEO: ≥90

### Playwright E2E Tests (if implemented)

```bash
# Install Playwright
npx playwright install

# Run tests
npx playwright test

# Run tests in UI mode (interactive)
npx playwright test --ui
```

---

## Deployment

### Deploy to GitHub Pages

**Prerequisites**:
- GitHub repository set up
- `organizationName` and `projectName` configured in `docusaurus.config.ts`

**Deployment Steps**:

```bash
# Method 1: Automatic (via GH_TOKEN)
GIT_USER=<your-username> npm run deploy

# Method 2: Manual
npm run build
# Then deploy /build directory to GitHub Pages via settings
```

**Verify Deployment**:
- Visit `https://<your-username>.github.io/<project-name>/`
- Check all sections load correctly
- Test on mobile device

### Deploy to Other Hosts

**Netlify**:
1. Connect GitHub repository
2. Build command: `npm run build`
3. Publish directory: `build`

**Vercel**:
1. Connect GitHub repository
2. Framework Preset: Docusaurus
3. Auto-detects build settings

**Static Host (any)**:
1. Run `npm run build`
2. Upload contents of `/build` directory
3. Configure server to serve `index.html` for all routes

---

## Troubleshooting

### Issue: Port 3000 already in use

```bash
# Solution: Use a different port
npm run start -- --port 3001
```

### Issue: Changes not reflecting

```bash
# Solution: Clear Docusaurus cache
npm run clear
npm run start
```

### Issue: Build fails with TypeScript errors

```bash
# Solution: Check TypeScript compilation
npm run typecheck

# Fix errors in reported files
# Then rebuild
npm run build
```

### Issue: Images not loading

- Check image paths are correct (relative to `/static/`)
- Verify images exist in `static/img/homepage/`
- Check browser console for 404 errors
- Ensure filenames match exactly (case-sensitive on Linux/Mac)

### Issue: CSS not applying

- Verify CSS module import: `import styles from './styles.module.css'`
- Check className usage: `className={styles.myClass}`
- Ensure CSS class names are camelCase in TypeScript
- Check browser DevTools to see if styles are being applied

---

## Best Practices

### Component Development

1. **Keep components small and focused**: Each component should do one thing well
2. **Co-locate styles**: Keep `.module.css` files next to component files
3. **Use TypeScript interfaces**: Import from `contracts/components.ts`
4. **Make components reusable**: Use props for configuration

### Content Management

1. **Separate content from components**: Use config files (`*Config.ts`)
2. **Keep descriptions concise**: Follow character limits in data-model.md
3. **Maintain consistency**: Use similar tone across all card descriptions

### Performance

1. **Optimize images**: Compress and use WebP format
2. **Lazy load below fold**: Only hero section loads immediately
3. **Minimize dependencies**: Don't add unnecessary npm packages
4. **Monitor bundle size**: Keep JavaScript bundle under 300KB

### Accessibility

1. **Use semantic HTML**: `<section>`, `<article>`, `<h1>` through `<h6>`
2. **Add ARIA labels**: For landmark regions and screen readers
3. **Test keyboard navigation**: Ensure all interactive elements are accessible
4. **Check color contrast**: Use DevTools to verify WCAG AA compliance

---

## Getting Help

**Documentation**:
- [Docusaurus Docs](https://docusaurus.io/docs)
- [React Docs](https://react.dev)
- [TypeScript Docs](https://www.typescriptlang.org/docs/)

**Specification Files**:
- `specs/001-ai-native-homepage/spec.md` - Feature requirements
- `specs/001-ai-native-homepage/plan.md` - Implementation plan
- `specs/001-ai-native-homepage/data-model.md` - Data structures
- `specs/001-ai-native-homepage/contracts/components.ts` - TypeScript interfaces

**Issue Tracking**:
- Check project GitHub Issues for known problems
- Create new issue for bugs or feature requests

---

## Quick Reference Commands

```bash
# Development
npm install                 # Install dependencies
npm run start              # Start dev server
npm run typecheck          # Check TypeScript errors
npm run clear              # Clear Docusaurus cache

# Production
npm run build              # Build for production
npm run serve              # Serve production build locally
npm run deploy             # Deploy to GitHub Pages

# Testing
npx playwright test        # Run E2E tests
lhci autorun              # Run Lighthouse audit
```

---

**Last Updated**: 2025-12-05
**Maintained By**: Development Team
**Questions?**: Refer to spec.md or create a GitHub issue
