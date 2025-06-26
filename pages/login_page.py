from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "uid")))
        self.driver.find_element(By.NAME, "uid").send_keys(username)
        self.driver.find_element(By.NAME, "passw").send_keys(password)
        self.driver.find_element(By.NAME, "btnSubmit").click()
