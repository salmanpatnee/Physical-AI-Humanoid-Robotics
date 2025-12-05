import React from 'react';
import Link from '@docusaurus/Link';
import type { HeroSectionProps } from '../types';
import styles from './styles.module.css';

/**
 * HeroSection Component
 *
 * Displays the main hero section with title, tagline, and call-to-action button.
 * This is the primary engagement point (P1 priority).
 *
 * @param props - HeroSectionProps with title, tagline, ctaText, ctaLink, and optional backgroundImage
 */
export default function HeroSection({
  title,
  tagline,
  ctaText,
  ctaLink,
  backgroundImage,
  className,
}: HeroSectionProps): JSX.Element {
  const heroStyle: React.CSSProperties = backgroundImage
    ? { backgroundImage: `url(${backgroundImage})` }
    : {};

  return (
    <section
      className={`${styles.hero} ${className || ''}`}
      style={heroStyle}
      aria-labelledby="hero-title"
    >
      <div className={styles.heroContent}>
        <h1 id="hero-title" className={styles.heroTitle}>
          {title}
        </h1>
        <p className={styles.heroTagline}>{tagline}</p>
        <Link
          className={styles.heroCta}
          to={ctaLink}
          aria-label={`${ctaText} - Navigate to introduction`}
        >
          {ctaText}
        </Link>
      </div>
    </section>
  );
}
