import React from 'react';
import type { MaturityCardProps } from '../types';
import styles from './styles.module.css';

/**
 * MaturityCard Component
 *
 * Renders a single maturity level card with level badge, title, description,
 * and characteristics list.
 */
export default function MaturityCard({
  level,
  title,
  description,
  characteristics,
  className,
}: MaturityCardProps): JSX.Element {
  return (
    <article className={`${styles.maturityCard} ${className || ''}`}>
      <div className={styles.levelBadge} aria-label={`Level ${level}`}>
        {level}
      </div>
      <h3 className={styles.cardTitle}>{title}</h3>
      <p className={styles.cardDescription}>{description}</p>
      <ul className={styles.characteristicsList}>
        {characteristics.map((characteristic, index) => (
          <li key={index} className={styles.characteristicItem}>
            {characteristic}
          </li>
        ))}
      </ul>
    </article>
  );
}
