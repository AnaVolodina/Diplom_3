import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог
import allure
from selenium.webdriver.common.action_chains import ActionChains
from locators import Locators
from pages.base_page import BasePage
from data import TestData
from URLs import *


class Account(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажатие на кнопку Личный кабинет")
    def click_on_lk_button(self):
        self.find_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Проверка перехода на страницу авторизации")
    def authorization_page(self):
        return self.get_current_url()

    @allure.step("Заполнение полей email и пароль")
    def fill_auth_fields(self):
        self.send_keys_to_element(Locators.EMAIL_FIELD_LOGIN_PAGE, TestData.EMAIL_FOR_LOGIN)
        self.send_keys_to_element(Locators.PASSWORD_FIELD_LOGIN_PAGE, TestData.PASSWORD_FOR_LOGIN)

    @allure.step("Нажатие на кнопку Войти")
    def click_login_button(self):
        self.click_element(Locators.LOGIN_BUTTON)

    @allure.step("Проверка перехода на страницу профиля")
    def check_account_page(self):
        self.wait_url_to_be(f'{URLs.BASE_URL}{URLs.PERSONAL_ACCOUNT_PAGE}')
        return self.get_current_url()

    @allure.step("Нажатие на кнопку История заказов и проверка перехода в данный раздел")
    def click_history_button(self, driver):
        element = self.find_element(Locators.ORDER_HISTORY_BUTTON)
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()


    @allure.step("Проверка перехода в раздел История заказов")
    def open_orders_history(self):
        return self.get_current_url()

    @allure.step("Нажатие на кнопку Выход")
    def logout(self, driver):
        element = self.find_element(Locators.LOGOUT_BUTTON)
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()

    @allure.step("Проверка перехода на страницу авторизации после нажатия на кнопку Выход")
    def auth_page(self):
        self.wait_url_to_be(f'{URLs.BASE_URL}{URLs.LOGIN_PAGE}')
        return self.get_current_url()


