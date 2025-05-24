import pytest

from project.main_page.main_page_data import *
from project.registration.registration_locators import *
from project.registration.registration_data import *
from playwright.sync_api import sync_playwright, Page
from project.main_page.main_page_locators import *
from project.loan_request.loan_request_data import *
from project.loan_request.loan_request_locators import *

@pytest.fixture()
def browser():
    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


def pw_start(page: Page):
    page.goto(main_page)
    page.click(register_button_path)


def register_fill(page):
    page.fill(reg_fname, first_name)
    page.fill(reg_lname, last_name)
    page.fill(reg_address, address)
    page.fill(reg_city, state_city)
    page.locator(reg_state).fill(state_city)
    page.fill(reg_zip, zip_code)
    page.fill(reg_phone, phone)
    page.fill(reg_ssn, ssn)
    page.fill(reg_username, username)
    page.fill(reg_password, password)
    page.fill(reg_confirm, password)
    page.click(reg_fill_button)
    page.wait_for_timeout(1000)

def test_reg(page):
    pw_start(page)
    register_fill(page)

def login(page):
    page.fill(login_username, username)
    page.fill(login_password, password)
    page.click(login_button_path)

def test_login(page):
    pw_start(page)
    login(page)

def logout(page):
    page.click(logout_button)
    page.wait_for_timeout(1000)

def overview(page):
    page.click(overview_button)

def loan(page):
    page.click(loan_request_button)
    page.fill(loan_amount_field, loan_amount)
    page.fill(loan_payment_field, loan_payment)
    page.click(loan_apply)
    page.wait_for_timeout(1000)

def test_loan(page):
    test_login(page)
    overview(page)
    loan(page)
    logout(page)
