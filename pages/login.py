from playwright.sync_api import sync_playwright , expect
from locators.login import Loc,Loc_1,Loc_2
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


class Login_1:
    def __init__(self,driver):
        self.driver = driver

    @allure.step('input username')
    def input_username(self,username):         
        self.driver.locator(Loc_1.input_username).fill(username)

    @allure.step('input password')
    def input_pasword(self,password):         
        self.driver.locator(Loc_1.input_password).fill(password)

    @allure.step('click button login')
    def click_btn_submit(self):
        self.driver.locator(Loc_1.btn_submit).click()


class Login_2:
    def __init__(self,driver):
        self.driver = driver
    
    @allure.step('input username')
    def input_username(self,username):         
        self.driver.locator(Loc_2.input_username).fill(username)
    
    @allure.step('input password')
    def input_pasword(self,password):         
        self.driver.locator(Loc_2.input_password).fill(password)

    @allure.step('click button login')
    def click_btn_submit(self):
        self.driver.locator(Loc_2.btn_submit).click()