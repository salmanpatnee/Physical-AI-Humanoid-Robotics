/**
 * Component Contracts: Physical AI Humanoid Robotics Landing Page
 *
 * Feature: 001-ai-native-homepage
 * Date: 2025-12-05
 *
 * This file defines TypeScript interfaces for all React components used in the
 * Physical AI Humanoid Robotics landing page. These contracts ensure type safety
 * and serve as documentation for component APIs.
 */

import type { ReactNode, ComponentType, SVGProps } from 'react';

// ============================================================================
// Data Entity Interfaces (from data-model.md)
// ============================================================================

/**
 * Hero section configuration data
 */
export interface HeroSectionData {
  /** Main heading text (max 60 characters) */
  title: string;

  /** Subtitle/value proposition (max 160 characters) */
  tagline: string;

  /** Call-to-action button text (max 20 characters) */
  ctaText: string;

  /** CTA button destination URL */
  ctaLink: string;

  /** Optional path to hero background image */
  backgroundImage?: string;
}

/**
 * Robotics development spectrum card data
 * Represents one of three paradigms (Traditional, AI-Enhanced, Physical AI)
 */
export interface SpectrumCardData {
  /** Unique identifier */
  id: string;

  /** Card heading (max 30 characters) */
  title: string;

  /** Paradigm explanation (100-200 characters recommended) */
  description: string;

  /** React SVG icon component */
  icon: ComponentType<SVGProps<SVGSVGElement>>;

  /** Display order (1, 2, or 3) */
  order: number;
}

/**
 * Book differentiator card data
 * Represents a unique benefit or feature of the book
 */
export interface DifferentiatorCardData {
  /** Unique identifier */
  id: string;

  /** Card heading (max 25 characters) */
  title: string;

  /** Benefit explanation (80-150 characters recommended) */
  description: string;

  /** React SVG icon component */
  icon: ComponentType<SVGProps<SVGSVGElement>>;

  /** Display order (positive integer) */
  order: number;
}

/**
 * Organizational robotics maturity level data
 * Represents one level from 0-5
 */
export interface MaturityLevelData {
  /** Maturity level (0, 1, 2, 3, 4, or 5) */
  level: number;

  /** Level name/category (max 30 characters) */
  title: string;

  /** Overview of this level (100-180 characters recommended) */
  description: string;

  /** Key capabilities at this level (3-5 items, each max 50 characters) */
  characteristics: string[];

  /** Optional level badge icon */
  icon?: ComponentType<SVGProps<SVGSVGElement>>;
}

/**
 * Transformation section content data
 */
export interface TransformationSectionData {
  /** Section title (max 50 characters) */
  heading: string;

  /** Section body content (JSX or string) */
  content: ReactNode;
}

// ============================================================================
// Component Props Interfaces
// ============================================================================

/**
 * HeroSection Component Props
 *
 * Renders the hero section with title, tagline, CTA button, and optional background.
 * This is the primary engagement point (P1 priority per spec).
 *
 * @example
 * ```tsx
 * <HeroSection
 *   title="Physical AI Humanoid Robotics"
 *   tagline="Master ROS2, Isaac Sim, VLA"
 *   ctaText="Get Started"
 *   ctaLink="/docs/intro"
 *   backgroundImage="/img/homepage/hero-bg.jpg"
 * />
 * ```
 */
export interface HeroSectionProps {
  /** Main heading text - displays prominently at top */
  title: string;

  /** Subtitle text - appears below title */
  tagline: string;

  /** Text for call-to-action button */
  ctaText: string;

  /** URL destination when CTA button is clicked */
  ctaLink: string;

  /** Optional path to background image (relative to /static/) */
  backgroundImage?: string;

  /** Optional CSS class name for custom styling */
  className?: string;
}

/**
 * SpectrumCard Component Props
 *
 * Renders a single card in the robotics development spectrum section.
 * Three cards total represent the evolution: Traditional → AI-Enhanced → Physical AI.
 *
 * @example
 * ```tsx
 * <SpectrumCard
 *   title="Physical AI Systems"
 *   description="Intelligent robots with embodied AI..."
 *   icon={BotIcon}
 *   order={3}
 * />
 * ```
 */
export interface SpectrumCardProps {
  /** Card title/heading */
  title: string;

  /** Description of this robotics paradigm */
  description: string;

  /** Icon component (from Lucide or custom SVG) */
  icon: ComponentType<SVGProps<SVGSVGElement>>;

  /** Display order (determines left-to-right position) */
  order: number;

  /** Optional CSS class name */
  className?: string;
}

/**
 * RoboticsSpectrum Component Props
 *
 * Container component that renders all three spectrum cards.
 * Handles layout, spacing, and responsive behavior.
 *
 * @example
 * ```tsx
 * <RoboticsSpectrum cards={spectrumCardsData} />
 * ```
 */
export interface RoboticsSpectrumProps {
  /** Array of spectrum card data (exactly 3 required per spec) */
  cards: SpectrumCardData[];

  /** Optional section heading override */
  heading?: string;

  /** Optional CSS class name */
  className?: string;
}

/**
 * DifferentiatorCard Component Props
 *
 * Renders a single card highlighting a book benefit/feature.
 * Minimum 4 cards required per spec (FR-007).
 *
 * @example
 * ```tsx
 * <DifferentiatorCard
 *   title="Hands-On Learning"
 *   description="Build real robots with practical exercises..."
 *   icon={WrenchIcon}
 * />
 * ```
 */
export interface DifferentiatorCardProps {
  /** Card title/heading */
  title: string;

  /** Description of this benefit */
  description: string;

  /** Icon component */
  icon: ComponentType<SVGProps<SVGSVGElement>>;

  /** Optional CSS class name */
  className?: string;
}

/**
 * BookDifferentiators Component Props
 *
 * Container component that renders all differentiator cards.
 * Handles grid layout and responsive behavior.
 *
 * @example
 * ```tsx
 * <BookDifferentiators cards={differentiatorCardsData} />
 * ```
 */
export interface BookDifferentiatorsProps {
  /** Array of differentiator card data (minimum 4 per spec) */
  cards: DifferentiatorCardData[];

  /** Optional section heading override */
  heading?: string;

  /** Optional CSS class name */
  className?: string;
}

/**
 * MaturityCard Component Props
 *
 * Renders a single maturity level card with level number, title, description,
 * and characteristics list. Six cards total (levels 0-5) per spec (FR-009).
 *
 * @example
 * ```tsx
 * <MaturityCard
 *   level={3}
 *   title="Systematic Integration"
 *   description="Robotics integrated into core workflows..."
 *   characteristics={["Cross-team collaboration", "Standardized processes"]}
 * />
 * ```
 */
export interface MaturityCardProps {
  /** Maturity level number (0-5) */
  level: number;

  /** Level title/name */
  title: string;

  /** Overview description of this level */
  description: string;

  /** List of key characteristics/capabilities */
  characteristics: string[];

  /** Optional level badge icon */
  icon?: ComponentType<SVGProps<SVGSVGElement>>;

  /** Optional CSS class name */
  className?: string;
}

/**
 * MaturityLevels Component Props
 *
 * Container component that renders all six maturity level cards (0-5).
 * Handles grid layout, progression visualization, and responsive behavior.
 *
 * @example
 * ```tsx
 * <MaturityLevels levels={maturityLevelsData} />
 * ```
 */
export interface MaturityLevelsProps {
  /** Array of maturity level data (exactly 6, levels 0-5 per spec) */
  levels: MaturityLevelData[];

  /** Optional section heading override */
  heading?: string;

  /** Optional CSS class name */
  className?: string;
}

/**
 * TransformationSection Component Props
 *
 * Renders the transformation journey content section explaining the evolution
 * from traditional robotics to physical AI systems. (P3 priority per spec)
 *
 * @example
 * ```tsx
 * <TransformationSection
 *   heading="From Traditional to Physical AI"
 *   content={<p>The robotics field is transforming...</p>}
 * />
 * ```
 */
export interface TransformationSectionProps {
  /** Section heading */
  heading: string;

  /** Section content (can be JSX, markdown, or string) */
  content: ReactNode;

  /** Optional CSS class name */
  className?: string;
}

// ============================================================================
// Utility Types
// ============================================================================

/**
 * Common props shared by all section container components
 */
export interface SectionCommonProps {
  /** Optional CSS class name for the section container */
  className?: string;

  /** Optional section ID for anchor links */
  id?: string;

  /** Optional ARIA label for accessibility */
  ariaLabel?: string;
}

/**
 * Common props shared by all card components
 */
export interface CardCommonProps {
  /** Optional CSS class name for the card */
  className?: string;

  /** Optional onClick handler for interactive cards (not used in MVP) */
  onClick?: () => void;
}

// ============================================================================
// Configuration Types
// ============================================================================

/**
 * Complete homepage configuration
 * Aggregates all section data for the landing page
 */
export interface HomepageConfig {
  hero: HeroSectionData;
  spectrum: SpectrumCardData[];
  differentiators: DifferentiatorCardData[];
  maturityLevels: MaturityLevelData[];
  transformation: TransformationSectionData;
}

// ============================================================================
// Type Guards (optional, for runtime validation)
// ============================================================================

/**
 * Type guard to check if an object is a valid HeroSectionData
 */
export function isHeroSectionData(obj: any): obj is HeroSectionData {
  return (
    typeof obj === 'object' &&
    typeof obj.title === 'string' &&
    typeof obj.tagline === 'string' &&
    typeof obj.ctaText === 'string' &&
    typeof obj.ctaLink === 'string' &&
    (obj.backgroundImage === undefined || typeof obj.backgroundImage === 'string')
  );
}

/**
 * Type guard to check if an object is a valid SpectrumCardData
 */
export function isSpectrumCardData(obj: any): obj is SpectrumCardData {
  return (
    typeof obj === 'object' &&
    typeof obj.id === 'string' &&
    typeof obj.title === 'string' &&
    typeof obj.description === 'string' &&
    typeof obj.icon === 'function' &&
    typeof obj.order === 'number' &&
    obj.order >= 1 &&
    obj.order <= 3
  );
}

/**
 * Type guard to check if an object is a valid MaturityLevelData
 */
export function isMaturityLevelData(obj: any): obj is MaturityLevelData {
  return (
    typeof obj === 'object' &&
    typeof obj.level === 'number' &&
    obj.level >= 0 &&
    obj.level <= 5 &&
    typeof obj.title === 'string' &&
    typeof obj.description === 'string' &&
    Array.isArray(obj.characteristics) &&
    obj.characteristics.every((c: any) => typeof c === 'string')
  );
}

// ============================================================================
// Exports
// ============================================================================

export type {
  // Re-export all interfaces for convenience
  ReactNode,
  ComponentType,
  SVGProps,
};
