import React from 'react';
import type { DifferentiatorCardProps } from '../types';
import styles from './styles.module.css';

/**
 * DifferentiatorCard Component
 *
 * Renders a single card highlighting a book benefit/feature.
 * Displays icon, title, and description.
 */
export default function DifferentiatorCard({
  title,
  description,
  icon: Icon,
  className,
}: DifferentiatorCardProps): JSX.Element {
  return (
    <article className={`${styles.differentiatorCard} ${className || ''}`}>
      <div className={styles.iconWrapper} aria-hidden="true">
        <Icon className={styles.cardIcon} />
      </div>
      <h3 className={styles.cardTitle}>{title}</h3>
      <p className={styles.cardDescription}>{description}</p>
    </article>
  );
}
