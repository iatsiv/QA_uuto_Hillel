
import requests

from user_login import UserLogin
from user_register import UserRegister
from constants import Constants


class TestAuth:
    def setup_class(self):
        self.session = requests.session()
        user_register = UserRegister(Constants.NAME, Constants.LAST_NAME, Constants.LOGIN_EMAIL_SETUP,
                                     Constants.PASSWORD, Constants.PASSWORD)
        self.session.post(url=Constants.URL_SIGNUP, json=user_register.__dict__)

    def setup_method(self):
        self.login_user = UserLogin(Constants.LOGIN_EMAIL_SETUP, Constants.PASSWORD, False)
        self.session.post(url=Constants.URL_SIGNIN, json=self.login_user.__dict__)

    def test_user_register(self):
        user_register = UserRegister(Constants.NAME, Constants.LAST_NAME, Constants.LOGIN_EMAIL_TEST,
                                     Constants.PASSWORD, Constants.PASSWORD)
        result = self.session.post(url=Constants.URL_SIGNUP, json=user_register.__dict__)
        assert result.status_code == 201, "Unexpected status code"
        assert result.json()["status"] == "ok", "problem with registration"

    def test_registration_failure(self):
        user_register = UserRegister(Constants.NAME, Constants.LAST_NAME, Constants.LOGIN_EMAIL_SETUP,
                                     Constants.PASSWORD, Constants.PASSWORD)
        result = self.session.post(url=Constants.URL_SIGNUP, json=user_register.__dict__)
        assert result.status_code == 400, "Unexpected status code"
        assert result.json()["status"] == "error"
        assert result.json()["message"] == "User already exists"


    def test_user_login(self):
        self.session.get(Constants.URL_LOGOUT)
        result = self.session.post(url=Constants.URL_SIGNIN, json=self.login_user.__dict__)
        assert result.status_code == 200, "Unexpected status code"
        assert result.json()["status"] == "ok", "problem with login"

    def test_user_chek(self):
        result = self.session.get(url=Constants.URL_PROFILE)
        assert result.status_code == 200, "Unexpected status code"
        assert result.json()["status"] == "ok", "problem with user chek"
        assert result.json()["data"]["name"] == Constants.NAME, "problem with user chek, wrong name"
        assert result.json()["data"]["lastName"] == Constants.LAST_NAME, "problem with user chek, wrong lastName"

    def teardown_method(self):
        self.session.get(Constants.URL_LOGOUT)

    def teardown_class(self):
        self.login_user = UserLogin(Constants.LOGIN_EMAIL_SETUP, Constants.PASSWORD, False)
        self.session.post(url=Constants.URL_SIGNIN, json=self.login_user.__dict__)
        self.session.delete(Constants.URL_DEL_USERS).json()
        self.login_user = UserLogin(Constants.LOGIN_EMAIL_TEST, Constants.PASSWORD, False)
        self.session.post(url=Constants.URL_SIGNIN, json=self.login_user.__dict__)
        self.session.delete(Constants.URL_DEL_USERS).json()
