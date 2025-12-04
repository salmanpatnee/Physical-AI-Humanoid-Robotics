import React from 'react';
import type { ExerciseBlockProps } from '../../../specs/003-chapter-template-system/contracts/component-props';
import styles from './styles.module.css';

export default function ExerciseBlock({
  question,
  hints,
  solution,
}: ExerciseBlockProps): JSX.Element {
  return (
    <div className={styles.exerciseBlock}>
      <div className={styles.question}>
        <h4 className={styles.questionTitle}>Exercise</h4>
        <p className={styles.questionText}>{question}</p>
      </div>

      {hints && hints.length > 0 && (
        <div className={styles.hintsSection}>
          <h5 className={styles.sectionTitle}>Hints</h5>
          {hints.map((hint, index) => (
            <details key={index} className={styles.hint}>
              <summary className={styles.hintTitle}>{hint.title}</summary>
              <div className={styles.hintContent}>{hint.content}</div>
            </details>
          ))}
        </div>
      )}

      <div className={styles.solutionSection}>
        <details className={styles.solution}>
          <summary className={styles.solutionTitle}>Solution</summary>
          <div className={styles.solutionContent}>{solution}</div>
        </details>
      </div>
    </div>
  );
}
