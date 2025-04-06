import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог

import allure
from selenium.webdriver.support.expected_conditions import invisibility_of_element

from data import *
from locators import *


class TestBaseFunctions:
    @allure.title('Проверка перехода нажатием на Ленту заказов')
    def test_url_feed_page(self, base_functions):
        base_functions.open_page()
        base_functions.click_on_feed_button()
        expected_url = URLs.FEED_PAGE
        base_functions.check_url(expected_url)
        actual_url = base_functions.get_current_url()
        assert actual_url == expected_url

    @allure.title('Проверка перехода нажатием на Конструктор')
    def test_url_constructor(self, base_functions):
        base_functions.open_page()
        base_functions.click_on_feed_button()
        base_functions.click_on_constructor()
        expected_url = URLs.BASE_URL
        base_functions.check_url(expected_url)
        actual_url = base_functions.get_current_url()
        assert actual_url == expected_url

    @allure.title('Проверка появления всплывающего окна с деталями при клике на ингредиент')
    def test_ingredient_details_window_located(self, base_functions):
        base_functions.open_page()
        base_functions.open_ingredient_popup()
        title = base_functions.get_element_text(Locators.INGREDIENT_DETAILS_WINDOW)
        assert "Детали" in title

    @allure.title('Проверка закрытия всплывающего окна с деталями при клике на крестик')
    def test_ingredient_details_window_closed(self, base_functions):
        base_functions.open_page()
        base_functions.open_ingredient_popup()
        base_functions.close_ingredient_popup()
        assert base_functions.check_ingredient_popup_not_located()

    @allure.title('Проверка увеличения каунтера ингредиента при добавлении ингредиента в заказ')
    def test_ingredient_counter(self, base_functions):
        base_functions.drag_and_drop_ingredient()
        base_functions.get_count_of_ingredients()
        assert "2" in base_functions.get_element_text(Locators.ADDED_INGREDIENT_COUNTER)

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_make_order(self, base_functions, driver):
        base_functions.drag_and_drop_ingredient()
        base_functions.user_authorization()
        base_functions.click_order_button(driver)
        base_functions.wait_until_element_closed(Locators.ID_9999)

        base_functions.find_element_with_wait(Locators.ORDER_ID_IN_ORDER_WINDOW)
        text = base_functions.get_element_text(Locators.ORDER_ID_IN_ORDER_WINDOW)
        assert 'идентификатор' in text
