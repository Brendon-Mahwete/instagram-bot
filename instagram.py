from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = r"C:\Users\MBmah\OneDrive\Documents\chromedriver_win32\chromedriver.exe"
SIMILAR_ACCOUNT = "w3schools.com_official"
FB_EMAIL = "email@gmail.co"
FB_PASSWORD = "***************"
URL = "https://www.instagram.com/"

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(URL)

time.sleep(5)

# -------------------------------------------Logging in------------------------------------------------------------
"""Logging in via facebook, ensure that you have logged in with facebook before and verified that you are not a robot
and that you are able to log in to facebook on chrome without entering your details."""

log_in = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[5]/button')
log_in.click()

time.sleep(5)

facebook_email = driver.find_element(By.NAME, "email")
facebook_password = driver.find_element(By.NAME, "pass")
facebook_email.send_keys(FB_EMAIL)
facebook_password.send_keys(FB_PASSWORD)
facebook_password.send_keys(Keys.ENTER)

time.sleep(5)

# This finds the notification pop up and clicks the not now button
# A while loop is used as depending on the device it may take longer to load the page
while True:
    try:
        turn_off_notifications = driver.find_element(By.CSS_SELECTOR, "button._a9_1")
        turn_off_notifications.click()
        break
    except selenium.common.exceptions.NoSuchElementException:
        print("Finding the notification button")

# -----------------------------------Finding the similar account and getting followers--------------------------

# Searching for the account
search_bar = driver.find_element(By.CLASS_NAME, "_aauy")
search_bar.send_keys(SIMILAR_ACCOUNT)

time.sleep(3)

# Clicking on the account that was searched
first_profile = driver.find_element(By.CLASS_NAME, "_abm4")
first_profile.click()

time.sleep(5)

# Clicking on the followers
followers = driver.find_element(By.CSS_SELECTOR, "a")
followers.click()
time.sleep(5)

# Scrolling down on the popup of followers
popup = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div['
                                      '2]/div/div/div/div/div[2]/div/div/div[2]')
for i in range(2):
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', popup)
    time.sleep(2)

time.sleep(5)

# Getting the 'Follow' button on the followers popup and clicking on all the follow buttons that it finds
followers_list = driver.find_elements(By.CSS_SELECTOR, "button")
for follower in followers_list:
    if follower.text == "Follow":
        follower.click()
