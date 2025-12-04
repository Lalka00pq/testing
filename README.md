# JetBrains Website Test Suite

Automated test suite for testing the JetBrains official website (https://www.jetbrains.com/)

## Overview

This repository contains comprehensive automated tests for the JetBrains website, covering:
- Homepage functionality
- Navigation menu items
- IDE availability in Developer Tools menu
- Search functionality
- Footer links
- Responsive design (mobile compatibility)
- Account and Store links
- Main content sections
- Call-to-Action buttons
- Cookie settings dialog

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate Virtual Environment

**On Windows:**
```bash
.\.venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install playwright
```

### 4. Install Browser

```bash
playwright install chromium
```

## Running Tests

### Run All Tests

```bash
python test_jetbrains.py
```

### Expected Output

```
============================================================
TESTING: https://www.jetbrains.com/
============================================================

[Test 1/10]
[OK] Test 1 PASSED: Homepage loaded successfully

[Test 2/10]
[SKIP] Test 2 SKIPPED: Cookie dialog not found

[Test 3/10]
  [+] Found menu item: AI
  [+] Found menu item: Developer Tools
  [+] Found menu item: Team Tools
  [+] Found menu item: Education
  [+] Found menu item: Solutions
  [+] Found menu item: Support
  [+] Found menu item: Store
[OK] Test 3 PASSED: All menu items present

...

============================================================
FINAL REPORT
============================================================
Passed: 10/10 tests
Success rate: 100.0%
============================================================
```

## Test Cases

### 1. Homepage Loading (TC-001)
Verifies that the JetBrains homepage loads correctly with proper title and logo.

### 2. Cookie Settings Dialog (TC-002)
Checks if the cookie consent dialog appears with appropriate buttons.

### 3. Navigation Menu (TC-003)
Verifies all main navigation menu items are present:
- AI
- Developer Tools
- Team Tools
- Education
- Solutions
- Support
- Store

### 4. Developer Tools Submenu (TC-004)
Checks that all major IDEs are listed in the Developer Tools menu:
- IntelliJ IDEA
- PyCharm
- WebStorm
- Rider
- CLion

### 5. Search Functionality (TC-005)
Verifies the search button is visible and accessible.

### 6. Footer Links (TC-006)
Checks for presence of important footer links:
- Privacy and Security
- Terms of Use
- Legal
- Genuine Tools

### 7. Responsive Design (TC-007)
Tests the website on mobile viewport (375x667).

### 8. Account and Store Links (TC-008)
Verifies links to account and store pages.

### 9. Main Content Sections (TC-009)
Checks that all main content sections are present:
- Junie (AI agent)
- For Developers
- For Teams
- For Businesses

### 10. Call-To-Action Buttons (TC-010)
Verifies CTA buttons are present and visible:
- Try now for free
- See plans and pricing
- Learn more

## Test Results

All tests execute with Chromium in headless mode, making the test suite suitable for CI/CD pipelines.

## File Structure

```
testing/
├── test_jetbrains.py      # Main test file with all test cases
├── TEST_CASES.md          # Detailed test case documentation
├── README.md              # This file
├── .venv/                 # Virtual environment
└── pyproject.toml         # Project configuration
```

## Troubleshooting

### Playwright Not Found
```bash
pip install playwright
playwright install chromium
```

### Encoding Issues
Tests are configured to use UTF-8 encoding. If you encounter encoding errors:
```python
# Ensure your Python file has UTF-8 encoding declaration
# -*- coding: utf-8 -*-
```

### Browser Not Found
If Chromium is not found, reinstall:
```bash
playwright install --with-deps chromium
```

### Tests Timing Out
Increase timeout in test files by modifying `wait_until="networkidle"` to `wait_until="networkidle2"` or increase `page.wait_for_timeout()` values.

## Continuous Integration

To integrate these tests into CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Install dependencies
  run: |
    pip install playwright
    playwright install chromium

- name: Run tests
  run: python test_jetbrains.py
```

## Contributing

When adding new tests:
1. Follow the existing test structure
2. Add comprehensive docstrings
3. Include appropriate error handling
4. Update TEST_CASES.md with new test details
5. Ensure tests are headless for CI/CD compatibility

## License

This test suite is provided as-is for testing purposes.

## Contact

For questions about these tests or the JetBrains website, please refer to official documentation at https://www.jetbrains.com/

---

**Last Updated:** December 4, 2025  
**Test Framework:** Playwright (Python)  
**Website Tested:** https://www.jetbrains.com/
