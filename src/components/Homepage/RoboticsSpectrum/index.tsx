import React from 'react';
import type { RoboticsSpectrumProps } from '../types';
import SpectrumCard from './SpectrumCard';
import styles from './styles.module.css';

/**
 * RoboticsSpectrum Component
 *
 * Container component that renders all three robotics paradigm cards.
 * Shows the evolution: Traditional → AI-Enhanced → Physical AI
 */
export default function RoboticsSpectrum({
  cards,
  heading = 'The Robotics Development Spectrum',
  className,
}: RoboticsSpectrumProps): JSX.Element {
  // Sort cards by order to ensure correct left-to-right progression
  const sortedCards = [...cards].sort((a, b) => a.order - b.order);

  return (
    <section
      className={`${styles.spectrumSection} ${className || ''}`}
      aria-labelledby="spectrum-heading"
    >
      <h2 id="spectrum-heading" className={styles.spectrumHeading}>
        {heading}
      </h2>
      <ul className={styles.spectrumGrid} role="list">
        {sortedCards.map((card) => (
          <li key={card.id}>
            <SpectrumCard
              title={card.title}
              description={card.description}
              icon={card.icon}
              order={card.order}
            />
          </li>
        ))}
      </ul>
    </section>
  );
}
