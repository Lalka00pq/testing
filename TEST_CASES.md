# Test Cases for JetBrains Website (https://www.jetbrains.com/)

## Overview
This document describes comprehensive test cases for testing the JetBrains official website. The tests cover functionality, UI elements, navigation, responsive design, and user interaction.

---

## Test Case 1: Homepage Loading Test
**ID:** TC-001  
**Title:** Verify homepage loads correctly  
**Priority:** Critical  
**Steps:**
1. Navigate to https://www.jetbrains.com/
2. Wait for page to load (networkidle)
3. Check page title contains "JetBrains"
4. Verify logo is present and visible

**Expected Result:**
- Page loads successfully
- Page title contains "JetBrains"
- Logo is visible on the page

**Test Status:** ✓ Automated

---

## Test Case 2: Cookie Settings Dialog
**ID:** TC-002  
**Title:** Verify cookie settings popup appears  
**Priority:** High  
**Steps:**
1. Navigate to https://www.jetbrains.com/
2. Check if cookie dialog is visible
3. Verify "Accept All" button is present
4. Verify "Deny All" button is present
5. Verify "Manage Settings" button is present

**Expected Result:**
- Cookie dialog appears on page load
- All three buttons (Accept All, Deny All, Manage Settings) are visible
- Dialog is properly styled

**Test Status:** ✓ Automated

---

## Test Case 3: Navigation Menu Verification
**ID:** TC-003  
**Title:** Check main navigation menu items  
**Priority:** High  
**Steps:**
1. Navigate to https://www.jetbrains.com/
2. Accept cookies
3. Verify navigation items are visible:
   - AI
   - Developer Tools
   - Team Tools
   - Education
   - Solutions
   - Support
   - Store

**Expected Result:**
- All menu items are visible and clickable
- Each menu item has correct label
- Menu items open submenus on hover/click

**Test Status:** ✓ Automated

---

## Test Case 4: Developer Tools Submenu
**ID:** TC-004  
**Title:** Verify Developer Tools submenu content  
**Priority:** High  
**Steps:**
1. Navigate to https://www.jetbrains.com/
2. Accept cookies
3. Click on "Developer Tools" menu
4. Verify the following IDEs are present:
   - IntelliJ IDEA
   - PyCharm
   - WebStorm
   - Rider
   - CLion

**Expected Result:**
- Developer Tools submenu opens
- All listed IDEs are visible in submenu
- Each IDE has a link to its product page

**Test Status:** ✓ Automated

---

## Test Case 5: Search Functionality
**ID:** TC-005  
**Title:** Check search feature availability  
**Priority:** Medium  
**Steps:**
1. Navigate to https://www.jetbrains.com/
2. Accept cookies
3. Locate search button in header
4. Verify search button is visible and clickable

**Expected Result:**
- Search button is visible in the header
- Search button is accessible and clickable
- Search button opens search interface

**Test Status:** ✓ Automated

---

## Test Case 6: Footer Links
**ID:** TC-006  
**Title:** Verify footer links are present  
**Priority:** Medium  
**Steps:**
1. Navigate to https://www.jetbrains.com/
2. Scroll to bottom of page
3. Verify the following links are visible:
   - Privacy and Security
   - Terms of Use
   - Legal
   - Genuine Tools

**Expected Result:**
- Footer is visible at bottom of page
- All specified links are present
- Links are clickable and have correct href attributes
- Social media icons are visible

**Test Status:** ✓ Automated

---

## Test Case 7: Responsive Design - Mobile
**ID:** TC-007  
**Title:** Check responsive design on mobile devices  
**Priority:** High  
**Viewport:** 375x667 (iPhone SE)  
**Steps:**
1. Set viewport to mobile size (375x667)
2. Navigate to https://www.jetbrains.com/
3. Accept cookies
4. Verify main content area is visible
5. Verify navigation adapts to mobile layout
6. Check that no horizontal scrolling is needed

**Expected Result:**
- Page loads correctly on mobile viewport
- Content is properly adjusted for mobile
- No layout issues or overflow
- Navigation menu is accessible (hamburger menu or similar)

**Test Status:** ✓ Automated

---

## Test Case 8: Account and Store Links
**ID:** TC-008  
**Title:** Verify account and store navigation links  
**Priority:** Medium  
**Steps:**
1. Navigate to https://www.jetbrains.com/
2. Accept cookies
3. Locate account profile link (should point to account.jetbrains.com)
4. Locate store link (should point to /store/)
5. Verify both links are clickable

**Expected Result:**
- Profile link with correct href is present
- Store link with correct href is present
- Links are visible in header/navigation area
- Links have appropriate icons or labels

**Test Status:** ✓ Automated

---

## Test Case 9: Main Content Sections
**ID:** TC-009  
**Title:** Verify main content sections are present  
**Priority:** High  
**Steps:**
1. Navigate to https://www.jetbrains.com/
2. Accept cookies
3. Verify the following main sections are visible:
   - Junie (AI coding agent)
   - For Developers section
   - For Teams section
   - For Businesses section
4. Scroll through page and verify content is properly displayed

**Expected Result:**
- All main sections are visible
- Each section contains relevant content and images
- Sections are properly spaced
- CTA buttons are present in each section

**Test Status:** ✓ Automated

---

## Test Case 10: Call-To-Action (CTA) Buttons
**ID:** TC-010  
**Title:** Verify CTA buttons are present and functional  
**Priority:** High  
**Steps:**
1. Navigate to https://www.jetbrains.com/
2. Accept cookies
3. Verify presence of CTA buttons:
   - "Try now for free"
   - "See plans and pricing"
   - "Learn more"
4. Verify buttons are clickable and styled correctly

**Expected Result:**
- All CTA buttons are visible
- Buttons have correct labels
- Buttons are clickable and navigate to correct pages
- Buttons have appropriate styling (color, size, hover effects)

**Test Status:** ✓ Automated

---

## Additional Test Cases (Manual Testing)

### TC-011: Performance Testing
- Load time should be less than 3 seconds
- Page should be interactive within 5 seconds
- No console errors during page load

### TC-012: Browser Compatibility
- Test on latest Chrome, Firefox, Safari, Edge
- Test on different OS (Windows, macOS, Linux)

### TC-013: Accessibility Testing
- Keyboard navigation works
- Screen reader compatibility
- Color contrast ratios meet WCAG standards
- Form labels are properly associated

### TC-014: Cross-browser Testing
- Test responsive behavior on Safari
- Test on Firefox
- Test on Microsoft Edge

---

## Test Execution Summary

| Test ID | Test Name | Status | Notes |
|---------|-----------|--------|-------|
| TC-001 | Homepage Loading | ✓ Pass | All elements loaded correctly |
| TC-002 | Cookie Dialog | ✓ Pass | Dialog appears with all buttons |
| TC-003 | Navigation Menu | ✓ Pass | All menu items visible |
| TC-004 | Developer Tools | ✓ Pass | All IDEs found in submenu |
| TC-005 | Search Function | ✓ Pass | Search button visible and accessible |
| TC-006 | Footer Links | ✓ Pass | All footer links present |
| TC-007 | Mobile Responsive | ✓ Pass | Works correctly on mobile viewport |
| TC-008 | Account/Store Links | ✓ Pass | Links present with correct URLs |
| TC-009 | Content Sections | ✓ Pass | All sections displayed correctly |
| TC-010 | CTA Buttons | ✓ Pass | Buttons visible and functional |

**Overall Success Rate:** 100%

---

## Test Environment
- **Browser:** Chromium (Playwright)
- **OS:** Windows 11
- **Test Framework:** Playwright (Python)
- **Test Execution Date:** December 4, 2025

---

## Conclusion
All automated test cases for the JetBrains website have passed successfully. The website displays correct functionality across different sections, menus, and responsive design. Further manual testing is recommended for edge cases and browser-specific issues.
