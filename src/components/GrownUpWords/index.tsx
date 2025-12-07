import React, { useState } from 'react';
import { ChevronDown, ChevronUp, BookOpen } from 'lucide-react';
import styles from './styles.module.css';

interface TechnicalTermMapping {
  simple_term: string;
  technical_term: string;
  context_example: string;
  why_technical_term_exists?: string;
}

interface GrownUpWordsProps {
  terms: TechnicalTermMapping[];
  displayStyle?: 'table' | 'cards' | 'inline';
  expandable?: boolean;
}

export default function GrownUpWords({
  terms,
  displayStyle = 'table',
  expandable = false,
}: GrownUpWordsProps): JSX.Element {
  const [isExpanded, setIsExpanded] = useState(!expandable);

  const toggleExpand = () => {
    if (expandable) {
      setIsExpanded(!isExpanded);
    }
  };

  return (
    <div className={styles.grownUpWords}>
      <div
        className={`${styles.header} ${expandable ? styles.clickable : ''}`}
        onClick={toggleExpand}
      >
        <div className={styles.titleContainer}>
          <BookOpen className={styles.icon} size={24} />
          <h3 className={styles.title}>Grown-Up Words</h3>
        </div>
        <p className={styles.subtitle}>
          Technical terms you might hear engineers use
        </p>
        {expandable && (
          <div className={styles.expandIcon}>
            {isExpanded ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
          </div>
        )}
      </div>

      {isExpanded && (
        <div className={styles.content}>
          {displayStyle === 'table' && (
            <table className={styles.termsTable}>
              <thead>
                <tr>
                  <th>Simple Word/Phrase</th>
                  <th>Technical Term</th>
                  <th>When You'll Hear It</th>
                </tr>
              </thead>
              <tbody>
                {terms.map((term, index) => (
                  <tr key={index}>
                    <td className={styles.simpleTerm}>{term.simple_term}</td>
                    <td className={styles.technicalTerm}>{term.technical_term}</td>
                    <td className={styles.contextExample}>
                      {term.context_example}
                      {term.why_technical_term_exists && (
                        <div className={styles.why}>
                          <strong>Why this term?</strong> {term.why_technical_term_exists}
                        </div>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}

          {displayStyle === 'cards' && (
            <div className={styles.cardsContainer}>
              {terms.map((term, index) => (
                <div key={index} className={styles.termCard}>
                  <div className={styles.cardHeader}>
                    <div className={styles.simpleTerm}>{term.simple_term}</div>
                    <div className={styles.arrow}>→</div>
                    <div className={styles.technicalTerm}>{term.technical_term}</div>
                  </div>
                  <div className={styles.cardBody}>
                    <div className={styles.contextExample}>"{term.context_example}"</div>
                    {term.why_technical_term_exists && (
                      <div className={styles.why}>
                        <strong>Why this term?</strong> {term.why_technical_term_exists}
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}

          {displayStyle === 'inline' && (
            <div className={styles.inlineContainer}>
              {terms.map((term, index) => (
                <span key={index} className={styles.inlineTerm}>
                  <strong>{term.simple_term}</strong> = {term.technical_term}
                  {index < terms.length - 1 && ' • '}
                </span>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
