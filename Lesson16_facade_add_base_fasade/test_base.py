from facade.login_facade import LoginFacade
from facade.create_car_facade import CreateCarFacade

class TestBase:
    def __init__(self):
        self.login_facade = LoginFacade()
        self.create_car_facade = CreateCarFacade
