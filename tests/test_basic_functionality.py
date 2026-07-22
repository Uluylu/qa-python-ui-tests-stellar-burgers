import allure
from pages.main_page import MainPage
from urls import Urls


class TestBasicFunc:

    @allure.title("Переход в раздел 'Лента заказов'")
    def test_order_feed_button_click_navigates_to_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)

        main_page.click_orders_feed_button()

        assert main_page.get_current_url() == Urls.ORDER_FEED_URL

    @allure.title("Переход в раздел 'Конструктор'")
    def test_constructor_button_click_navigates_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)

        main_page.click_orders_feed_button()
        main_page.click_constructor_button()

        assert main_page.get_current_url() == Urls.BASE_URL

    @allure.title("Открытие всплывающего окна с деталями ингредиента")
    def test_ingredient_click_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)

        main_page.click_ingredient_bun()

        assert main_page.get_modal_title() == "Детали ингредиента"

    @allure.title("Закрытие всплывающего окна с деталями ингредиента")
    def test_ingredient_modal_close_button_closes_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)

        main_page.click_ingredient_bun()
        main_page.close_modal_window()

        assert main_page.modal_closed()

    @allure.title("Счетчик ингредиента увеличивается при его добавлении в заказ")
    def test_ingredient_add_to_constructor_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)

        before = main_page.get_ingredient_counter_value()
        main_page.add_ingredient_to_constructor()
        after = main_page.get_ingredient_counter_value()

        assert before + 1 == after
