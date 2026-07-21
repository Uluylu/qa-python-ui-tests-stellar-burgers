import allure
from pages.base_page import BasePage
from locators import Locators


class LoginPage(BasePage):

    @allure.step("Авторизоваться под пользователем")
    def login(self, email, password):
        self.fill_field(Locators.EMAIL_FIELD, email)
        self.fill_field(Locators.PASSWORD_FIELD, password)
        self.click_element(Locators.LOGIN_BUTTON)
        