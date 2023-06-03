from selenium.webdriver.common.by import By

from driver import Driver


class BasePageWithDriver:

    def __init__(self):
        self._driver = Driver.get_chrom_driver()

class LoginPage(BasePageWithDriver):

    def __init__(self):
        super().__init__()
        self._sign_in_button = None
        self._email_field = None
        self._password_field = None
        self._login_button = None
        self._email_incorrect_alert = None
        self._remember_me_button = None
        self._wrong_user_alert = None

    def get_sign_in_button(self):
        self._sign_in_button = self._driver.find_element(By.XPATH, "//button[text()='Sign In']")
        return self._sign_in_button

    def get_email_field(self):
        self._email_field = self._driver.find_element(By.ID, "signinEmail")
        return self._email_field

    def get_password_field(self):
        self._password_field = self._driver.find_element(By.ID, "signinPassword")
        return self._password_field

    def get_login_button(self):
        self._login_button = self._driver.find_element(By.XPATH, "//button[text()='Login']")
        return self._login_button

    def get_remember_me_button(self):
        self._remember_me_button = self._driver.find_element(By.ID, "remember")
        return self._remember_me_button
