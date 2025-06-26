from pages.login_page import LoginPage
from pages.transfer_page import TransferPage

def test_login_and_transfer(driver):
    login = LoginPage(driver)
    login.login("admin", "admin")

    transfer = TransferPage(driver)
    transfer.transfer_funds("100")

    assert transfer.verify_success()
