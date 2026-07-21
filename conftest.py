import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from urls import Urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    elif request.param == "firefox":
        browser = webdriver.Firefox()
    
    browser.set_window_size(1920, 1080)
    
    yield browser
    
    browser.quit()

@pytest.fixture
def user_credentials():
    return {
        "email": "testovoeimya@yandex.ru",
        "password": "123456TestovoeImya"
    }

@pytest.fixture
def authorized(driver, user_credentials):
    driver.get(Urls.BASE_URL)
    
    main_page = MainPage(driver)
    main_page.click_login_in_account()
    
    login_page = LoginPage(driver)
    login_page.login(user_credentials["email"], user_credentials["password"])
    main_page.wait_for_place_order_button()

    return driver
