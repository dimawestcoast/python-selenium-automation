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

#By ID (ID's are fast)
driver.find_element(By.ID,'twotabsearchtextbox')

#By XPATH
#Tag and attribute
driver.find_element(By.XPATH, "//a[@data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
#multiple attributes
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_bestsellers']")
#by Text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
#combo
driver.find_element(By.XPATH, "//a[text()='Best Sellers'and @class='nav-a']")

driver.find_element()