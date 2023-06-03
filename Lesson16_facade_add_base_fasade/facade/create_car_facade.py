import time
import allure
from facade_base import FacadeBase


class CreateCarFacade(FacadeBase):
    def __init__(self):
        super().__init__()

    @allure.step("Fill mileage and click")
    def set_mileage_and_click(self, mileage):
        self._create_car_page.get_mileage_field().send_keys(mileage)
        self._create_car_page.get_add_button().click()

    @allure.step("Set_fields_on_create_car_page_and_save_changes")
    def set_fields_on_create_car_page_and_save_changes(self):
        self._create_car_page.get_brand_field().click()
        self._create_car_page.get_brand_value_porsh().click()
        self._create_car_page.get_save_button().click()

    @allure.step("Remove car")
    def remove_one_car(self):
        self._create_car_page.get_edit_button().click()
        time.sleep(1)
        self._create_car_page.get_remove_button().click()
        time.sleep(1)
        self._create_car_page.get_remove_finish_button().click()
        time.sleep(1)
