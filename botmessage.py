# from dotenv import load_dotenv
from dotenv import dotenv_values
import random
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = browser.find_element(
            By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        password_input = browser.find_element(
            By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = browser.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
        login_button.click()
        sleep(10)

    def search(self, target_user):
        # click search icon
        self.browser.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div").click()
        sleep(8)

        # click on search bar
        input_search = browser.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input")

        # enter target username
        input_search.send_keys(target_user)
        sleep(8)
        input_search.send_keys(Keys.ENTER, Keys.ENTER)

    def message(self, message):
        # XPATH checker, check for presence of path
        def hasxpath(xpath):
            try:
                browser.find_element(By.XPATH, xpath)
                return True
            except:
                return False

        # enter message section of instagram
        if hasxpath("/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div"):
            # print("YES GOT XPATH")
            message_tab = browser.find_element(
                By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div")
            message_tab.click()
        else:
            # print("NO PATH")
            message_tab = browser.find_element(
                By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div")
            message_tab.click()

        # click on "not now" of notification pop-up
        if hasxpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"):
            pop_up_click = browser.find_element(
                By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            pop_up_click.click()

        # click on message
        input_message = browser.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")

        # type message and send
        input_message.send_keys(message, Keys.ENTER)
        sleep(5)


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        # find "Log in"
        self.browser.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()
        sleep(5)
        return LoginPage(self.browser)


browser = webdriver.Firefox()
browser.implicitly_wait(5)

# load_dotenv()
config = dotenv_values(".env")
# print(config["INSTA_USER"])


def first_login_page(browser, target_user, message):

    # accessing instagram homepage
    home_page = HomePage(browser)

    # login to homepage with user and pass
    login_page = home_page.go_to_login_page()
    login_page.login(config["INSTA_USER"], config["INSTA_PASS"])

    # search for target user
    login_page.search(target_user)

    # enter "message" with target user
    login_page.message(message)

    sleep(5)


def second_login_page(browser, target_user, message):
    # accessing instagram homepage
    home_page = HomePage(browser)
    sleep(5)

    # login to homepage
    login_page = LoginPage(browser)

    # search for target user
    login_page.search(target_user)

    # enter "message" with target user
    login_page.message(message)

    sleep(5)


# user and message to DM
target_user_list = ["yyj0728", "y.uuno"]
randomNumber = random.randint(0, 11)
message_list = ["Happy Birthday!", "clown", "PLEASE REPLY!", "BIGFAN!", "HELLO",
                "i'm tired", "you", "heloo", "hi", "reply me im desperate", "can i be your friend?", "stream twitch!"]
message = message_list[randomNumber]


for target_user in target_user_list:
    if (target_user == target_user_list[0]):
        first_login_page(browser, target_user, message)
    else:
        second_login_page(browser, target_user, message)
