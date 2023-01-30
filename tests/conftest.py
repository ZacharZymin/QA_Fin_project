from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.core.utils import ChromeType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest


@pytest.fixture
def get_options():
    options = ChromeOptions()
    options.add_argument('-chrome')  # Use --headless if you do not need browser UI
    options.add_argument('--start-maximized')
    # options.add_argument('--window-size=1200, 800')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    return options


@pytest.fixture
def get_webdriver(get_options):
    options = get_options

    driver = webdriver.Chrome(options=options,
                              service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    return driver


@pytest.fixture
def setup(request, get_webdriver):
    driver = get_webdriver
    url = "https://www.google.com/intl/ru/gmail/about/"
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
