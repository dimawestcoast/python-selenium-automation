from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

# css selectors
# by Class
driver.find_element(By.CSS_SELECTOR, '.nav-input.nav-progressive-attribute')
driver.find_element(By.CSS_SELECTOR, '.nav-input')

# by ID
driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button')
#by ID +class
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')
#By ID + Class + tag
driver.find_element(By.CSS_SELECTOR, 'input#nav-search-submit-button.nav-progressive-attribute.nav-input')

#By ID and Class
driver.find_element(By.CSS_SELECTOR, '.nav-input#nav-search-submit-button')

# by other attribute
driver.find_element(By.CSS_SELECTOR, "[aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[type='text'][name='field-keywords']")

# By class + other attributes
driver.find_element(By.CSS_SELECTOR, ".nav-input[type='text'][name='field-keywords']")
# By partial attribute
driver.find_element(By.CSS_SELECTOR, '[href*="ap_signin_notification_condition_of_use"]')
# By parent - child element
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='condition_of_use']")


