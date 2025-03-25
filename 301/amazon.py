from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Wait for the page to load completely
WebDriverWait(driver, 10).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

signin_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "nav-link-accountList"))
)

actions = ActionChains(driver)
actions.move_to_element(signin_dropdown).perform()

signin_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='nav-flyout-ya-signin']/a"))
)
signin_button.click()

sleep(2)

def test_form():
    amazon_logo = driver.find_element(By.XPATH, "//a[@aria-label='www.amazon.com']/i")
    assert amazon_logo is not None, 'The Amazon logo is missing!!'

    email_field = driver.find_element(By.ID, "ap_email")
    assert email_field is not None, 'Email field is missing!!'

    continue_button = driver.find_element(By.ID, "continue-announce")
    assert continue_button.text == 'Continue', 'Button text is not "Continue"!!'

    conditions_link = driver.find_element(By.XPATH, "//div[@id='legalTextRow']/a[1]")
    assert conditions_link.text == 'Conditions of Use', 'Link text is not "Conditions of Use"!!'

    privacy_link = driver.find_element(By.XPATH, "//div[@id='legalTextRow']/a[2]")
    assert privacy_link.text == 'Privacy Notice', 'Link text is not "Privacy Notice"!!'

    needhelp_link = driver.find_element(By.XPATH, "//div[@class='a-section']/div/a/span")
    assert needhelp_link.text == 'Need help?', 'Link text is not "Need help?"!!'

    needhelp_link.click()

    sleep(1)

    forgotpw_link = driver.find_element(By.ID, "auth-fpp-link-bottom")
    assert forgotpw_link.text == 'Forgot your password?', 'Link text is not "Forgot your password?"!!'

    otherissues_link = driver.find_element(By.ID, "ap-other-signin-issues-link")
    assert otherissues_link.text == 'Other issues with Sign-In', 'Link text is not "Other issues with Sign-In"!!'

    createaccount_button = driver.find_element(By.ID, "createAccountSubmit")
    assert createaccount_button.text == 'Create your Amazon account', 'Button text is not "Create your Amazon account"!!'

test_form()

driver.quit()