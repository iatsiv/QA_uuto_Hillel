import allure
from pages.create_car_page import CreateCarPage
import time

class CreateCarFacade:
    def __init__(self):
        self.create_car_page = CreateCarPage()

    @allure.step("Fill mileage and click")
    def set_mileage_and_click(self, mileage):
        self.create_car_page.get_mileage_field().send_keys(mileage)
        self.create_car_page.get_add_button().click()

    @allure.step("Set_fields_on_create_car_page_and_save_changes")
    def set_fields_on_create_car_page_and_save_changes(self):
        self.create_car_page.get_brand_field().click()
        self.create_car_page.get_brand_value_porsh().click()
        self.create_car_page.get_save_button().click()

    @allure.step("Remove car")
    def remove_one_car(self):
        self.create_car_page.get_edit_button().click()
        time.sleep(1)
        self.create_car_page.get_remove_button().click()
        time.sleep(1)
        self.create_car_page.get_remove_finish_button().click()
        time.sleep(1)
