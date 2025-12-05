import React from 'react';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';

// Import homepage components
import HeroSection from '@site/src/components/Homepage/HeroSection';
import RoboticsSpectrum from '@site/src/components/Homepage/RoboticsSpectrum';
import BookDifferentiators from '@site/src/components/Homepage/BookDifferentiators';
import MaturityLevels from '@site/src/components/Homepage/MaturityLevels';
import TransformationSection from '@site/src/components/Homepage/TransformationSection';

// Import configuration data
import { heroData } from '@site/src/components/Homepage/HeroSection/heroConfig';
import { spectrumCards } from '@site/src/components/Homepage/RoboticsSpectrum/spectrumConfig';
import { differentiatorCards } from '@site/src/components/Homepage/BookDifferentiators/differentiatorsConfig';
import { maturityLevels } from '@site/src/components/Homepage/MaturityLevels/maturityConfig';
import { transformationData } from '@site/src/components/Homepage/TransformationSection/transformationConfig';

/**
 * Homepage Component
 *
 * Landing page for the Physical AI Humanoid Robotics book.
 * Features:
 * - Hero section with title, tagline, and CTA
 * - Robotics development spectrum (3 paradigm cards)
 * - Book differentiators (4 feature cards)
 * - Maturity levels (6 organizational stages)
 * - Transformation journey content
 */
export default function Home(): JSX.Element {
  // SEO metadata
  const pageTitle = 'Physical AI Humanoid Robotics | Master ROS2, Isaac Sim, VLA';
  const pageDescription =
    'Comprehensive course on Physical AI and Humanoid Robotics. Learn ROS2, Isaac Sim, Vision-Language-Action models, and build intelligent robotic systems from scratch.';
  const pageImage = '/img/homepage/og-image.jpg'; // TODO: Create OG image
  const pageUrl = 'https://your-domain.com/'; // TODO: Update with actual domain

  return (
    <Layout
      title={pageTitle}
      description={pageDescription}
    >
      <Head>
        {/* Open Graph tags for social sharing */}
        <meta property="og:title" content={pageTitle} />
        <meta property="og:description" content={pageDescription} />
        <meta property="og:image" content={pageUrl + pageImage} />
        <meta property="og:url" content={pageUrl} />
        <meta property="og:type" content="website" />

        {/* Twitter Card tags */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content={pageTitle} />
        <meta name="twitter:description" content={pageDescription} />
        <meta name="twitter:image" content={pageUrl + pageImage} />

        {/* Additional SEO tags */}
        <meta
          name="keywords"
          content="physical ai, humanoid robotics, ros2, isaac sim, vla, robotics course, embodied ai, vision-language-action"
        />
        <link rel="canonical" href={pageUrl} />
      </Head>

      {/* Hero Section */}
      <HeroSection
        title={heroData.title}
        tagline={heroData.tagline}
        ctaText={heroData.ctaText}
        ctaLink={heroData.ctaLink}
        backgroundImage={heroData.backgroundImage}
      />

      {/* Main Content */}
      <main>
        {/* Robotics Development Spectrum */}
        <RoboticsSpectrum cards={spectrumCards} />

        {/* Book Differentiators */}
        <BookDifferentiators cards={differentiatorCards} />

        {/* Maturity Levels */}
        <MaturityLevels levels={maturityLevels} />

        {/* Transformation Journey */}
        <TransformationSection
          heading={transformationData.heading}
          content={transformationData.content}
        />
      </main>
    </Layout>
  );
}
