import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог

import allure
from locators import Locators
from pages.base_page import *


class TestRecoveryPassword:
    @allure.step('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_recovery_page(self, password_recovery):
        password_recovery.open_page()
        password_recovery.click_on_lk_button()
        password_recovery.click_recovery_password_button()
        expected_url = URLs.FORGOT_PASSWORD_PAGE
        actual_url = password_recovery.get_current_url()
        assert actual_url == expected_url

    @allure.step('Проверка ввода почты и клика по кнопке «Восстановить»')
    def test_enter_email_and_click_recovery(self, password_recovery):
        password_recovery.open_page()
        password_recovery.click_on_lk_button()
        password_recovery.scroll_to_element(Locators.FORGOT_PASSWORD_BUTTON_LOGIN_PAGE)
        password_recovery.click_recovery_password_button()
        password_recovery.recovery_password_page()
        password_recovery.fill_email_field()
        password_recovery.click_repair_button()
        password_recovery.wait_url_to_be(URLs.RESET_PASSWORD_PAGE)
        url = password_recovery.get_current_url()
        assert 'reset-password' in url

    @allure.step('Проверка подсветки поля Пароль после клика по кнопке «Показать/скрыть»')
    def test_lightning_password_field(self, password_recovery):
        password_recovery.open_page()
        password_recovery.click_on_lk_button()
        password_recovery.scroll_to_element(Locators.FORGOT_PASSWORD_BUTTON_LOGIN_PAGE)
        password_recovery.click_recovery_password_button()
        password_recovery.recovery_password_page()
        password_recovery.fill_email_field()
        password_recovery.click_repair_button()
        password_recovery.open_reset_password_page()
        attribute = password_recovery.check_lightning_field().get_attribute('class')
        assert 'active' in attribute