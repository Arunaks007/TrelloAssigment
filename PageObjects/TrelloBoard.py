from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class ProjectBoard(BasePage):
    btn_addnewlist = (By.XPATH, "//*[@id='board']/div/form/a")
    input_list = (By.XPATH, "//*[@id='board']/div/form/a/following::input[1]")
    btn_addlist = (By.XPATH, "//*[@id='board']/div/form/a/following::input[2]")
    btn_cancel = (By.XPATH, "//a[contains(@aria-label,'Cancel')]")
    board = (By.ID, "board")

    btn_addacard = (By.XPATH, "(//*[@id='board']/div/div/div/a)[1]")
    textarea_card = (By.XPATH, "//textarea[contains(@placeholder,'Enter a title for')]")
    btn_addcard = (By.XPATH, "//input[contains(@value,'Add card')]")
    btn_cancelcard = (By.XPATH, "//input[contains(@value,'Add card')]/following::a[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_boardcreated(self):
        self.is_displayed(self.board)

    def click_addanewlist(self):
        self.do_click(self.btn_addnewlist)

    def enter_listname(self, name):
        self.sendkeys(self.input_list, name)

    def click_addlist(self):
        self.do_click(self.btn_addlist)

    def click_cancel(self):
        self.do_click(self.btn_cancel)

    def click_addaCard(self):
        self.do_click(self.btn_addacard)

    def enter_cardName(self, name):
        self.sendkeys(self.textarea_card, name)

    def click_addCard(self):
        self.do_click(self.btn_addcard)

    def click_cancelCard(self):
        self.do_click(self.btn_cancelcard)

    def drag_drop_dynamic(self, cardname, target):
        action = ActionChains(self.driver)

        card_names = self.driver.find_elements("xpath",
                                               "//div[@id='board']/div/div/div[contains(@class,'list-cards')]/a//span[contains(@class,'card-name')]")
        if target == "Progress":
            target_path = self.driver.find_element("xpath",
                                                  "(//div[@id='board']/div/div/div[contains(@class,'list-cards')])[2]");
        elif target == "QA":
            target_path = self.driver.find_element("xpath",
                                                  "(//div[@id='board']/div/div/div[contains(@class,'list-cards')])[3]");
        else:
            target_path = self.driver.find_element("xpath",
                                                  "(//div[@id='board']/div/div/div[contains(@class,'list-cards')])[4]");

        for names in card_names:
            if names.text == cardname:
                action.drag_and_drop(names, target_path).perform()

    def click_card(self, card_name):
        card_names = self.driver.find_elements("xpath",
                                               "//div[@id='board']/div/div/div[contains(@class,'list-cards')]/a//span[contains(@class,'card-name')]")

        for names in card_names:
            if names.text == card_name:
                names.click()