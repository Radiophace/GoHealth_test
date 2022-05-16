import time
from selenium import webdriver
from selenium.webdriver import Chrome 

#browser = webdriver.Chrome('/Users/serj/Coding/chromedriver/chromedriver')

def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(0.3)

browser = Chrome()
browser.get('https://www.browserstack.com')
button = browser.find_element_by_id('signupModalButton')
time.sleep(1)
button.click()

time.sleep(2)

button = browser.find_element_by_id('accept-cookie-notification-cross-icon')
button.click()

name = browser.find_element_by_id('user_full_name')

slow_typing(name, 'John Doe')

submit_button = browser.find_element_by_id('user_submit')
submit_button.click()

#browser.close()


