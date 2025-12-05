import { Settings, Brain, Bot } from 'lucide-react';
import type { SpectrumCardData } from '../types';

/**
 * Robotics Development Spectrum Configuration
 * Three paradigm cards showing the evolution from Traditional to Physical AI
 */
export const spectrumCards: SpectrumCardData[] = [
  {
    id: 'traditional',
    title: 'Traditional Robotics',
    description: 'Pre-programmed systems with fixed, deterministic behaviors and limited adaptability.',
    icon: Settings,
    order: 1,
  },
  {
    id: 'ai-enhanced',
    title: 'AI-Enhanced Robotics',
    description: 'Traditional systems augmented with AI for specific tasks like vision or path planning.',
    icon: Brain,
    order: 2,
  },
  {
    id: 'physical-ai',
    title: 'Physical AI Systems',
    description: 'Intelligent robots with embodied AI, learning from interaction, and adapting to environments.',
    icon: Bot,
    order: 3,
  },
];
