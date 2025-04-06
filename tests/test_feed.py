import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог

import allure
from data import URLs
from locators import *


class TestFeedPage:
    @allure.title('Проверка появления всплывающего окна при клике на заказ')
    def test_order_popup(self, feed_page, driver):
        feed_page.open_page()
        feed_page.go_to_feed_page(driver)
        feed_page.open_window_with_order_details()
        text = feed_page.get_element_text(Locators.ORDER_STRUCTURE)
        assert 'Cостав' in text

    @allure.title('Проверка отображения заказов пользователя из истории в Ленте заказов')
    def test_check_user_orders_in_feed(self, driver, feed_page, account, base_functions):
        feed_page.open_page()
        base_functions.user_authorization()
        account.click_on_lk_button()
        account.check_account_page()
        account.click_history_button(driver)
        order_number = feed_page.get_first_order_number()
        feed_page.go_to_feed_page(driver)
        feed_page.get_orders_list()
        feed_page.search_user_order_in_feed(order_number)
        assert True


    @allure.title('Проверка отображения номера нового заказа в разделе В работе')
    def test_new_order_number_in_work(self, feed_page, base_functions, driver):
        feed_page.open_page()
        base_functions.drag_and_drop_ingredient()
        base_functions.user_authorization()
        base_functions.click_order_button(driver)
        number = feed_page.get_new_order_number()
        feed_page.close_window_with_order_details(driver)
        feed_page.go_to_feed_page(driver)
        order_in_work = feed_page.get_order_number_in_work()
        assert number in order_in_work

    @allure.title('Проверка увеличения счётчика Выполнено за всё время после создания заказа')
    def test_alltime_orders_counter(self, feed_page,base_functions, driver):
        feed_page.open_page()
        feed_page.go_to_feed_page(driver)
        before = feed_page.all_orders_quantity()
        base_functions.click_on_constructor()
        base_functions.drag_and_drop_ingredient()
        base_functions.user_authorization()
        base_functions.click_order_button(driver)
        feed_page.close_window_with_order_details(driver)
        feed_page.go_to_feed_page(driver)
        after = feed_page.all_orders_quantity()
        assert  int(after) > int(before)

    @allure.title('Проверка увеличения счётчика Выполнено за сегодня после создания заказа')
    def test_daily_orders_counter(self, feed_page, base_functions, driver):
        feed_page.open_page()
        feed_page.go_to_feed_page(driver)
        before = feed_page.daily_orders_quantity()
        base_functions.click_on_constructor()
        base_functions.drag_and_drop_ingredient()
        base_functions.user_authorization()
        base_functions.click_order_button(driver)
        base_functions.close_overlay()
        feed_page.close_window_with_order_details(driver)
        feed_page.go_to_feed_page(driver)
        after = feed_page.daily_orders_quantity()
        assert int(after) > int(before)






