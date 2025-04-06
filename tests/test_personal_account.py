import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог
import allure
from data import URLs


class TestAccount:
    @allure.step("Проверка перехода по клику на Личный кабинет")
    def test_switch_to_lk(self, account):
        account.open_page()
        account.click_on_lk_button()
        current_url = account.authorization_page()
        assert 'login' in current_url

    @allure.step("Проверка перехода в раздел История заказов")
    def test_switch_to_order_history(self, account, driver, base_functions):
        account.open_page()
        account.click_on_lk_button()
        account.wait_url_to_be(URLs.LOGIN_PAGE)
        account.fill_auth_fields()
        account.click_login_button()
        account.wait_url_to_be(URLs.BASE_URL)
        account.click_on_lk_button()
        account.check_account_page()
        account.click_history_button(driver)
        base_functions.close_overlay()
        current_url = account.open_orders_history()
        assert current_url == URLs.ORDER_HISTORY_PAGE

    @allure.step("Проверка выхода из аккаунта")
    def test_logout(self, account, driver):
        account.open_page()
        account.click_on_lk_button()
        account.wait_url_to_be(URLs.LOGIN_PAGE)
        account.fill_auth_fields()
        account.click_login_button()
        account.wait_url_to_be(URLs.BASE_URL)
        account.click_on_lk_button()
        account.wait_url_to_be(URLs.PERSONAL_ACCOUNT_PAGE)
        account.logout(driver)
        current_url = account.auth_page()
        assert 'login' in current_url
