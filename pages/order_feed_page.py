import allure
from pages.base_page import BasePage
from locators import Locators
from urls import Urls


class OrderFeedPage(BasePage):

    @allure.step("Открыть страницу 'Лента заказов'")
    def open_order_feed_page(self):
        self.driver.get(Urls.ORDER_FEED_URL)

    @allure.step("Получить количество заказов 'Выполнено за всё время'")
    def get_total_orders_count(self):
        self.wait_for_element_visibility(Locators.TOTAL_ORDERS_COUNTER)
        count_text = self.get_text(Locators.TOTAL_ORDERS_COUNTER)
        return int(count_text)
    
    @allure.step("Получить количество заказов 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        self.wait_for_element_visibility(Locators.TODAY_ORDERS_COUNTER)
        count_text = self.get_text(Locators.TODAY_ORDERS_COUNTER)
        return int(count_text)
    
    @allure.step("Получить список номеров заказов 'В работе'")
    def get_orders_in_progress_list(self):
        self.wait_for_text_not_to_be_in_element(Locators.ORDER_IN_PROGRESS, "Все текущие заказы готовы!")
        elements = self.find_elements(Locators.ORDER_IN_PROGRESS)
        return [element.text for element in elements]
    
    @allure.step("Ждать пока не загрузится заказ в поле 'В работе'")
    def wait_order_in_progress(self, order):
        self.wait_for_text_to_be_present(Locators.ORDER_IN_PROGRESS, order)
    