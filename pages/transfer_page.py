from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransferPage:
    def __init__(self, driver):
        self.driver = driver

    def transfer_funds(self, amount):
        self.driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "transferAmount"))
        )
        self.driver.find_element(By.NAME, "transferAmount").send_keys(amount)
        self.driver.find_element(By.NAME, "fromAccount").send_keys("800000")
        self.driver.find_element(By.NAME, "toAccount").send_keys("800001")
        self.driver.find_element(By.NAME, "transfer").click()

    def verify_success(self):
        return "was successful" in self.driver.page_source
