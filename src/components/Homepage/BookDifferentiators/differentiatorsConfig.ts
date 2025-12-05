import { Wrench, Zap, Building, Users } from 'lucide-react';
import type { DifferentiatorCardData } from '../types';

/**
 * Book Differentiators Configuration
 * Cards highlighting unique benefits and features of the book
 */
export const differentiatorCards: DifferentiatorCardData[] = [
  {
    id: 'hands-on',
    title: 'Hands-On Learning',
    description: 'Build real robots with practical exercises and simulations in Isaac Sim.',
    icon: Wrench,
    order: 1,
  },
  {
    id: 'cutting-edge',
    title: 'Cutting-Edge Content',
    description: 'Learn latest techniques: Vision-Language-Action models, imitation learning, and more.',
    icon: Zap,
    order: 2,
  },
  {
    id: 'industry-ready',
    title: 'Industry-Ready Skills',
    description: 'Master ROS2 and real-world robotics workflows used by leading companies.',
    icon: Building,
    order: 3,
  },
  {
    id: 'community',
    title: 'Community Support',
    description: 'Join a vibrant community of learners and practitioners building the future of robotics.',
    icon: Users,
    order: 4,
  },
];
