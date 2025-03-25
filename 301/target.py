from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# Wait for the page to load completely
WebDriverWait(driver, 10).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

signin_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "account-sign-in"))
)
signin_dropdown.click()

side_nav = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='ModalDrawer']/div/div"))
)

signin_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='accountNav-signIn']"))
)
signin_button.click()

signin_title = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@id='__next']/div/div/div/div/div/h1/span"))
)
assert signin_title.text == "Sign into your Target account", 'Signin title not found!!!'

signin_with_pw_button = driver.find_element(By.ID, "login")
assert signin_with_pw_button is not None, "Signin-with-pw button was not found!"

driver.quit()