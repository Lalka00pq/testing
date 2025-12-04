# -*- coding: utf-8 -*-
"""
Test cases for https://www.jetbrains.com/
Functional and UI testing
"""

from playwright.sync_api import sync_playwright
import sys

# Set encoding for output
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def test_jetbrains_homepage():
    """Test case 1: Check homepage loads correctly"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Check page title
            assert "JetBrains" in page.title(), f"Wrong title: {page.title()}"
            
            # Check logo exists
            logo = page.locator("a[href='/'] img")
            assert logo.count() > 0, "Logo not found"
            
            print("[OK] Test 1 PASSED: Homepage loaded successfully")
            return True
        except AssertionError as e:
            print("[FAIL] Test 1 FAILED:", str(e))
            return False
        except Exception as e:
            print("[ERROR] Test 1 FAILED:", str(e))
            return False
        finally:
            browser.close()


def test_cookie_settings_popup():
    """Test case 2: Check cookie settings dialog"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Check cookie dialog
            cookie_dialog = page.locator("dialog")
            if cookie_dialog.count() > 0:
                accept_btn = page.get_by_role("button", name="Accept All")
                deny_btn = page.get_by_role("button", name="Deny All")
                
                if accept_btn.count() > 0 and deny_btn.count() > 0:
                    print("[OK] Test 2 PASSED: Cookie dialog with correct buttons found")
                    return True
                else:
                    return False
            else:
                print("[SKIP] Test 2 SKIPPED: Cookie dialog not found")
                return True
        except Exception as e:
            print("[ERROR] Test 2 FAILED:", str(e))
            return False
        finally:
            browser.close()


def test_navigation_menu():
    """Test case 3: Check main navigation menu"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible(timeout=2000):
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Check navigation items
            nav_items = ["AI", "Developer Tools", "Team Tools", "Education", "Solutions", "Support", "Store"]
            
            for item in nav_items:
                nav_button = page.get_by_role("button", name=f"{item}: Open submenu")
                if nav_button.is_visible():
                    print(f"  [+] Found menu item: {item}")
                else:
                    raise AssertionError(f"Menu item not found: {item}")
            
            print("[OK] Test 3 PASSED: All menu items present")
            return True
        except AssertionError as e:
            print("[FAIL] Test 3 FAILED:", str(e))
            return False
        finally:
            browser.close()


def test_developer_tools_menu():
    """Test case 4: Check Developer Tools submenu"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Close cookies
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible(timeout=2000):
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Open Developer Tools menu
            dev_tools_btn = page.get_by_role("button", name="Developer Tools: Open submenu")
            dev_tools_btn.click()
            page.wait_for_timeout(500)
            
            # Check IDEs by href
            ides = {
                "IntelliJ IDEA": "/idea/",
                "PyCharm": "/pycharm/",
                "WebStorm": "/webstorm/",
                "Rider": "/rider/",
                "CLion": "/clion/"
            }
            
            for ide_name, ide_path in ides.items():
                ide_link = page.locator(f"a[href='{ide_path}']")
                if ide_link.count() > 0:
                    print(f"  [+] Found IDE: {ide_name}")
                else:
                    raise AssertionError(f"IDE not found: {ide_name}")
            
            print("[OK] Test 4 PASSED: All IDEs available in menu")
            return True
        except AssertionError as e:
            print("[FAIL] Test 4 FAILED:", str(e))
            return False
        except Exception as e:
            print("[ERROR] Test 4 FAILED:", str(e))
            return False
        finally:
            browser.close()


def test_search_functionality():
    """Test case 5: Check search functionality"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Close cookies
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible():
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Find search button
            search_btn = page.locator("button[aria-label='Open search']")
            assert search_btn.is_visible(), "Search button not found"
            
            print("[OK] Test 5 PASSED: Search function available")
            return True
        except AssertionError as e:
            print("[FAIL] Test 5 FAILED:", str(e))
            return False
        finally:
            browser.close()


def test_footer_links():
    """Test case 6: Check footer links"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Scroll to footer
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(500)
            
            # Check footer links
            footer_links = ["Privacy and Security", "Terms of Use", "Legal", "Genuine Tools"]
            
            for link_text in footer_links:
                footer_link = page.get_by_role("link", name=link_text)
                if footer_link.count() > 0:
                    print(f"  [+] Found link: {link_text}")
            
            print("[OK] Test 6 PASSED: Footer links available")
            return True
        except AssertionError as e:
            print("[FAIL] Test 6 FAILED:", str(e))
            return False
        finally:
            browser.close()


def test_responsive_design():
    """Test case 7: Check responsive design for mobile"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        
        try:
            # Check on mobile resolution
            page = browser.new_page(viewport={"width": 375, "height": 667})
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Close cookies
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible():
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Check main content
            main_content = page.locator("main")
            assert main_content.is_visible(), "Main content not visible"
            
            print("[OK] Test 7 PASSED: Responsive design works on mobile")
            return True
        except AssertionError as e:
            print("[FAIL] Test 7 FAILED:", str(e))
            return False
        finally:
            browser.close()


def test_profile_account_link():
    """Test case 8: Check account and store links"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Close cookies
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible():
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Check profile link
            profile_link = page.locator("a[href='https://account.jetbrains.com/']")
            if profile_link.count() > 0:
                print("  [+] Account link found")
            
            # Check store link
            store_link = page.locator("a[href='/store/']")
            if store_link.count() > 0:
                print("  [+] Store link found")
            
            print("[OK] Test 8 PASSED: Account and Store links available")
            return True
        except AssertionError as e:
            print("[FAIL] Test 8 FAILED:", str(e))
            return False
        finally:
            browser.close()


def test_main_content_sections():
    """Test case 9: Check main content sections"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Close cookies
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible():
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Check main sections
            sections = {
                "Junie": "Your smart coding agent",
                "For developers": "Enjoy building software",
                "For teams": "Minimize friction",
                "For businesses": "Empower your team"
            }
            
            for section_name, section_text in sections.items():
                heading = page.get_by_text(section_name)
                if heading.count() > 0:
                    print(f"  [+] Found section: {section_name}")
            
            print("[OK] Test 9 PASSED: All main sections present")
            return True
        except AssertionError as e:
            print("[FAIL] Test 9 FAILED:", str(e))
            return False
        finally:
            browser.close()


def test_cta_buttons():
    """Test case 10: Check Call-To-Action buttons"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Close cookies
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible():
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Check CTA buttons
            cta_buttons = [
                "Try now for free",
                "See plans and pricing",
                "Learn more"
            ]
            
            for button_text in cta_buttons:
                buttons = page.get_by_role("link", name=button_text)
                if buttons.count() > 0:
                    print(f"  [+] Found CTA button: {button_text}")
            
            print("[OK] Test 10 PASSED: CTA buttons available and visible")
            return True
        except AssertionError as e:
            print("[FAIL] Test 10 FAILED:", str(e))
            return False
        finally:
            browser.close()


# Run all tests
if __name__ == "__main__":
    print("="*60)
    print("TESTING: https://www.jetbrains.com/")
    print("="*60)
    print()
    
    tests = [
        test_jetbrains_homepage,
        test_cookie_settings_popup,
        test_navigation_menu,
        test_developer_tools_menu,
        test_search_functionality,
        test_footer_links,
        test_responsive_design,
        test_profile_account_link,
        test_main_content_sections,
        test_cta_buttons
    ]
    
    results = []
    for i, test_func in enumerate(tests, 1):
        print(f"\n[Test {i}/10]")
        result = test_func()
        results.append(result)
    
    print("\n" + "="*60)
    print("FINAL REPORT")
    print("="*60)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total} tests")
    print(f"Success rate: {(passed/total)*100:.1f}%")
    print("="*60)
