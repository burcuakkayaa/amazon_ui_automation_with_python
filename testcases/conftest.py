import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from configfiles.config import TestData
from pages.home_page import HomePage


@pytest.fixture(autouse=True, scope="class", params=["chrome"])
def test_setup(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        #options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)
    elif request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get(TestData.BASE_URL)
    driver.maximize_window()
    driver.delete_all_cookies()
    request.cls.driver = driver

    yield
    driver.quit()