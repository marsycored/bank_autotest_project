import pytest
from bank.conf.driver.driver_test import *
from bank.data.page.pages import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bank.data.page.pages import username, password


@pytest.mark.test
def test_login (driver):
    driver.get(main_page)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))


    username_fill = driver.find_element(By.NAME, "username").send_keys(username)
    password_fill = driver.find_element(By.NAME, "password").send_keys(password)


    login_button = driver.find_element(By.XPATH, login_button_path).click()

    time.sleep(5)