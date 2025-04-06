import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог

import allure
from data import *
from locators import Locators
from pages.base_page import *


class BaseFunctions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        pass

    @allure.step('Переход по клику на Ленту заказов')
    def click_on_feed_button(self):
        self.find_element(Locators.FEED_BUTTON)
        self.click_element(Locators.FEED_BUTTON)


    @allure.step('Переход по клику на конструктор')
    def click_on_constructor(self):
        self.find_element(Locators.CONSTRUCTOR_BUTTON)
        self.click_element(Locators.CONSTRUCTOR_BUTTON)
        self.check_url(URLs.BASE_URL)

    @allure.step('Открытие всплывающего окна с деталями ингредиента')
    def open_ingredient_popup(self):
        self.find_element(Locators.FLUOR_BUN)
        self.click_element(Locators.FLUOR_BUN)
        self.find_element(Locators.INGREDIENT_DETAILS_WINDOW)

    @allure.step('Закрытие всплывающего окна с деталями ингредиента по клику на крестик')
    def close_ingredient_popup(self):
        self.click_element(Locators.CLOSE_DETAILS_WINDOW_BUTTON)
        self.wait_until_element_closed(Locators.INGREDIENT_DETAILS_WINDOW)

    @allure.step('Проверка отсутствия всплывающего окна с деталями ингредиента после закрытия')
    def check_ingredient_popup_not_located(self):
        self.wait_until_element_closed(Locators.INGREDIENT_DETAILS_WINDOW)
        return self.check_invisibility(Locators.INGREDIENT_DETAILS_WINDOW)

    @allure.step('Добавление ингредиента в заказ')
    def drag_and_drop_ingredient(self):
        source_locator = Locators.FLUOR_BUN
        target_locator = Locators.BASKET
        self.drag_and_drop_element(source_locator, target_locator)

    @allure.step('Получение количества добавленных ингредиентов (каунтер ингредиента)')
    def get_count_of_ingredients(self):
        return self.get_element_text(Locators.ADDED_INGREDIENT_COUNTER)

    @allure.step('Переход по клику на конструктор')
    def click_on_constructor(self):
        self.find_element(Locators.CONSTRUCTOR_BUTTON)
        self.click_element(Locators.CONSTRUCTOR_BUTTON)
        self.check_url(URLs.BASE_URL)

    @allure.step('Авторизация пользователя')
    def user_authorization(self):
        self.find_element(Locators.LOGIN_BUTTON_MAIN_PAGE)
        self.click_element(Locators.LOGIN_BUTTON_MAIN_PAGE)
        self.check_url(URLs.LOGIN_PAGE)
        self.send_keys_to_element(Locators.EMAIL_FIELD_LOGIN_PAGE, TestData.EMAIL_FOR_LOGIN)
        self.send_keys_to_element(Locators.PASSWORD_FIELD_LOGIN_PAGE, TestData.PASSWORD_FOR_LOGIN)
        self.scroll_to_element(Locators.LOGIN_BUTTON)
        self.click_element(Locators.LOGIN_BUTTON)
        self.check_url(URLs.BASE_URL)

    @allure.step('Нажатие на кнопку Оформить заказ')
    def click_order_button(self, driver):
        element = self.find_element(Locators.MAKE_ORDER_BUTTON)
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()


    @allure.step('Ожидание закрытия перекрывающего окна')
    def close_overlay(self):
        self.wait_until_element_closed(Locators.OVERLAY)



