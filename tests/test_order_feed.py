import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.title("При создании нового заказа увеличивается счетчик 'Выполнено за все время'")
    def test_total_orders_counter_increases_after_new_order(self, driver, authorized):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)

        main_page.click_orders_feed_button()
        before_order = order_page.get_total_orders_count()

        main_page.click_constructor_button()
        main_page.add_ingredients_to_constructor()
        main_page.click_place_order_button()
        main_page.get_created_order_number()

        main_page.close_modal_window()
        
        main_page.click_orders_feed_button()
        after_order = order_page.get_total_orders_count()

        assert before_order + 1 == after_order

    @allure.title("При создании нового заказа увеличивается счетчик 'Выполнено за сегодня'")
    def test_today_orders_counter_increases_after_new_order(self, driver, authorized):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)

        main_page.click_orders_feed_button()
        before_order = order_page.get_today_orders_count()

        main_page.click_constructor_button()
        main_page.add_ingredients_to_constructor()
        main_page.click_place_order_button()
        main_page.get_created_order_number()

        main_page.close_modal_window()

        main_page.click_orders_feed_button()
        after_order = order_page.get_today_orders_count()

        assert before_order + 1 == after_order

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress(self, driver, authorized):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)

        main_page.add_ingredients_to_constructor()
        main_page.click_place_order_button()
        order = main_page.get_created_order_number()

        main_page.close_modal_window()

        main_page.click_orders_feed_button()
        order_page.wait_order_in_progress(order)
        all_orders = order_page.get_orders_in_progress_list()

        assert order in all_orders or f"0{order}" in all_orders
