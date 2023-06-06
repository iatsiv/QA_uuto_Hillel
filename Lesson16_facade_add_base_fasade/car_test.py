import requests
import time

from user_login import UserLogin
from user_register import UserRegister
from users_constants import UsersConstants
from create_car import CraeteCar
from driver import Driver
from pages.create_car_page import CreateCarPage
from pages.login_page import LoginPage
from test_base import TestBase



class TestAuth(TestBase):

    def setup_class(self):
        self.driver = None
        self.create_car_page = CreateCarPage()
        self.login_page = LoginPage()
        self.driver = Driver.get_chrom_driver()
        self.driver.implicitly_wait(10)
        self.session = requests.session()
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        user_register = UserRegister(UsersConstants.NAME, UsersConstants.LAST_NAME, UsersConstants.LOGIN_EMAIL_SETUP,
                                     UsersConstants.PASSWORD, UsersConstants.PASSWORD)
        self.session.post(url=UsersConstants.URL_SIGNUP, json=user_register.__dict__)
        self.login_user = UserLogin(UsersConstants.LOGIN_EMAIL_SETUP, UsersConstants.PASSWORD, False)
        self.session.post(url=UsersConstants.URL_SIGNIN, json=self.login_user.__dict__)
        self.login_page.get_sign_in_button().click()
        self.login_facade.set_email_and_password_and_click_login_button(UsersConstants.LOGIN_EMAIL_SETUP, UsersConstants.PASSWORD)

    def setup_method(self):
        self.create_car = CraeteCar(UsersConstants.BRAND_ID, UsersConstants.MODEL_ID, UsersConstants.MILEAGE_SETUP)
        self.session.post(url=UsersConstants.URL_CREATE_CAR, json=self.create_car.__dict__)

    def test_car_create(self):
        time.sleep(1)
        self.driver.get(UsersConstants.URL_GARAGE)
        self.create_car_page.get_create_car_button().click()
        time.sleep(1)
        assert self.create_car_page.get_add_car_header().is_displayed()
        self.create_car_facade.set_mileage_and_click(UsersConstants.MILEAGE)
        time.sleep(1)
        assert self.create_car_page.get_update_car().is_displayed()

    def test_car_edit(self):
        assert self.create_car_page.get_model_car().text == 'Audi TT', "delete current user and repeat"
        self.create_car_page.get_edit_button().click()
        time.sleep(1)
        self.create_car_facade.set_fields_on_create_car_page_and_save_changes()
        assert self.create_car_page.get_model_car().text == 'Porsche 911'

    def test_car_delete(self):
        self.create_car_facade.remove_one_car()
        self.create_car_facade.remove_one_car()
        self.create_car_page.get_ampty_garage().is_displayed()

    def teardown_class(self):
        self.login_user = UserLogin(UsersConstants.LOGIN_EMAIL_SETUP, UsersConstants.PASSWORD, False)
        self.session.post(url=UsersConstants.URL_SIGNIN, json=self.login_user.__dict__)
        self.session.delete(UsersConstants.URL_DEL_USERS).json()
