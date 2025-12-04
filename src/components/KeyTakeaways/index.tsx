import React from 'react';
import type { KeyTakeawaysProps } from '../../../specs/003-chapter-template-system/contracts/component-props';
import styles from './styles.module.css';

export default function KeyTakeaways({ children }: KeyTakeawaysProps): JSX.Element {
  return (
    <div className={styles.keyTakeaways}>
      <h3 className={styles.title}>Key Takeaways</h3>
      <div className={styles.content}>{children}</div>
    </div>
  );
}
