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
#input search text
driver.find_element(By.ID,'twotabsearchtextbox').send_keys('table')
#click on search
driver.find_element(By.ID,'nav-search-submit-button').click()
expected_results = '"table"'
actual_results = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_results == actual_results
print('Test case passed')