# без неявного импорта не срабатывала команда запуска тестов pytest -v
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import pytest
import requests
from faker import Faker
from data import URLs, TestData, Endpoints
from pages.page_base_functions import *
from pages.page_personal_account import *
from pages.page_password import *
from pages.page_feed import *


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        service = Service()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_window_size(1080, 720)

    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(900, 600)
    else:
        raise TypeError("Driver is not found")
    driver.get(URLs.BASE_URL)
    driver.execute_script("document.body.style.zoom='60%'")
    yield driver
    driver.quit()


@pytest.fixture
def base_functions(driver):
    base_functions = BaseFunctions(driver)
    return base_functions

@pytest.fixture
def password_recovery(driver):
    password_recovery = PasswordRecovery(driver)
    return password_recovery

@pytest.fixture
def account(driver):
    account = Account(driver)
    return account

@pytest.fixture
def feed_page(driver):
    feed_page = FeedPage(driver)
    return feed_page

