// specs/003-chapter-template-system/contracts/component-props.ts

import { ReactNode } from 'react';

/**
 * Props for the LearningGoals component.
 * This component displays a list of learning goals for the chapter.
 */
export interface LearningGoalsProps {
  /** The content of the component, expected to be a list of goals. */
  children: ReactNode;
}

/**
 * Props for the Prerequisites component.
 * This component displays a list of prerequisites for the chapter.
 */
export interface PrerequisitesProps {
  /** The content of the component, expected to be a list of prerequisites. */
  children: ReactNode;
}

/**
 * Props for the KeyTakeaways component.
 * This component displays a list of key takeaways or summary points.
 */
export interface KeyTakeawaysProps {
  /** The content of the component, expected to be a list of takeaways. */
  children: ReactNode;
}

/**
 * Represents a single hint within an exercise.
 */
export interface Hint {
  /** The content of the hint. */
  content: string;
  /** The title of the hint, displayed before it's revealed. */
  title: string;
}

/**
 * Props for the ExerciseBlock component.
 * This component provides an interactive exercise with progressively revealed hints.
 */
export interface ExerciseBlockProps {
  /** The main question or problem for the exercise. */
  question: string;
  /** An array of hints for the exercise. */
  hints: Hint[];
  /** The final solution or answer to the exercise. */
  solution: ReactNode;
}
