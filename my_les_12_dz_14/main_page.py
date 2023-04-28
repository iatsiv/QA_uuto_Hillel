from button import Button
from selenium.webdriver.common.by import By
from base_page import BasePage


class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        self.__auth_button: Button = None

    def get_auth_button(self):
        self.__auth_button = Button(self._driver.find_element(By.XPATH, '//button[@class="button-1 login-button"]'))
        return self.__auth_button
