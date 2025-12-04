import React from 'react';
import type { LearningGoalsProps } from '../../../specs/003-chapter-template-system/contracts/component-props';
import styles from './styles.module.css';

export default function LearningGoals({ children }: LearningGoalsProps): JSX.Element {
  return (
    <div className={styles.learningGoals}>
      <h3 className={styles.title}>Learning Goals</h3>
      <div className={styles.content}>{children}</div>
    </div>
  );
}
