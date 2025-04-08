import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог

import allure
from URLs import *
from selenium.webdriver.common.keys import Keys
from locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход в раздел Лента заказов')
    def go_to_feed_page(self, driver):
        element = self.find_element(Locators.FEED_BUTTON)
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
        self.wait_url_to_be(f'{URLs.BASE_URL}{URLs.FEED_PAGE}')


    @allure.step('Клик по заказу в ленте и открытие окна с деталями заказа')
    def open_window_with_order_details(self):
        self.find_element(Locators.FIRST_ORDER_IN_HISTORY_FEED_PAGE)
        self.click_element(Locators.FIRST_ORDER_IN_HISTORY_FEED_PAGE)
        self.wait_until_element_visibility(Locators.ORDER_DETAILS_POPUP)

    @allure.step('Закрытие окна с деталями заказа')
    def close_window_with_order_details(self, driver):
        self.wait_until_element_closed(Locators.LOADING_ANIMATION)
        self.wait_until_element_closed(Locators.ID_9999)
        self.find_element(Locators.ORDER_ID_IN_ORDER_WINDOW)
        element = self.find_element(Locators.CLOSE_ORDER_DETAILS_POPUP)
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()


    @allure.step("Проверка совпадения заказов в истории и в ленте")
    def check_order_id(self, order_id, locator):
        elements = self.find_until_all_elements_located(locator)
        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step("Проверка нахождения идентификатора заказа в истории")
    def order_id_found_in_history(self, order_number):
        return self.check_order_id(order_number, Locators.USER_ORDERS_LIST)

    @allure.step('Получение номера нового заказа')
    def get_new_order_number(self):
        self.wait_until_element_closed(Locators.LOADING_ANIMATION)
        self.wait_until_element_closed(Locators.ID_9999)
        self.find_element(Locators.NEW_ORDER_NUMBER)
        return self.get_element_text(Locators.NEW_ORDER_NUMBER)

    @allure.step('Получение номера заказа в работе')
    def get_order_number_in_work(self):
        self.wait_until_element_closed(Locators.ALL_ORDERS_DONE)
        self.find_element_with_wait(Locators.NUMBER_OF_ORDER_IN_WORK)
        return self.get_element_text(Locators.NUMBER_OF_ORDER_IN_WORK)


    @allure.step('Проверка увеличения количества заказов на счетчике Выполнено за всё время')
    def all_orders_quantity(self):
        self.wait_until_element_closed(Locators.ALL_ORDERS_DONE)
        self.scroll_to_element(Locators.TITLE_ALL_TIME_ORDERS)
        return self.get_element_text(Locators.COUNTER_ALL_ORDERS)

    @allure.step('Проверка увеличения количества заказов на счетчике Выполнено за сегодня')
    def daily_orders_quantity(self):
        self.wait_until_element_closed(Locators.ALL_ORDERS_DONE)
        self.scroll_to_element(Locators.TITLE_DAILY_ORDERS)
        return self.get_element_text(Locators.COUNTER_DAILY_ORDERS)




