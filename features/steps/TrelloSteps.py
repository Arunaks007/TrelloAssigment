from time import sleep

from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains

from PageObjects.CardDetails import CardDetails
from PageObjects.TrelloBoard import ProjectBoard
from PageObjects.TrelloDashboard import DashBoard
from PageObjects.TrelloHomepage import Login


@given(u'I launch the trello website')
def step_impl(context):
    context.driver = webdriver.Chrome(
        executable_path=".\\drivers\\chromedriver.exe")
    context.driver.delete_all_cookies()
    context.driver.get("https://trello.com/login")
    context.driver.maximize_window()


@given(u'I login to the application {value} and {pwd}')
def step_impl(context, value, pwd):
    login_page = Login(context.driver)
    login_page.header_displayed()
    login_page.enter_username(value)
    login_page.click_continue()
    login_page.enter_password(pwd)
    login_page.click_login()


@when(u'The login is done new board is getting created {board}')
def step_impl(context, board):
    dashboard = DashBoard(context.driver)
    dashboard.click_newboard()
    dashboard.enter_boardname(board)
    dashboard.click_create()


@when(u'Im checking whether the board is ready')
def step_impl(context):
    context.board = ProjectBoard(context.driver)
    context.board.verify_boardcreated()


@then(u'I create a four new lists')
def step_impl(context):
    list_names = ["Not Started", "In Progress", "QA", "Done"]

    for i in list_names:
        context.board.enter_listname(i)
        context.board.click_addlist()
    sleep(2)
    context.board.click_cancel()


@then(u'I create a four new cards under a newly created list')
def step_impl(context):
    list_cards = ["Card 1", "Card 2", "Card 3", "Card 4"]
    context.board.click_addaCard()

    for i in list_cards:
        context.board.enter_cardName(i)
        context.board.click_addCard()
    sleep(2)
    context.board.click_cancelCard()


@then(u'Im moving card two to the list inprogress')
def step_impl(context):
    context.board.drag_drop_dynamic("Card 2", "Progress")


@then(u'Im moving card three to the list QA')
def step_impl(context):
    context.board.drag_drop_dynamic("Card 3", "QA")


@then(u'Im moving card two from inprogress to the list QA')
def step_impl(context):
    context.board.drag_drop_dynamic("Card 2", "QA")


@then(u'Im opening card one and assigning it to current user')
def step_impl(context):
    context.board.click_card("Card 1")
    context.details = CardDetails(context.driver)
    context.details.click_member()
    context.details.click_current_user()
    context.details.click_close_member()


@then(u'Im leaving a comment on card one {comments}')
def step_impl(context,comments):
    context.details.enter_comment(comments)
    context.details.click_save_comment()
    sleep(2)
