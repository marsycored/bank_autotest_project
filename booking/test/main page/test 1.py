
from booking.conf.driver.booking_driver import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.mark.test
def test_web_page(driver):
    driver.get(page)

    reservation_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-primary[href^='/reservation']"))
    )

    # Скроллим к кнопке
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", reservation_button)

    # Ждём, пока кнопка реально станет кликабельной
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-primary[href^='/reservation']")))

    # Кликаем через ActionChains (надёжнее на этой странице)
    ActionChains(driver).move_to_element(reservation_button).click().perform()


