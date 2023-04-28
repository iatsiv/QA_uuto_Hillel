from driver import Driver
from main_page import MainPage


class TestAuth:

    def setup_class(self):
        self.driver = Driver.get_chrom_driver()
        self.main_page = MainPage()

    def setup_method(self):
        self.driver.get("https://admin-demo.nopcommerce.com/")

    def test_auth_positive(self):
        self.main_page.get_auth_button().click()
        assert self.driver.current_url == 'https://admin-demo.nopcommerce.com/admin/', "bad url"

    @staticmethod
    def teardown_class():
        Driver.quit_chrome_driver()
