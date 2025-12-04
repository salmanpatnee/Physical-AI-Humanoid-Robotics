import React from 'react';
import type { PrerequisitesProps } from '../../../specs/003-chapter-template-system/contracts/component-props';
import styles from './styles.module.css';

export default function Prerequisites({ children }: PrerequisitesProps): JSX.Element {
  return (
    <div className={styles.prerequisites}>
      <h3 className={styles.title}>Prerequisites</h3>
      <div className={styles.content}>{children}</div>
    </div>
  );
}
