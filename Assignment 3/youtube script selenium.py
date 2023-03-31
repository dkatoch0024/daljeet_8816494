# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

driver.get("https://www.youtube.com/")
time.sleep(3)

youtube_search_bar = driver.find_element("name", "search_query")
youtube_search_bar.send_keys("apple 14")
youtube_search_bar.send_keys(Keys.RETURN)
time.sleep(5)
assert "apple 14" in driver.title

filter_button = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div/div/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
filter_button.click()
time.sleep(5)

filter_select_button = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div/iron-collapse/div/ytd-search-filter-group-renderer[1]/ytd-search-filter-renderer[5]/a/div/yt-formatted-string")
filter_select_button.click()
time.sleep(5)

video_link = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
video_link.click()
time.sleep(30)

Home_page = driver.find_element("xpath", "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[1]/ytd-topbar-logo-renderer/a/div/ytd-logo/yt-icon")
Home_page.click()
time.sleep(5)

driver.close()
