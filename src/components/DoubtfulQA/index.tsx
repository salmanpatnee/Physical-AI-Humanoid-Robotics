import React, { useState } from 'react';
import { ChevronDown, ChevronRight } from 'lucide-react';
import styles from './styles.module.css';

interface ConfusionPoint {
  id: string;
  question: string;
  answer: string;
  category: 'terminology' | 'why-vs-how' | 'scope' | 'sim-vs-real' | 'abstract';
  misconception_addressed: string;
  follow_up_questions?: string[];
  visual_aid?: string;
}

interface DoubtfulQAProps {
  questions: ConfusionPoint[];
  allowExpand?: boolean;
  showCategory?: boolean;
}

const categoryLabels = {
  'terminology': 'Word Confusion',
  'why-vs-how': 'Why & How',
  'scope': "What's Included",
  'sim-vs-real': 'Simulation vs Reality',
  'abstract': 'Abstract Concepts'
};

export default function DoubtfulQA({
  questions,
  allowExpand = true,
  showCategory = false,
}: DoubtfulQAProps): JSX.Element {
  const [expandedIds, setExpandedIds] = useState<Set<string>>(
    allowExpand ? new Set() : new Set(questions.map(q => q.id))
  );

  const toggleExpand = (id: string) => {
    if (!allowExpand) return;

    const newExpandedIds = new Set(expandedIds);
    if (newExpandedIds.has(id)) {
      newExpandedIds.delete(id);
    } else {
      newExpandedIds.add(id);
    }
    setExpandedIds(newExpandedIds);
  };

  return (
    <div className={styles.doubtfulQA}>
      <h3 className={styles.title}>Doubtful Questions & Answers</h3>
      <p className={styles.subtitle}>
        Common questions students ask about this topic
      </p>
      <div className={styles.questionsContainer}>
        {questions.map((q) => {
          const isExpanded = expandedIds.has(q.id);

          return (
            <div key={q.id} className={styles.questionItem}>
              <div
                className={`${styles.questionHeader} ${allowExpand ? styles.clickable : ''}`}
                onClick={() => toggleExpand(q.id)}
              >
                {allowExpand && (
                  <div className={styles.expandIcon}>
                    {isExpanded ? <ChevronDown size={20} /> : <ChevronRight size={20} />}
                  </div>
                )}
                <div className={styles.questionContent}>
                  <div className={styles.questionText}>{q.question}</div>
                  {showCategory && (
                    <span className={`${styles.categoryBadge} ${styles[q.category]}`}>
                      {categoryLabels[q.category]}
                    </span>
                  )}
                </div>
              </div>

              {isExpanded && (
                <div className={styles.answerContent}>
                  <p className={styles.answer}>{q.answer}</p>

                  {q.visual_aid && (
                    <div className={styles.visualAid}>
                      <img src={q.visual_aid} alt="Visual explanation" />
                    </div>
                  )}

                  {q.follow_up_questions && q.follow_up_questions.length > 0 && (
                    <div className={styles.followUp}>
                      <p className={styles.followUpTitle}>Want to learn more?</p>
                      <ul className={styles.followUpList}>
                        {q.follow_up_questions.map((fq, index) => (
                          <li key={index}>{fq}</li>
                        ))}
                      </ul>
                    </div>
                  )}

                  <div className={styles.misconceptionNote}>
                    <strong>Common misconception:</strong> {q.misconception_addressed}
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
