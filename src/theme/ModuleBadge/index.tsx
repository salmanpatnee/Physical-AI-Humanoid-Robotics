import React from 'react';
import moduleColorMap from '../ModuleColorMap.json';
import styles from './styles.module.css';

interface ModuleBadgeProps {
  module: string;
  children?: React.ReactNode;
  size?: 'sm' | 'md' | 'lg';
}

const ModuleBadge: React.FC<ModuleBadgeProps> = ({
  module,
  children,
  size = 'md'
}) => {
  // Get the color from the module color map
  const backgroundColor = moduleColorMap[module as keyof typeof moduleColorMap] || 'var(--ifm-color-primary)';

  // Get the module label
  const label = children || `Module ${module.split('-')[1] || module}`;

  return (
    <span
      className={`${styles.moduleBadge} ${styles[size]}`}
      style={{ backgroundColor }}
    >
      {label}
    </span>
  );
};

export default ModuleBadge;
