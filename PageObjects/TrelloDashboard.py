from time import sleep

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class DashBoard(BasePage):
    btn_createNewBoard = (By.XPATH, "//*[@*='create-board-tile']")
    input_boardTitle = (By.XPATH, "//*[@*='create-board-title-input']")
    btn_create = (By.XPATH, "//*[@*='create-board-submit-button']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_newboard(self):
        self.do_click(self.btn_createNewBoard)

    def enter_boardname(self, value):
        self.sendkeys(self.input_boardTitle, value)

    def click_create(self):
        self.do_click(self.btn_create)
