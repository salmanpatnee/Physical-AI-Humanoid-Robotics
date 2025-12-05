import React from 'react';
import type { TransformationSectionProps } from '../types';
import styles from './styles.module.css';

/**
 * TransformationSection Component
 *
 * Renders the transformation journey content explaining the evolution
 * from traditional robotics to physical AI systems.
 */
export default function TransformationSection({
  heading,
  content,
  className,
}: TransformationSectionProps): JSX.Element {
  return (
    <section
      className={`${styles.transformationSection} ${className || ''}`}
      aria-labelledby="transformation-heading"
    >
      <div className={styles.container}>
        <h2 id="transformation-heading" className={styles.transformationHeading}>
          {heading}
        </h2>
        <div className={styles.content}>{content}</div>
      </div>
    </section>
  );
}
