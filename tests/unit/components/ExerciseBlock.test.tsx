import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import ExerciseBlock from '../../../src/components/ExerciseBlock';

describe('ExerciseBlock Component', () => {
  const mockProps = {
    question: 'What is the capital of France?',
    hints: [
      { title: 'Hint 1', content: 'It is a major European city.' },
      { title: 'Hint 2', content: 'It is known for the Eiffel Tower.' },
    ],
    solution: <div>The answer is Paris.</div>,
  };

  test('renders the question correctly', () => {
    render(<ExerciseBlock {...mockProps} />);
    expect(screen.getByText('What is the capital of France?')).toBeInTheDocument();
  });

  test('renders all hints with correct titles', () => {
    render(<ExerciseBlock {...mockProps} />);
    expect(screen.getByText('Hint 1')).toBeInTheDocument();
    expect(screen.getByText('Hint 2')).toBeInTheDocument();
  });

  test('renders hint content', () => {
    render(<ExerciseBlock {...mockProps} />);
    expect(screen.getByText('It is a major European city.')).toBeInTheDocument();
    expect(screen.getByText('It is known for the Eiffel Tower.')).toBeInTheDocument();
  });

  test('renders the solution', () => {
    render(<ExerciseBlock {...mockProps} />);
    expect(screen.getByText('The answer is Paris.')).toBeInTheDocument();
  });

  test('renders hints section header', () => {
    render(<ExerciseBlock {...mockProps} />);
    expect(screen.getByText('Hints')).toBeInTheDocument();
  });

  test('renders solution section header', () => {
    render(<ExerciseBlock {...mockProps} />);
    expect(screen.getByText('Solution')).toBeInTheDocument();
  });

  test('uses semantic HTML details elements for accessibility', () => {
    const { container } = render(<ExerciseBlock {...mockProps} />);
    const detailsElements = container.querySelectorAll('details');
    // Should have one details element per hint plus one for the solution
    expect(detailsElements.length).toBe(mockProps.hints.length + 1);
  });

  test('handles empty hints array', () => {
    const propsWithNoHints = {
      ...mockProps,
      hints: [],
    };
    render(<ExerciseBlock {...propsWithNoHints} />);
    expect(screen.getByText('What is the capital of France?')).toBeInTheDocument();
    expect(screen.getByText('The answer is Paris.')).toBeInTheDocument();
  });
});
