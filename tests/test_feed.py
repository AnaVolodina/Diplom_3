import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог

import allure
from locators import *
from pages.page_personal_account import Account
from pages.page_base_functions import BaseFunctions
from pages.page_feed import FeedPage



class TestFeedPage:
    @allure.title('Проверка появления всплывающего окна при клике на заказ')
    def test_order_popup(self, driver):
        feed_page = FeedPage(driver)
        feed_page.go_to_feed_page(driver)
        feed_page.open_window_with_order_details()
        text = feed_page.get_element_text(Locators.ORDER_STRUCTURE)
        assert 'Cостав' in text

    @allure.title('Проверка отображения заказов пользователя из истории в Ленте заказов')
    def test_check_user_orders_in_feed(self, driver):
        feed_page = FeedPage(driver)
        account = Account(driver)
        base_functions = BaseFunctions(driver)
        base_functions.drag_and_drop_ingredient()
        base_functions.user_authorization()
        base_functions.click_order_button(driver)
        base_functions.wait_until_element_closed(Locators.ID_9999)
        base_functions.check_invisibility(Locators.ID_9999)
        base_functions.find_element_with_wait(Locators.NEW_ORDER_NUMBER)
        order_number = base_functions.get_element_text(Locators.NEW_ORDER_NUMBER)
        feed_page.close_window_with_order_details(driver)
        feed_page.go_to_feed_page(driver)
        order_id_feed = feed_page.order_id_found_in_history(order_number)
        base_functions.find_element_with_wait(Locators.PERSONAL_ACCOUNT_BUTTON)
        account.click_on_lk_button()
        account.check_account_page()
        account.click_history_button(driver)
        order_id_history = feed_page.order_id_found_in_history(order_number)
        assert order_id_feed and order_id_history


    @allure.title('Проверка отображения номера нового заказа в разделе В работе')
    def test_new_order_number_in_work(self, driver):
        feed_page = FeedPage(driver)
        base_functions = BaseFunctions(driver)
        base_functions.drag_and_drop_ingredient()
        base_functions.user_authorization()
        base_functions.click_order_button(driver)
        number = feed_page.get_new_order_number()
        feed_page.close_window_with_order_details(driver)
        feed_page.go_to_feed_page(driver)
        order_in_work = feed_page.get_order_number_in_work()
        assert number in order_in_work

    @allure.title('Проверка увеличения счётчика Выполнено за всё время после создания заказа')
    def test_alltime_orders_counter(self, driver):
        feed_page = FeedPage(driver)
        base_functions = BaseFunctions(driver)
        feed_page.go_to_feed_page(driver)
        before = feed_page.all_orders_quantity()
        base_functions.click_on_constructor()
        base_functions.drag_and_drop_ingredient()
        base_functions.user_authorization()
        base_functions.click_order_button(driver)
        base_functions.wait_until_element_visibility(Locators.CLOSE_ORDER_DETAILS_POPUP)
        feed_page.close_window_with_order_details(driver)
        feed_page.go_to_feed_page(driver)
        after = feed_page.all_orders_quantity()
        assert  int(after) > int(before)

    @allure.title('Проверка увеличения счётчика Выполнено за сегодня после создания заказа')
    def test_daily_orders_counter(self, driver):
        feed_page = FeedPage(driver)
        base_functions = BaseFunctions(driver)
        feed_page.go_to_feed_page(driver)
        before = feed_page.daily_orders_quantity()
        base_functions.click_on_constructor()
        base_functions.drag_and_drop_ingredient()
        base_functions.user_authorization()
        base_functions.click_order_button(driver)
        base_functions.wait_until_element_visibility(Locators.CLOSE_ORDER_DETAILS_POPUP)
        feed_page.close_window_with_order_details(driver)
        feed_page.go_to_feed_page(driver)
        after = feed_page.daily_orders_quantity()
        assert int(after) > int(before)






