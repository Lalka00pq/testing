"""
Тест-кейсы для https://www.jetbrains.com/
Проверка функциональности и пользовательского интерфейса
"""

from playwright.sync_api import sync_playwright
import time
import sys

# Установка кодировки для вывода
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def test_jetbrains_homepage():
    """Тест-кейс 1: Проверка загрузки главной страницы"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        ## эээээээээээээээээээээ
        
        try:
            # Переход на главную страницу
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Проверка заголовка страницы
            assert "JetBrains" in page.title(), f"Неправильный заголовок: {page.title()}"
            
            # Проверка наличия логотипа
            logo = page.locator("a[href='/'] img")
            assert logo.count() > 0, "Логотип не найден"
            
            print("[OK] Тест 1 ПРОЙДЕН: Главная страница загружена успешно")
            return True
        except AssertionError as e:
            print("[FAIL] Тест 1 НЕ ПРОЙДЕН:", str(e))
            return False
        except Exception as e:
            print("[FAIL] Тест 1 НЕ ПРОЙДЕН (ошибка):", str(e))
            return False
        finally:
            browser.close()


def test_cookie_settings_popup():
    """Тест-кейс 2: Проверка всплывающего окна с куками"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Проверка наличия диалога с cookies
            cookie_dialog = page.locator("dialog")
            if cookie_dialog.count() > 0:
                # Проверка наличия кнопок
                accept_btn = page.get_by_role("button", name="Accept All")
                deny_btn = page.get_by_role("button", name="Deny All")
                manage_btn = page.get_by_role("button", name="Manage Settings")
                
                if accept_btn.count() > 0 and deny_btn.count() > 0:
                    print("[OK] Тест 2 ПРОЙДЕН: Диалог cookies присутствует с корректными кнопками")
                    return True
                else:
                    return False
            else:
                print("[SKIP] Тест 2 ПРОПУЩЕН: Диалог cookies отсутствует")
                return True
        except AssertionError as e:
            print("[FAIL] Тест 2 НЕ ПРОЙДЕН:", str(e))
            return False
        except Exception as e:
            print("[FAIL] Тест 2 НЕ ПРОЙДЕН (ошибка):", str(e))
            return False
        finally:
            browser.close()


def test_navigation_menu():
    """Тест-кейс 3: Проверка главного меню навигации"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Закрытие cookies если нужно
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible():
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Проверка наличия навигационных кнопок
            nav_items = ["AI", "Developer Tools", "Team Tools", "Education", "Solutions", "Support", "Store"]
            
            for item in nav_items:
                nav_button = page.get_by_role("button", name=f"{item}: Open submenu")
                if nav_button.is_visible():
                    print(f"  [+] Найден элемент: {item}")
                else:
                    raise AssertionError(f"Не найден элемент меню: {item}")
            
            print("[OK] Тест 3 ПРОЙДЕН: Все элементы меню присутствуют")
            return True
        except AssertionError as e:
            print("[FAIL] Тест 3 НЕ ПРОЙДЕН:", str(e))
            return False
        finally:
            browser.close()


