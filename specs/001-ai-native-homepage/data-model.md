# Data Model: Physical AI Humanoid Robotics Landing Page

**Feature**: 001-ai-native-homepage
**Date**: 2025-12-05
**Status**: ✅ Complete

## Purpose

This document defines the data structures and entities used in the Physical AI Humanoid Robotics landing page. All entities represent static, configuration-based data (no database/API required).

---

## Entity Definitions

### 1. HeroSectionData

**Purpose**: Configuration data for the hero section (primary landing area)

**Fields**:
| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `title` | `string` | ✅ | Main heading text | "Physical AI Humanoid Robotics" |
| `tagline` | `string` | ✅ | Subtitle/value proposition | "Master ROS2, Isaac Sim, VLA — Build Intelligent Robotic Systems" |
| `ctaText` | `string` | ✅ | Call-to-action button text | "Get Started" |
| `ctaLink` | `string` | ✅ | CTA button destination URL | "/docs/intro" |
| `backgroundImage` | `string` | ❌ | Path to hero background image | "/img/homepage/hero-bg.jpg" |

**Validation Rules**:
- `title`: Max 60 characters (SEO best practice)
- `tagline`: Max 160 characters (meta description length)
- `ctaText`: Max 20 characters (button UX)
- `ctaLink`: Must be valid relative or absolute URL
- `backgroundImage`: Must point to existing static asset

**Example**:
```typescript
const heroData: HeroSectionData = {
  title: "Physical AI Humanoid Robotics",
  tagline: "Master ROS2, Isaac Sim, VLA — Build Intelligent Robotic Systems from Scratch",
  ctaText: "Get Started",
  ctaLink: "/docs/intro",
  backgroundImage: "/img/homepage/hero-bg.jpg"
};
```

---

### 2. SpectrumCardData

**Purpose**: Represents one of three robotics development paradigms in the spectrum section

**Fields**:
| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | `string` | ✅ | Unique identifier | "traditional" |
| `title` | `string` | ✅ | Card heading | "Traditional Robotics" |
| `description` | `string` | ✅ | Explanation of this paradigm | "Pre-programmed systems with fixed behaviors..." |
| `icon` | `ComponentType<SVGProps>` | ✅ | React SVG icon component | `SettingsIcon` |
| `order` | `number` | ✅ | Display order (1, 2, 3) | 1 |

**Validation Rules**:
- `id`: Must be unique within spectrum cards
- `title`: Max 30 characters
- `description`: 100-200 characters recommended
- `order`: Must be 1, 2, or 3 (exactly 3 cards required per spec)

**Example**:
```typescript
const spectrumCards: SpectrumCardData[] = [
  {
    id: "traditional",
    title: "Traditional Robotics",
    description: "Pre-programmed systems with fixed, deterministic behaviors and limited adaptability.",
    icon: SettingsIcon,
    order: 1
  },
  {
    id: "ai-enhanced",
    title: "AI-Enhanced Robotics",
    description: "Traditional systems augmented with AI for specific tasks like vision or path planning.",
    icon: BrainIcon,
    order: 2
  },
  {
    id: "physical-ai",
    title: "Physical AI Systems",
    description: "Intelligent robots with embodied AI, learning from interaction, and adapting to environments.",
    icon: BotIcon,
    order: 3
  }
];
```

---

### 3. DifferentiatorCardData

**Purpose**: Represents a unique benefit or feature of the book (differentiator section)

**Fields**:
| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | `string` | ✅ | Unique identifier | "hands-on" |
| `title` | `string` | ✅ | Card heading | "Hands-On Learning" |
| `description` | `string` | ✅ | Benefit explanation | "Build real robots with practical exercises..." |
| `icon` | `ComponentType<SVGProps>` | ✅ | React SVG icon component | `WrenchIcon` |
| `order` | `number` | ✅ | Display order | 1 |

**Validation Rules**:
- `id`: Must be unique within differentiator cards
- `title`: Max 25 characters
- `description`: 80-150 characters recommended
- `order`: Positive integer (minimum 4 cards per spec)

**Example**:
```typescript
const differentiatorCards: DifferentiatorCardData[] = [
  {
    id: "hands-on",
    title: "Hands-On Learning",
    description: "Build real robots with practical exercises and simulations in Isaac Sim.",
    icon: WrenchIcon,
    order: 1
  },
  {
    id: "cutting-edge",
    title: "Cutting-Edge Content",
    description: "Learn latest techniques: Vision-Language-Action models, imitation learning, and more.",
    icon: ZapIcon,
    order: 2
  },
  {
    id: "industry-ready",
    title: "Industry-Ready Skills",
    description: "Master ROS2 and real-world robotics workflows used by leading companies.",
    icon: BuildingIcon,
    order: 3
  },
  {
    id: "community",
    title: "Community Support",
    description: "Join a vibrant community of learners and practitioners building the future of robotics.",
    icon: UsersIcon,
    order: 4
  }
];
```

---

### 4. MaturityLevelData

**Purpose**: Represents one organizational robotics implementation maturity level (0-5)

**Fields**:
| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `level` | `number` | ✅ | Maturity level (0-5) | 3 |
| `title` | `string` | ✅ | Level name/category | "Systematic Integration" |
| `description` | `string` | ✅ | Overview of this level | "Robotics integrated into core workflows..." |
| `characteristics` | `string[]` | ✅ | Key capabilities at this level | ["Cross-team collaboration", "Standardized processes"] |
| `icon` | `ComponentType<SVGProps>` | ❌ | Optional level badge icon | `TrendingUpIcon` |

**Validation Rules**:
- `level`: Must be 0, 1, 2, 3, 4, or 5 (exactly 6 cards per spec)
- `title`: Max 30 characters
- `description`: 100-180 characters recommended
- `characteristics`: 3-5 items, each max 50 characters

**Example**:
```typescript
const maturityLevels: MaturityLevelData[] = [
  {
    level: 0,
    title: "No Robotics",
    description: "Organization has no robotics capabilities or automation beyond basic tools.",
    characteristics: [
      "Manual processes only",
      "No automation infrastructure",
      "Limited technical expertise"
    ]
  },
  {
    level: 1,
    title: "Initial Exploration",
    description: "First experiments with robotics or automation in isolated projects.",
    characteristics: [
      "Pilot projects underway",
      "Learning basic robotics concepts",
      "Limited organizational support"
    ]
  },
  {
    level: 2,
    title: "Departmental Adoption",
    description: "Individual departments use robotics for specific tasks, but no coordination.",
    characteristics: [
      "Department-specific solutions",
      "Some technical expertise",
      "Siloed implementations"
    ]
  },
  {
    level: 3,
    title: "Systematic Integration",
    description: "Robotics integrated into core workflows with standardized processes.",
    characteristics: [
      "Cross-team collaboration",
      "Standardized platforms (e.g., ROS2)",
      "Measurable ROI"
    ]
  },
  {
    level: 4,
    title: "Advanced Optimization",
    description: "AI-enhanced robotics systems with continuous learning and optimization.",
    characteristics: [
      "Machine learning integration",
      "Real-time adaptation",
      "Data-driven improvements"
    ]
  },
  {
    level: 5,
    title: "Physical AI Leadership",
    description: "Cutting-edge physical AI systems with humanoid robots and autonomous operation.",
    characteristics: [
      "Embodied AI deployed",
      "Humanoid robot workforce",
      "Industry innovation leader"
    ]
  }
];
```

---

### 5. TransformationSectionData

**Purpose**: Configuration for the transformation journey content section

**Fields**:
| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `heading` | `string` | ✅ | Section title | "From Traditional to Physical AI" |
| `content` | `ReactNode` | ✅ | Section body (JSX/markdown) | `<p>Learn how...</p>` |

**Validation Rules**:
- `heading`: Max 50 characters
- `content`: Can be string, JSX elements, or markdown (rendered via MDX if needed)

**Example**:
```typescript
const transformationData: TransformationSectionData = {
  heading: "From Traditional Robotics to Physical AI",
  content: (
    <>
      <p>
        The robotics field is undergoing a fundamental transformation. Traditional pre-programmed
        systems are giving way to intelligent, adaptive robots powered by physical AI.
      </p>
      <p>
        This course guides you through this evolution, teaching you to build next-generation
        robotic systems that learn, adapt, and interact intelligently with their environment.
      </p>
    </>
  )
};
```

---

## Data Relationships

```
HomePage
├── HeroSectionData (1)
├── SpectrumCardData[] (exactly 3)
├── DifferentiatorCardData[] (4+, no max)
├── MaturityLevelData[] (exactly 6, levels 0-5)
└── TransformationSectionData (1)
```

**Cardinality**:
- **Hero**: Exactly 1
- **Spectrum**: Exactly 3 cards (per spec requirement FR-005)
- **Differentiators**: Minimum 4 cards (per spec requirement FR-007)
- **Maturity Levels**: Exactly 6 cards, levels 0-5 (per spec requirement FR-009)
- **Transformation**: Exactly 1 section

---

## Data Storage & Configuration

**Location**: All data is defined in TypeScript as static configuration within component files.

**No Database Required**: This is a static site; all content is configured at build time.

**Content Files**:
```
src/components/Homepage/
├── HeroSection/
│   └── heroConfig.ts          # HeroSectionData
├── RoboticsSpectrum/
│   └── spectrumConfig.ts      # SpectrumCardData[]
├── BookDifferentiators/
│   └── differentiatorsConfig.ts  # DifferentiatorCardData[]
├── MaturityLevels/
│   └── maturityConfig.ts      # MaturityLevelData[]
└── TransformationSection/
    └── transformationConfig.ts   # TransformationSectionData
```

**Editing Content**: To update page content, edit the respective config files and rebuild the site.

---

## Accessibility Considerations

**Alt Text Strategy**:
- Icons: Mark as `aria-hidden="true"` (decorative only, meaning conveyed by text)
- Background images: Not visible to screen readers (text overlay provides content)

**Content Guidelines**:
- All text fields must be plain text (no HTML entities in content, use Unicode)
- Card descriptions should be self-contained (understandable without context)
- Characteristics arrays should be ordered logically (not dependent on visual layout)

---

## Validation & Type Safety

**TypeScript Interfaces**: See `contracts/components.ts` for full interface definitions.

**Runtime Validation** (optional, not required for MVP):
- Can add Zod schemas for config validation
- Helpful if content is provided by external source (CMS)
- Not needed for hardcoded config files

---

## Future Extensibility

**Potential Enhancements** (not in current spec):
1. **Multi-language Support**: Add `locale` field to all entities
2. **CMS Integration**: Replace static config with API/CMS data fetching
3. **A/B Testing**: Add `variant` field for different content versions
4. **Analytics Tracking**: Add `trackingId` fields for event tracking

**Current Scope**: Static, single-language, hardcoded configuration (per spec requirements).

---

**Data Model Status**: ✅ **COMPLETE AND VALIDATED**
**Ready For**: Contract generation (TypeScript interfaces in `contracts/components.ts`)
