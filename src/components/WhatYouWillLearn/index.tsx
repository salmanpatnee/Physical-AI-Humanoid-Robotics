import React from 'react';
import * as LucideIcons from 'lucide-react';
import styles from './styles.module.css';

interface LearningGoal {
  text: string;
  icon?: string;
  why_it_matters?: string;
}

interface WhatYouWillLearnProps {
  goals: LearningGoal[];
  displayStyle?: 'bullets' | 'cards' | 'numbered';
  colorTheme?: 'primary' | 'success' | 'info';
}

export default function WhatYouWillLearn({
  goals,
  displayStyle = 'bullets',
  colorTheme = 'primary',
}: WhatYouWillLearnProps): JSX.Element {
  const getIcon = (iconName?: string) => {
    if (!iconName) return null;
    const Icon = LucideIcons[iconName];
    return Icon ? <Icon className={styles.icon} size={24} /> : null;
  };

  return (
    <div className={`${styles.whatYouWillLearn} ${styles[colorTheme]}`}>
      <h3 className={styles.title}>What You Will Learn</h3>
      <div className={`${styles.goalsContainer} ${styles[displayStyle]}`}>
        {goals.map((goal, index) => (
          <div key={index} className={styles.goalItem}>
            {goal.icon && <div className={styles.iconContainer}>{getIcon(goal.icon)}</div>}
            <div className={styles.goalContent}>
              <p className={styles.goalText}>{goal.text}</p>
              {goal.why_it_matters && (
                <p className={styles.whyItMatters}>{goal.why_it_matters}</p>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
