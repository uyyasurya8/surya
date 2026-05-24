from playwright.sync_api import sync_playwright , expect
import pytest
import allure
from pages.login import Login,Login_1,Login_2
from common.browser_function import Browser,Browser_1,Browser_2

def test_validation_required_email_1(browser):

    login = Login(browser)

    login.input_pasword('1234567890')
    login.click_btn_submit()

    head = Browser(browser)
    head.validation_message()
    

def test_validation_format_email_2(browser):

    login = Login_1(browser)

    login.input_username('uno.test')
    login.input_pasword('1234567890')
    login.click_btn_submit()

    head = Browser_1(browser)
    head.validation_message()
        
    

def test_validation_format_email_3(browser):

   
    login = Login_2(browser)

    login.input_username('uno.testing3@gmail.')
    login.input_pasword('1234567890')
    login.click_btn_submit()

    head = Browser_2(browser)
    head.validation_message()

        