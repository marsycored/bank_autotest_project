import pytest
import os

from booking.data.page.main_page import page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#def driver():
    #driver_path = ChromeService(executable_path="C:/Users/popov/Документы/QA/материалы/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    #browser = webdriver.Chrome(service=driver_path)
    #yield browser
    #driver.quit()


@pytest.fixture()
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

@pytest.mark.test
def test_one(driver):
    driver.get(page)