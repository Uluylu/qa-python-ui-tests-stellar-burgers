import allure
from pages.base_page import BasePage
from locators import Locators



class MainPage(BasePage):

    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor_button(self):
        self.click_element(Locators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на раздел 'Лента заказов'")
    def click_orders_feed_button(self):
        element = self.find_element(Locators.ORDERS_FEED_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient_bun(self):
        self.click_element(Locators.INGREDIENT_BUN)

    @allure.step("Получить заголовок модального окна ингредиента")
    def get_modal_title(self):
        return self.get_text(Locators.MODAL_TITLE)

    @allure.step("Закрыть всплывающее окно")
    def close_modal_window(self):
        element = self.find_element(Locators.CLOSE_MODAL_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)
        self.wait_for_invisibility(Locators.MODAL_OVERLAY)

    @allure.step("Проверить, что всплювающее окно закрылось")
    def modal_closed(self):
        return self.wait_for_invisibility(Locators.MODAL_TITLE)
    
    @allure.step("Дождаться появления кнопки 'Оформить заказ'")
    def wait_for_place_order_button(self):
        return self.wait_for_element_visibility(Locators.PLACE_ORDER_BUTTON)

    @allure.step("Кликнуть по кнопке 'Оформить заказ'")
    def click_place_order_button(self):
        self.click_element(Locators.PLACE_ORDER_BUTTON)

    @allure.step("Добавить соус ингредиент в заказ")
    def add_ingredient_to_constructor(self):
        self.move_ingredient(Locators.INGREDIENT_SAUCE, Locators.CONSTRUCTOR_BASKET)

    @allure.step("Добавить ингредиенты в заказ")
    def add_ingredients_to_constructor(self):
        self.move_ingredient(Locators.INGREDIENT_BUN, Locators.CONSTRUCTOR_BASKET)
        self.move_ingredient(Locators.INGREDIENT_MEAT, Locators.CONSTRUCTOR_BASKET)
        self.move_ingredient(Locators.INGREDIENT_SAUCE, Locators.CONSTRUCTOR_BASKET)

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter_value(self):
        return int(self.get_text(Locators.INGREDIENT_SAUCE_COUNTER))

    @allure.step("Получить номер созданного заказа")
    def get_created_order_number(self):
        self.wait_for_text_not_to_be_in_element(Locators.NUMBER_ORDER, "9999")
        return self.get_text(Locators.NUMBER_ORDER)
    
    @allure.step("Кликнуть по кнопке 'Войти в аккаунт'")
    def click_login_in_account(self):
        self.click_element(Locators.AUTHORIZATION_BUTTON)
    