from time import sleep

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class Login(BasePage):
    txt_loginHeader = (By.XPATH, "//h1[contains(text(),'Log in')]")
    input_email = (By.ID, "user")
    input_password = (By.ID, "password")
    btn_continue = (By.ID, "login")
    btn_login = (By.XPATH, "//*[@id='login-submit']/span/span[contains(text(),'Log')]")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, value):
        self.sendkeys(self.input_email, value)

    def click_continue(self):
        self.do_click(self.btn_continue)

    def enter_password(self, password):
        self.sendkeys(self.input_password, password)

    def click_login(self):
        self.do_click(self.btn_login)

    def header_displayed(self):
        self.is_displayed(self.txt_loginHeader)


