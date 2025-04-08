import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог
import allure
from pages.page_personal_account import Account
from pages.page_base_functions import BaseFunctions
from URLs import *


class TestAccount:
    @allure.step("Проверка перехода по клику на Личный кабинет")
    def test_switch_to_lk(self, driver):
        account = Account(driver)
        account.click_on_lk_button()
        current_url = account.authorization_page()
        assert 'login' in current_url

    @allure.step("Проверка перехода в раздел История заказов")
    def test_switch_to_order_history(self, driver):
        account = Account(driver)
        base_functions = BaseFunctions(driver)
        account.click_on_lk_button()
        account.wait_url_to_be(f'{URLs.BASE_URL}{URLs.LOGIN_PAGE}')
        account.fill_auth_fields()
        account.click_login_button()
        account.wait_url_to_be(URLs.BASE_URL)
        account.click_on_lk_button()
        account.check_account_page()
        account.click_history_button(driver)
        base_functions.close_overlay()
        current_url = account.open_orders_history()
        assert current_url == f'{URLs.BASE_URL}{URLs.ORDER_HISTORY_PAGE}'

    @allure.step("Проверка выхода из аккаунта")
    def test_logout(self, driver):
        account = Account(driver)
        account.click_on_lk_button()
        account.wait_url_to_be(f'{URLs.BASE_URL}{URLs.LOGIN_PAGE}')
        account.fill_auth_fields()
        account.click_login_button()
        account.wait_url_to_be(URLs.BASE_URL)
        account.click_on_lk_button()
        account.wait_url_to_be(f'{URLs.BASE_URL}{URLs.PERSONAL_ACCOUNT_PAGE}')
        account.logout(driver)
        current_url = account.auth_page()
        assert 'login' in current_url
