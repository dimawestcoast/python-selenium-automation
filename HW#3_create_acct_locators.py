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

driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&mobileBrowserWeblabTreatment=C&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Ftag%3Damazusnavi-20%26hvadid%3D616931945677%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D13176129676939902981%26hvpone%3D%26hvptwo%3D%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9011786%26hvtargid%3Dkwd-10573980%26ref%3Dnav_ya_signin%26hydadcr%3D28883_14649097&prevRID=X285TCYX78JE8A8568P1&openid.assoc_handle=usflex&openid.mode=checkid_setup&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
#Amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')
#Create account text
driver.find_element(By.CSS_SELECTOR, '.a-spacing-small')
#Your name text box
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
#Email text box
driver.find_element(By.CSS_SELECTOR, '#ap_email')
#password text box
driver.find_element(By.CSS_SELECTOR, '#ap_password')
#password requirement text
driver.find_element(By.CSS_SELECTOR, ".a-box.a-alert-inline.a-alert-inline-info.[aria-live='polite']")
#contidition of use link
driver.find_element(By.CSS_SELECTOR, '[href*="ap_register_notification_condition_of_use"]')
#privacy notice
driver.find_element(By.CSS_SELECTOR, '[href*="ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496"]')
#sign in link
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis[href*='/ap/signin?openid.pape.max_auth_age=0&openid']")


