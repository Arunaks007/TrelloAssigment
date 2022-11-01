from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class CardDetails(BasePage):

    btn_members = (By.XPATH, "//div/a[contains(@title,'Members')]")
    btn_current_user = (By.XPATH, "//a[contains(@title,'user')]")
    btn_close = (By.XPATH, "//a[contains(@class,'close-btn')]")

    #comment
    textarea_comment = (By.XPATH, "//div[@class='comment-box']/textarea")
    btn_save_comment = (By.XPATH, "(//*[@value='Save'])[last()]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_member(self):
        self.do_click(self.btn_members)

    def click_current_user(self):
        self.do_click(self.btn_current_user)

    def click_close_member(self):
        self.do_click(self.btn_close)

    def enter_comment(self, comment):
        self.sendkeys(self.textarea_comment, comment)

    def click_save_comment(self):
        self.do_click(self.btn_save_comment)

