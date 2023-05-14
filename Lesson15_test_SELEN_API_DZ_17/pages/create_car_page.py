from selenium.webdriver.common.by import By
# from base_page_with_driver import BasePageWithDriver

from driver import Driver


class BasePageWithDriver:
    def __init__(self):
        self._driver = Driver.get_chrom_driver()


class CreateCarPage(BasePageWithDriver):
    def __init__(self):
        super().__init__()
        self._create_car_button = None
        self._brand_field = None
        self._model_field = None
        self._mileage_field = None
        self._get_add_car_header = None
        self._get_add_button = None
        self._get_edit_button = None
        self._get_save_button = None
        self._get_remove_button = None
        self._get_update_car = None
        self._get_brand_value_porsh = None
        self._get_ampty_garage = None

    def get_create_car_button(self):
        self._create_car_button = self._driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        return self._create_car_button

    def get_brand_field(self):
        self._brand_field = self._driver.find_element(By.XPATH, "//select[@id='addCarBrand']")
        return self._brand_field

    def get_model_field(self):
        self._model_field = self._driver.find_element(By.XPATH, "//select[@id='addCarModel']")
        return self._model_field

    def get_mileage_field(self):
        self._mileage_field = self._driver.find_element(By.XPATH, "//input[@id='addCarMileage']")
        return self._mileage_field

    def get_add_car_header(self):
        self._get_add_car_header = self._driver.find_element(By.XPATH, "//div[@class='modal-header']")
        return self._get_add_car_header

    def get_update_car(self):
        self._get_update_car = self._driver.find_element(By.XPATH, "//p[@class='car_update-mileage']")
        return self._get_update_car

    def get_add_button(self):
        self._get_add_button = self._driver.find_element(By.XPATH, "//*[text()='Add']")
        return self._get_add_button

    def get_edit_button(self):
        self._get_edit_button = \
            self._driver.find_element(By.XPATH, "(//button[@class='car_edit btn btn-edit'])[1]")
        return self._get_edit_button

    def get_save_button(self):
        self._get_save_button = self._driver.find_element(By.XPATH, "//*[text()='Save']")
        return self._get_save_button

    def get_remove_button(self):
        self._get_remove_button = self._driver.find_element(By.XPATH, "//*[text()='Remove car']")
        return self._get_remove_button

    def get_model_car(self):
        self._get_model_car = self._driver.find_element(By.XPATH, "(//p[@class='car_name h2'])[1]")
        return self._get_model_car

    def get_remove_finish_button(self):
        self._get_remove_finish_button = self._driver.find_element(By.XPATH, "//*[text()='Remove']")
        return self._get_remove_finish_button

    def get_ampty_garage(self):
        self._get_ampty_garage = self._driver.find_element(By.XPATH,
                                                           "//*[text()='You don’t have any cars in your garage']")
        return self._get_ampty_garage

    def get_brand_value_porsh(self):
        self._get_brand_value_porsh = self._driver.find_element(By.XPATH, "//*[text()='Porsche']")
        return self._get_brand_value_porsh