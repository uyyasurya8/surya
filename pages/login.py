from playwright.sync_api import sync_playwright , expect
from locators.login import Loc
import allure

class Login:
    def __init__(self,driver):
        self.driver = driver
    
    @allure.step('input password')
    def input_pasword(self,password):         
        self.driver.locator(Loc.input_password).fill(password)

    @allure.step('click button login')
    def click_btn_submit(self):
        self.driver.locator(Loc.btn_submit).click()


        