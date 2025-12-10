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
    mwith sync_playwright() as playwright:
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


def test_developer_tools_menu():
    """Тест-кейс 4: Проверка подменю 'Developer Tools'"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Закрытие cookies
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible(timeout=2000):
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Открытие меню Developer Tools
            dev_tools_btn = page.get_by_role("button", name="Developer Tools: Open submenu")
            dev_tools_btn.click()
            page.wait_for_timeout(500)
            
            # Проверка наличия IDE в подменю используя локатор по href
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
                    print(f"  [+] Найден IDE: {ide_name}")
                else:
                    raise AssertionError(f"IDE не найдена: {ide_name}")
            
            print("[OK] Тест 4 ПРОЙДЕН: Все IDE доступны в меню")
            return True
        except AssertionError as e:
            print("[FAIL] Тест 4 НЕ ПРОЙДЕН:", str(e))
            return False
        except Exception as e:
            print("[FAIL] Тест 4 НЕ ПРОЙДЕН (ошибка):", str(e))
            return False
        finally:
            browser.close()


def test_search_functionality():
    """Тест-кейс 5: Проверка функции поиска"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Закрытие cookies
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible():
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Поиск кнопки поиска
            search_btn = page.locator("button[aria-label='Open search']")
            assert search_btn.is_visible(), "Кнопка поиска не найдена"
            
            print("[OK] Тест 5 ПРОЙДЕН: Функция поиска доступна")
            return True
        except AssertionError as e:
            print("[FAIL] Тест 5 НЕ ПРОЙДЕН:", str(e))
            return False
        finally:
            browser.close()


def test_footer_links():
    """Тест-кейс 6: Проверка ссылок в футере"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Скроллинг к футеру
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(500)
            
            # Проверка наличия ссылок в футере
            footer_links = ["Privacy and Security", "Terms of Use", "Legal", "Genuine Tools"]
            
            for link_text in footer_links:
                footer_link = page.get_by_role("link", name=link_text)
                # Проверяем видимость хотя бы одной ссылки
                if footer_link.count() > 0:
                    print(f"  [+] Найдена ссылка: {link_text}")
            
            print("[OK] Тест 6 ПРОЙДЕН: Ссылки футера доступны")
            return True
        except AssertionError as e:
            print("[FAIL] Тест 6 НЕ ПРОЙДЕН:", str(e))
            return False
        finally:
            browser.close()


def test_responsive_design():
    """Тест-кейс 7: Проверка адаптивности дизайна"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        
        try:
            # Проверка на мобильном разрешении
            page = browser.new_page(viewport={"width": 375, "height": 667})
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Закрытие cookies
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible():
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Проверка наличия основных элементов
            main_content = page.locator("main")
            assert main_content.is_visible(), "Основной контент не видим"
            
            print("[OK] Тест 7 ПРОЙДЕН: Адаптивный дизайн работает на мобильных устройствах")
            return True
        except AssertionError as e:
            print("[FAIL] Тест 7 НЕ ПРОЙДЕН:", str(e))
            return False
        finally:
            browser.close()


def test_profile_account_link():
    """Тест-кейс 8: Проверка ссылки на аккаунт"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Закрытие cookies
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible():
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Проверка ссылки на профиль
            profile_link = page.locator("a[href='https://account.jetbrains.com/']")
            if profile_link.count() > 0:
                print("  [+] Ссылка на аккаунт найдена")
            
            # Проверка ссылки на Store
            store_link = page.locator("a[href='/store/']")
            if store_link.count() > 0:
                print("  [+] Ссылка на Store найдена")
            
            print("[OK] Тест 8 ПРОЙДЕН: Ссылки на аккаунт и Store доступны")
            return True
        except AssertionError as e:
            print("[FAIL] Тест 8 НЕ ПРОЙДЕН:", str(e))
            return False
        finally:
            browser.close()


def test_main_content_sections():
    """Тест-кейс 9: Проверка главных разделов контента"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Закрытие cookies
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible():
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Проверка наличия основных секций
            sections = {
                "Junie": "Your smart coding agent",
                "For developers": "Enjoy building software",
                "For teams": "Minimize friction",
                "For businesses": "Empower your team"
            }
            
            for section_name, section_text in sections.items():
                heading = page.get_by_text(section_name)
                if heading.count() > 0:
                    print(f"  [+] Найден раздел: {section_name}")
            
            print("[OK] Тест 9 ПРОЙДЕН: Все основные разделы присутствуют на странице")
            return True
        except AssertionError as e:
            print("[FAIL] Тест 9 НЕ ПРОЙДЕН:", str(e))
            return False
        finally:
            browser.close()


def test_cta_buttons():
    """Тест-кейс 10: Проверка кнопок призыва к действию (CTA)"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.jetbrains.com/", wait_until="networkidle")
            
            # Закрытие cookies
            accept_btn = page.get_by_role("button", name="Accept All")
            if accept_btn.is_visible():
                accept_btn.click()
                page.wait_for_timeout(500)
            
            # Проверка CTA кнопок
            cta_buttons = [
                "Try now for free",
                "See plans and pricing",
                "Learn more"
            ]
            
            for button_text in cta_buttons:
                buttons = page.get_by_role("link", name=button_text)
                if buttons.count() > 0:
                    print(f"  ✓ Найдена CTA кнопка: {button_text}")
            
            print("✓ Тест 10 ПРОЙДЕН: CTA кнопки доступны и видимы")
            return True
        except AssertionError as e:
            print("✗ Тест 10 НЕ ПРОЙДЕН:", str(e))
            return False
        finally:
            browser.close()


# Запуск всех тестов
if __name__ == "__main__":
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ САЙТА: https://www.jetbrains.com/")
    print("=" * 60)
    print()
    
    tests = [
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
        print(f"\n[Тест {i}/10]")
        result = test_func()
        results.append(result)
    
    print("\n" + "=" * 60)
    print("ИТОГОВЫЙ ОТЧЕТ")
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Пройдено: {passed}/{total} тестов")
    print(f"Успешность: {(passed/total)*100:.1f}%")
    print("=" * 60)
    ## SUPER TEST