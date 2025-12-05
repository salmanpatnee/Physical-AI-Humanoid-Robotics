import type { MaturityLevelData } from '../types';

/**
 * Maturity Levels Configuration
 * Six organizational robotics implementation maturity levels (0-5)
 */
export const maturityLevels: MaturityLevelData[] = [
  {
    level: 0,
    title: 'No Robotics',
    description: 'Organization has no robotics capabilities or automation beyond basic tools.',
    characteristics: [
      'Manual processes only',
      'No automation infrastructure',
      'Limited technical expertise',
    ],
  },
  {
    level: 1,
    title: 'Initial Exploration',
    description: 'First experiments with robotics or automation in isolated projects.',
    characteristics: [
      'Pilot projects underway',
      'Learning basic robotics concepts',
      'Limited organizational support',
    ],
  },
  {
    level: 2,
    title: 'Departmental Adoption',
    description: 'Individual departments use robotics for specific tasks, but no coordination.',
    characteristics: [
      'Department-specific solutions',
      'Some technical expertise',
      'Siloed implementations',
    ],
  },
  {
    level: 3,
    title: 'Systematic Integration',
    description: 'Robotics integrated into core workflows with standardized processes.',
    characteristics: [
      'Cross-team collaboration',
      'Standardized platforms (e.g., ROS2)',
      'Measurable ROI',
    ],
  },
  {
    level: 4,
    title: 'Advanced Optimization',
    description: 'AI-enhanced robotics systems with continuous learning and optimization.',
    characteristics: [
      'Machine learning integration',
      'Real-time adaptation',
      'Data-driven improvements',
    ],
  },
  {
    level: 5,
    title: 'Physical AI Leadership',
    description: 'Cutting-edge physical AI systems with humanoid robots and autonomous operation.',
    characteristics: [
      'Embodied AI deployed',
      'Humanoid robot workforce',
      'Industry innovation leader',
    ],
  },
];
