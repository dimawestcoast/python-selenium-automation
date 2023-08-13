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

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

#### 2. Practice with locators.
#Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
#Email field
driver.find_element(By.XPATH, "//input[@type='email']")
#Continue button
driver.find_element(By.ID, 'continue')
#Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
#Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
#Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')
#Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')
#Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

#3. Create a test case for the Sign In page using python & selenium script.
#Test Case: Logged out user sees Sign in page when clicking Orders
#1. Open https://www.amazon.com 2. Click Orders 3. Verify Sign in page opened: Sign In header is visible, email input field is present.
driver.get('https://www.amazon.com')
#click on Orders
driver.find_element(By.ID, "nav-orders").click()
sleep(5)
expected_result = 'Sign in'
actual_results = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result == actual_results, f'Expected{actual_results} but got {expected_result}'
print('Test case Passed')

driver.quit()