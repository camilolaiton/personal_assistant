#!/usr/bin/python3

"""
    Made by:
        - Camilo Laiton

        University of Magdalena, Colombia
        2020-1
        GitHub: https://github.com/camilolaiton/
"""

from selenium.webdriver.common.by import By

class YoutubeLoginPage(object):
    another_account_btn = (By.CSS_SELECTOR, 'li.JDAKTe:nth-child(2) > div:nth-child(1)')
    get_access_btn = (By.CSS_SELECTOR, 'ytd-button-renderer.style-scope:nth-child(4) > a:nth-child(1) > paper-button:nth-child(1) > yt-formatted-string:nth-child(2)')
    username_box = (By.CSS_SELECTOR, '#identifierId')
    next_btn = (By.CSS_SELECTOR, '.RveJvd')
    password_box = (By.CSS_SELECTOR, '.I0VJ4d > div:nth-child(1) > input:nth-child(1)')
    sign_in_btn = (By.CSS_SELECTOR, '#passwordNext > span:nth-child(3) > span:nth-child(1)')
    
class YoutubeWelcomePage(object):
    create_content_link = (By.CSS_SELECTOR, 'ytd-topbar-menu-button-renderer.style-scope:nth-child(1) > div:nth-child(2) > a:nth-child(1) > yt-icon-button:nth-child(1) > button:nth-child(1) > yt-icon:nth-child(1)')
    profile_link = (By.CSS_SELECTOR, 'yt-img-shadow.ytd-topbar-menu-button-renderer > img:nth-child(1)')
    sign_out_btn = (By.CSS_SELECTOR, 'yt-multi-page-menu-section-renderer.style-scope:nth-child(1) > div:nth-child(2) > ytd-compact-link-renderer:nth-child(5) > a:nth-child(1) > paper-item:nth-child(1)')

class YoutubeSearcher(object):
    search_bar = (By.XPATH, '//input[@id="search"]')
    search_btn = (By.CSS_SELECTOR, 'yt-icon.ytd-searchbox')
    first_video = (By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
