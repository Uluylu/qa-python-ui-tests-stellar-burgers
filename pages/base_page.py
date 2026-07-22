import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход по указанному URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Клик по элементу с помощью JavaScript")
    def click_with_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Найти элемент с локатором: {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step("Найти все элементы с локатором: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Выполнить клик по элементу с локатором: {locator}")
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Заполнить поле {locator} значением: {text}")
    def fill_field(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step("Перетащить ингредиент")
    def move_ingredient(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
    
        self.driver.execute_script(
        "arguments[0].dispatchEvent(new DragEvent('dragstart', {bubbles: true}));"
        "arguments[1].dispatchEvent(new DragEvent('drop', {bubbles: true}));",
        source, target)

    @allure.step("Прокрутить страницу до элемента с локатором: {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
        return element
    
    @allure.step("Получить текст элемента с локатором: {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Ждать исчезновения элемента с локатором: {locator}")
    def wait_for_invisibility(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located(locator))
    
    @allure.step("Ждать пока появится элемент с локатором: {locator}")
    def wait_for_element_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
    
    @allure.step("Ждать исчезновения текста '{text}' из элемента с локатором: {locator}")
    def wait_for_text_not_to_be_in_element(self, locator, text):
        return WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(locator, text))
    
    @allure.step("Ждать появления текста '{text}' в элементе с локатором: {locator}")
    def wait_for_text_to_be_present(self, locator, text):
        return WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url
    