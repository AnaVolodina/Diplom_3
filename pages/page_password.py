import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from locators import Locators

from pages.base_page import BasePage
from data import TestData
from URLs import *
from selenium.webdriver.common.keys import Keys

class PasswordRecovery(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажатие на кнопку Войти в аккаунт")
    def click_on_lk_button(self):
        login_button = self.find_element(Locators.LOGIN_BUTTON_MAIN_PAGE)
        self.click_element(login_button)

    @allure.step("Нажатие на кнопку Восстановить пароль")
    def click_recovery_password_button(self):
        self.scroll_to_element(Locators.REPAIR_PASSWORD_BUTTON_LOGIN_PAGE)
        self.click_element(Locators.REPAIR_PASSWORD_BUTTON_LOGIN_PAGE)

    @allure.step("Проверка перехода на страницу восстановления пароля")
    def recovery_password_page(self):
        self.check_url(f'{URLs.BASE_URL}{URLs.FORGOT_PASSWORD_PAGE}')

    @allure.step("Заполнение поля email на странице восстановления пароля")
    def fill_email_field(self):
        self.find_element(Locators.EMAIL_FIELD_REPAIR_PASSWORD_PAGE)
        self.send_keys_to_element(Locators.EMAIL_FIELD_REPAIR_PASSWORD_PAGE, TestData.EMAIL_FOR_LOGIN)

    @allure.step("Нажатие на кнопку Восстановить")
    def click_repair_button(self):
        self.find_element(Locators.REPAIR_BUTTON)
        self.click_element(Locators.REPAIR_BUTTON)

    @allure.step("Ожидание перехода на страницу сброса пароля")
    def open_reset_password_page(self):
        self.wait_url_to_be(f'{URLs.BASE_URL}{URLs.RESET_PASSWORD_PAGE}')


    @allure.step("Проверка подсветки поля при клике по кнопке показать/скрыть пароль")
    def check_lightning_field(self):
        self.wait_until_element_closed(Locators.LOADING_ANIMATION)
        self.find_element(Locators.SHOW_PASSWORD_BUTTON)
        self.click_element(Locators.SHOW_PASSWORD_BUTTON)
        self.wait_until_element_closed(Locators.LOADING_ANIMATION)
        return self.find_element(Locators.ACTIVE_PASSWORD_FIELD_RESET_PASSWORD_PAGE)

