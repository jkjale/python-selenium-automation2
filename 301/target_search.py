from selenium import webdriver
from selenium.webdriver import Keys
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
driver.get('https://www.target.com/')

# Wait for the page to load completely
WebDriverWait(driver, 10).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

input_field = driver.find_element(By.ID, "search")

item = 'soap'

input_field.send_keys(item)

input_field.send_keys(Keys.RETURN)

results_num = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@data-test='lp-resultsCount']/h2/span"))
)
assert 'result' in results_num.text.strip(), 'Number of results is not displayed!!'

results_category = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']/span")
assert item in results_category.text.strip(), 'Searched category is not displayed!!'

sleep(2)

driver.quit()