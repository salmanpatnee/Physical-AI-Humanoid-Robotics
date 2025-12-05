# Feature Specification: Site Visual Refresh

**Feature Branch**: `011-site-visual-refresh`
**Created**: 2025-12-05
**Status**: Draft
**Input**: User description: "I want to change "My Site" text to short book name, remove github link from the header, remove Blog link, update /docs/intro link to /docs, in footer Add 4 modules links in place of get started and course content, improve the readability of the Learning Goals section, use the gray theme instead of green"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Visitor experiences updated branding and navigation (Priority: P1)

A site visitor should be able to browse the website and experience the updated branding, navigation, and color scheme. This provides a more consistent and professional user experience, and directs users to the most important content more efficiently.

**Why this priority**: This is the most critical user journey as it impacts every visitor to the site and defines the core look and feel.

**Independent Test**: Can be fully tested by navigating the main pages of the site (homepage, docs pages) and verifying the visual and navigational changes. This delivers immediate value by improving the site's usability and aesthetics.

**Acceptance Scenarios**:

1.  **Given** a user is on any page of the site, **When** they look at the header, **Then** the site title should be "Physical AI & Humanoid Robotics".
2.  **Given** a user is on any page of the site, **When** they look at the header, **Then** there should be no "Blog" or "GitHub" links.
3.  **Given** a user is on the homepage, **When** they click the main "Documentation" link/button, **Then** they should be navigated to `/docs`.
4.  **Given** a user is on any page of the site, **When** they look at the footer, **Then** they should see links to "Module 1", "Module 2", "Module 3", and "Module 4".
5.  **Given** a user is on any page of the site, **When** they view the page, **Then** the primary color scheme of the site should be gray.

### User Story 2 - Visitor can more easily read learning goals (Priority: P2)

A visitor reading a chapter's content should find the "Learning Goals" section clear and easy to read, without visual clutter.

**Why this priority**: Improves the educational effectiveness of the content.

**Independent Test**: Can be tested by navigating to any page that uses the "Learning Goals" component and assessing its readability.

**Acceptance Scenarios**:

1.  **Given** a user is on a page with a "Learning Goals" section, **When** they view the section, **Then** the text should have improved line spacing, font size, and/or color contrast to enhance readability.

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: The site title displayed in the header navigation bar MUST be changed from "My Site" to "Physical AI & Humanoid Robotics".
-   **FR-002**: The navigation link to the "Blog" section MUST be removed from the site's header.
-   **FR-003**: The navigation link to the external "GitHub" repository MUST be removed from the site's header.
-   **FR-004**: The primary documentation link in the header, which currently points to `/docs/intro`, MUST be updated to point to `/docs`.
-   **FR-005**: The footer links under the "Community" and "More" sections MUST be replaced with a "Modules" section containing links to the four course modules.
-   **FR-006**: The styling for the `<LearningGoals />` React component MUST be updated to improve its visual clarity and readability.
-   **FR-007**: The Docusaurus website's primary color in the theme configuration MUST be changed from the current green to a gray color.

### Assumptions

-   The "short book name" is "Physical AI & Humanoid Robotics".
-   The four module links in the footer should point to `/docs/module1-robotic-nervous-system`, `/docs/module2-the-digital-twin`, `/docs/module3-ai-robot-brain`, and `/docs/module4-vision-language-action`.
-   Improving "readability" for the Learning Goals section implies changes to CSS properties like `line-height`, `font-size`, `color`, or `padding`.
-   Changing the theme to "gray" means updating the `--ifm-color-primary` CSS variable in the Docusaurus configuration.

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: A visual inspection of the deployed website confirms that all specified text, link, and color changes in the header and footer are correctly implemented on 100% of pages.
-   **SC-002**: All existing end-to-end tests for site navigation and page rendering MUST pass after the changes are implemented.
-   **SC-003**: A user survey of the "Learning Goals" component indicates a 25% or greater improvement in "readability" scores compared to the original design.
-   **SC-004**: The Lighthouse accessibility score for pages containing the updated "Learning Goals" component MUST remain at 90 or above.