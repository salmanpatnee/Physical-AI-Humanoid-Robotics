import React from 'react';
import type { MaturityLevelsProps } from '../types';
import MaturityCard from './MaturityCard';
import styles from './styles.module.css';

/**
 * MaturityLevels Component
 *
 * Container component that renders all six maturity level cards (0-5).
 * Shows organizational robotics implementation progression.
 */
export default function MaturityLevels({
  levels,
  heading = 'Robotics Implementation Maturity Levels',
  className,
}: MaturityLevelsProps): JSX.Element {
  // Sort levels by level number (0-5) to ensure correct order
  const sortedLevels = [...levels].sort((a, b) => a.level - b.level);

  return (
    <section
      className={`${styles.maturitySection} ${className || ''}`}
      aria-labelledby="maturity-heading"
    >
      <h2 id="maturity-heading" className={styles.maturityHeading}>
        {heading}
      </h2>
      <ul className={styles.maturityGrid} role="list">
        {sortedLevels.map((levelData) => (
          <li key={levelData.level}>
            <MaturityCard
              level={levelData.level}
              title={levelData.title}
              description={levelData.description}
              characteristics={levelData.characteristics}
              icon={levelData.icon}
            />
          </li>
        ))}
      </ul>
    </section>
  );
}
