import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог

import allure
from data import URLs
from selenium.webdriver.common.keys import Keys
from locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        pass

    @allure.step('Переход в раздел Лента заказов')
    def go_to_feed_page(self, driver):
        self.wait_until_element_closed(Locators.OVERLAY)
        element = self.find_element(Locators.FEED_BUTTON)
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
        self.wait_url_to_be(URLs.FEED_PAGE)


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

    @allure.step('Получение номера первого заказа из истории заказов пользователя')
    def get_first_order_number(self):
        self.find_element(Locators.FIRST_USER_ORDER)
        self.click_element(Locators.FIRST_USER_ORDER)
        self.get_element_text(Locators.FIRST_USER_ORDER_ID)
        self.click_element(Locators.CLOSE_DETAILS_WINDOW_BUTTON)

    @allure.step('Проверка отображения заказов из истории на странице «Лента заказов»')
    def search_user_order_in_feed(self, order_number):

        order_elements = self.driver.find_elements(*Locators.ORDER_NUMBER_LIST)  # Получаем список элементов с номерами заказов
        for element in order_elements:
            if order_number in element.text:  # Ищем совпадение
                return True  # Если есть - возвращаем True
        return False

    @allure.step('Получение списка заказов из Ленты заказов')
    def get_orders_list(self):
        order = self.find_until_all_elements_located(Locators.ALL_ORDERS_FEED_PAGE)
        for order_list in order:
            order_number = order_list.text
            return order_number


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




