import React from 'react';
import type { BookDifferentiatorsProps } from '../types';
import DifferentiatorCard from './DifferentiatorCard';
import styles from './styles.module.css';

/**
 * BookDifferentiators Component
 *
 * Container component that renders all differentiator cards.
 * Shows unique benefits and features of the book.
 */
export default function BookDifferentiators({
  cards,
  heading = 'What Makes This Book Different',
  className,
}: BookDifferentiatorsProps): JSX.Element {
  // Sort cards by order for consistent display
  const sortedCards = [...cards].sort((a, b) => a.order - b.order);

  return (
    <section
      className={`${styles.differentiatorsSection} ${className || ''}`}
      aria-labelledby="differentiators-heading"
    >
      <h2 id="differentiators-heading" className={styles.differentiatorsHeading}>
        {heading}
      </h2>
      <ul className={styles.differentiatorsGrid} role="list">
        {sortedCards.map((card) => (
          <li key={card.id}>
            <DifferentiatorCard
              title={card.title}
              description={card.description}
              icon={card.icon}
            />
          </li>
        ))}
      </ul>
    </section>
  );
}
