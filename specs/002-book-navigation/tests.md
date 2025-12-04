# Manual Test Checklist: Book Navigation

**Feature**: Book Navigation
**Created**: 2025-12-04
**Related**: [spec.md](spec.md), [plan.md](plan.md)

## Test Environment Setup

Before testing:
1. Run `npm run start` to start the local development server
2. Open browser at `http://localhost:3000`
3. Navigate to any documentation page

## Navigation Sidebar Tests

### Visual Rendering

- [ ] Sidebar is visible on all documentation pages
- [ ] Sidebar appears on the left side of the page
- [ ] Sidebar has consistent styling with the rest of the site

### Structure and Content

- [ ] "Introduction" category is present and correctly labeled
- [ ] "Core Modules" category is present and correctly labeled
- [ ] "Applications" category is present and correctly labeled
- [ ] All categories appear in the correct order (Introduction → Core Modules → Applications)
- [ ] Each category can be expanded/collapsed
- [ ] All nested items are present within their respective categories

### Navigation Functionality

- [ ] Clicking "Introduction" index link navigates to the introduction overview page
- [ ] Clicking "What is Physical AI?" navigates to the correct page
- [ ] Clicking "Humanoid Robotics Overview" navigates to the correct page
- [ ] Clicking "Core Modules" index link navigates to the modules overview page
- [ ] Clicking "Perception" navigates to the correct page
- [ ] Clicking "Locomotion" navigates to the correct page
- [ ] Clicking "Manipulation" navigates to the correct page
- [ ] Clicking "Applications" index link navigates to the applications overview page
- [ ] Clicking "Industrial" navigates to the correct page
- [ ] Clicking "Healthcare" navigates to the correct page
- [ ] Clicking "Service Robotics" navigates to the correct page
- [ ] Clicking "intro" (top-level) navigates to the intro page

### Error Conditions

- [ ] No broken link errors in browser console
- [ ] No 404 pages when clicking sidebar links
- [ ] No missing page warnings in the terminal

### Build Process

- [ ] `npm run build` completes successfully without errors
- [ ] Build output confirms sidebar was processed correctly
- [ ] No sidebar configuration warnings or errors in build log

## Acceptance Criteria Verification

Verify against spec.md:

- [ ] **FR-001**: Sidebar displays on all documentation pages
- [ ] **FR-002**: Sidebar structure matches `sidebars.ts` configuration
- [ ] **FR-003**: Nested categories work correctly
- [ ] **FR-004**: All links point to valid documents in `docs/`
- [ ] **FR-005**: Order matches definition in `sidebars.ts`

- [ ] **SC-001**: Sidebar visible on 100% of documentation pages
- [ ] **SC-002**: Single-click navigation works for all sections
- [ ] **SC-003**: Build process completes without errors
- [ ] **SC-004**: Rendered structure matches configuration 1:1

## Test Results

**Tested By**: _______________
**Date**: _______________
**Build Version**: _______________
**Status**: [ ] PASS / [ ] FAIL

**Notes**:
