from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.amazon.com/')
actions = ActionChains(driver)

WebDriverWait(driver, 10).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)
signin_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#nav-link-accountList"))
)
actions.move_to_element(signin_dropdown).perform()
driver.find_element(By.CSS_SELECTOR, "#nav-flyout-ya-signin span").click()
create_account_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#createAccountSubmit"))
)
create_account_button.click()
create_account_page_header = driver.find_element(By.CSS_SELECTOR, ".a-box-inner > h1").text
assert create_account_page_header.strip().lower() == 'create account'
assert 'register' in driver.current_url



amazon_logo = driver.find_element(By.CSS_SELECTOR, ".a-link-nav-icon > i")
create_account_div_header = driver.find_element(By.CSS_SELECTOR, ".a-box-inner > h1").text
name_field = driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
email_field = driver.find_element(By.CSS_SELECTOR, "#ap_email")
pw_field = driver.find_element(By.CSS_SELECTOR, "#ap_password")
pw_alert = driver.find_element(By.CSS_SELECTOR, "#auth-password-requirement-info .a-alert-content").text
reenter_password_field = driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
conditions_of_use_link = driver.find_element(By.CSS_SELECTOR, "#legalTextRow > a:nth-child(1)").get_attribute("href")
privacy_notice_link = driver.find_element(By.CSS_SELECTOR, "#legalTextRow > a:nth-child(2)").get_attribute("href")
sign_in_link = driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis").get_attribute("href")



assert amazon_logo.is_displayed(), "Logo is not displayed on the page"
assert create_account_div_header.strip().lower() == "create account", "'Create Account' header is missing"
assert name_field.is_displayed(), "Name fiels is not displayed on the page"
assert email_field.is_displayed(), "Email fields is not displayed on the page"
assert pw_field.is_displayed(), "Password fields is not displayed on the page"
assert pw_alert.strip().lower() == "passwords must be at least 6 characters.", "Password alert is missing"
assert reenter_password_field.is_displayed(), "Reenter password fields is not displayed on the page"
assert continue_button.is_displayed(), "Continue button is not displayed on the page"
assert "condition" in conditions_of_use_link.strip().lower(), "Condition link is broken"
assert "privacy" in privacy_notice_link.strip().lower(), "Privacy notice link is broken"
assert "signin" in sign_in_link.strip().lower(), "Sign in link is broken"


driver.quit()