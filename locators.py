from selenium.webdriver.common.by import By


class Locators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
    INGREDIENT_BUN = (By.CSS_SELECTOR, "img[alt='Флюоресцентная булка R2-D3']")
    INGREDIENT_SAUCE = (By.CSS_SELECTOR, "img[alt='Соус Spicy-X']")
    INGREDIENT_MEAT = (By.CSS_SELECTOR, "img[alt='Филе Люминесцентного тетраодонтимформа']")
    INGREDIENT_SAUCE_COUNTER = (By.XPATH, "//img[contains(@alt, 'Spicy-X')]/../div[1]/p")
    CONSTRUCTOR_BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    MODAL_TITLE = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal')]//button")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    
    AUTHORIZATION_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    EMAIL_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    NUMBER_ORDER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/../p[2]")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/../p[2]")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")
    