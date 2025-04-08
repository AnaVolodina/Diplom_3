# без неявного импорта не срабатывала команда запуска тестов pytest -v
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import pytest
import requests
from faker import Faker
from data import TestData
from URLs import *
from pages.page_base_functions import *
from pages.page_personal_account import *
from pages.page_password import *
from pages.page_feed import *


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        screen_width = driver.execute_script("return screen.width;")
        screen_height = driver.execute_script("return screen.height;")
        driver.set_window_size(screen_width, screen_height)

    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
        screen_width = driver.execute_script("return screen.width;")
        screen_height = driver.execute_script("return screen.height;")
        driver.set_window_size(screen_width, screen_height)

    else:
        raise TypeError("Driver is not found")
    driver.get(URLs.BASE_URL)
    driver.execute_script(f"document.body.style.zoom='{70}%'")
    yield driver
    driver.quit()

