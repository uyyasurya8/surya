from playwright.sync_api import sync_playwright , expect
import pytest
import allure
from pages.login import Login
from common.browser_function import Browser
def test_validation_required_email_1(browser):

    login = Login(browser)

    login.input_pasword('1234567890')
    login.click_btn_submit()

    head = Browser(browser)
    head.validation_message()
    

# def test_validation_format_email_2():

#     with sync_playwright() as p:

#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()

#         page.goto("https://test.kelasotomesyen.com/",timeout=10000)
#         page.locator('[data-testid="login-email-input"]').fill("uno.test")
#         page.locator('[data-testid="login-password-input"]').fill("1234567890")
#         page.locator('[data-testid="login-submit-button"]').click()
#         validation_message = page.locator('[data-testid="login-email-input"]').evaluate("element => element.validationMessage")
#         print("Validation Message :", validation_message)
#         assert validation_message == "Please include an '@' in the email address. 'uno.test' is missing an '@'."
#         page.wait_for_timeout(5000)

# def test_validation_format_email_3():

#     with sync_playwright() as p:

#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()

#         page.goto("https://test.kelasotomesyen.com/",timeout=10000)
#         page.locator('[data-testid="login-email-input"]').fill("uno.testing3@gmail.")
#         page.locator('[data-testid="login-password-input"]').fill("1234567890")
#         page.locator('[data-testid="login-submit-button"]').click()
#         validation_message = page.locator('[data-testid="login-email-input"]').evaluate("element => element.validationMessage")
#         print("Validation Message :", validation_message)
#         assert validation_message == "'.' is used at a wrong position in 'gmail.'."
#         page.wait_for_timeout(5000)

#         browser.close()