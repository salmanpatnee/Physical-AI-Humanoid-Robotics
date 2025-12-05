import React from 'react';
import type { SpectrumCardProps } from '../types';
import styles from './styles.module.css';

/**
 * SpectrumCard Component
 *
 * Renders a single card in the robotics development spectrum section.
 * Displays icon, title, and description for one paradigm.
 */
export default function SpectrumCard({
  title,
  description,
  icon: Icon,
  className,
}: SpectrumCardProps): JSX.Element {
  return (
    <article className={`${styles.spectrumCard} ${className || ''}`}>
      <div className={styles.iconContainer} aria-hidden="true">
        <Icon className={styles.icon} />
      </div>
      <h3 className={styles.cardTitle}>{title}</h3>
      <p className={styles.cardDescription}>{description}</p>
    </article>
  );
}
