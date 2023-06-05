import allure
from pages.login_page import LoginPage

class LoginFacade:
    def __init__(self):
        self.login_page = LoginPage()

    @allure.step("Fill email and password fields")
    def set_email_and_password(self, email, password):
        self.login_page.get_email_field().send_keys(email)
        self.login_page.get_password_field().send_keys(password)

    @allure.step("Fill email and password fields and click login button")
    def set_email_and_password_and_click_login_button(self, email, password):
        self.set_email_and_password(email, password)
        self.login_page.get_remember_me_button().click()
        self.login_page.get_login_button().click()
