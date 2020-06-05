#!/usr/bin/python3

"""
    Made by:
        - Camilo Laiton

        University of Magdalena, Colombia
        2020-1
        GitHub: https://github.com/camilolaiton/
"""

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators import *
from secrets import youtube_pro, youtube_pw
import time
"""
from pynput.keyboard import Key, Controller

keyboard = Controller()
keyboard.type('Hello World')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
"""
TIME_TO_SLEEP = 2

class YoutubePageBot():

    def __init__(self, time_to_wait=5):
        self.web_link = "https://youtube.com/"

        self.driver = webdriver.Firefox(
            executable_path="./geckodriver"
        )
        self.driver.implicitly_wait(time_to_wait)
        self.login_state = False
        self.username = None
        self.driver.get(self.web_link)

    def signIn(self, username, password):
        if not self.login_state:
            self.driver.get(self.web_link)

            time.sleep(TIME_TO_SLEEP)
            access_btn = self.driver.find_element(*YoutubeLoginPage.get_access_btn).click()
            
            try:
                self.driver.find_element(*YoutubeLoginPage.another_account_btn).click()
            except NoSuchElementException:
                print("Another account click wasn't necesary.")

            username_box = self.driver.find_element(*YoutubeLoginPage.username_box)
            username_box.click()
            time.sleep(TIME_TO_SLEEP)
            username_box.send_keys(username)
            time.sleep(TIME_TO_SLEEP)
            # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(*YoutubeLoginPage.username_box)).send_keys(self.username)
            self.driver.find_element(*YoutubeLoginPage.next_btn).click()
            self.username = username

            password_box = self.driver.find_element(*YoutubeLoginPage.password_box)
            password_box.click()
            password_box.send_keys(password)

            self.driver.find_element(*YoutubeLoginPage.sign_in_btn).click()
            
            try:
                logged_account = self.driver.find_element(*YoutubeWelcomePage.create_content_link)
                self.login_state = True
            except NoSuchElementException:
                self.login_state = False

            return self.login_state
        return False

    def signOut(self):
        if self.login_state:
            self.driver.find_element(*YoutubeWelcomePage.profile_link).click()
            self.driver.find_element(*YoutubeWelcomePage.sign_out_btn).click()
            self.login_state = False
            return True
        return False

    def findYoutubeVideo(self, course_name):

        search_bar = self.driver.find_element(*YoutubeSearcher.search_bar)
        search_bar.clear()
        search_bar.send_keys(course_name)

        time.sleep(TIME_TO_SLEEP)
        search_button = self.driver.find_element(*YoutubeSearcher.search_btn).click()
        time.sleep(TIME_TO_SLEEP)
        first_video = self.driver.find_element(*YoutubeSearcher.first_video).click()

if __name__ == "__main__":
    youtubePage = YoutubePageBot()
    # print("youtubeLogin:", youtubePage.signIn(youtube_pro, youtube_pw))
    # print("youtubeLogout:", youtubePage.signOut())
    youtubePage.findYoutubeVideo("guns and roses")
