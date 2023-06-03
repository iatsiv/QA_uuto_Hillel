from pages.login_page import LoginPage
from pages.create_car_page import CreateCarPage


class FacadeBase:
    def __init__(self):
        self._login_page = LoginPage()
        self._create_car_page = CreateCarPage()
