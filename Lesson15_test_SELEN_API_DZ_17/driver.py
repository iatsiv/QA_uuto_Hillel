from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    driver = None

    @staticmethod
    def get_chrom_driver() -> WebDriver:
        if Driver.driver is None:
            Driver.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            Driver.driver.implicitly_wait(10)
            return Driver.driver
        else:
            return Driver.driver

    @staticmethod
    def quit_chrome_driver():
        Driver.driver.quit()
