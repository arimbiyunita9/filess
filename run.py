from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
DesiredCapabilities
import string
import time
import json

chrome_options = ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--no-sandbox")

class TestUntitled():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    def teardown_method(self, method):
        self.driver.quit()
  
with open("email.txt", "r") as file:
    credential_list = file.readlines()
    for credential in credential_list:
        credentials = credential.strip().split(",")
        if len(credentials) == 2:
            username, password = credentials
            
        else:
            print(f"Kesalahan: {credential} tidak memiliki format yang benar")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://studiolab.sagemaker.aws/login")

        email_input = driver.find_element(By.NAME, "username")
        email_input.send_keys(username)

        password_input = driver.find_element(by=By.XPATH, value="//div[2]/div/div/div/input")
        password_input.send_keys(password)

        driver.find_element(By.CSS_SELECTOR, ".qa-signin-submit-button > .MuiButton-label").click()
        element = driver.find_element(By.CSS_SELECTOR, "body")

        time.sleep(10)
        
        actions = ActionChains(driver)
        element = driver.find_element(By.CSS_SELECTOR, ".qa-start-stop-button")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        driver.find_element(By.CSS_SELECTOR, ".qa-start-stop-button").click()
        time.sleep(60)
        driver.find_element(By.CSS_SELECTOR, ".qa-launch-project-button > .MuiButton-label").click()
        time.sleep(30)

driver.quit()
