"""
Write a test to log in on the website https://admin-demo.nopcommerce.com/

Credentials:

Login - admin@yourstore.com
Password - admin
Enter the login and password fields and click the login button.
Check that login was successful
"""


from selenium.webdriver.common.by import By
from locators_constants import LocatorsConstants
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver


def test_auth_positive():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(LocatorsConstants.URL)
    driver.find_element(By.XPATH, LocatorsConstants.INPUT_EMAIL).clear()
    driver.find_element(By.XPATH, LocatorsConstants.INPUT_EMAIL)\
        .send_keys(LocatorsConstants.LOGIN_EMAIL)
    driver.find_element(By.XPATH, LocatorsConstants.INPUT_PASSWORD).clear()
    driver.find_element(By.XPATH, LocatorsConstants.INPUT_PASSWORD)\
        .send_keys(LocatorsConstants.PASSWORD)
    driver.find_element(By.XPATH, LocatorsConstants.BUTTON_LOGIN).click()
    content_header = driver.find_element(By.XPATH,
                                         LocatorsConstants.CONTENT_HEADER)
    user_name_in_header = \
        driver.find_element(By.XPATH, LocatorsConstants.USER_NAME_IN_HEADER)

    assert driver.current_url == LocatorsConstants.URL_AFTER_AUTH, "bad url"
    assert content_header.is_displayed(), "content-header not found"
    assert user_name_in_header.is_displayed(),  "user name wrong or not found"


def test_auth_negative():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(LocatorsConstants.URL)
    driver.find_element(By.XPATH, LocatorsConstants.INPUT_EMAIL).clear()
    driver.find_element(By.XPATH, LocatorsConstants.INPUT_EMAIL)\
        .send_keys(LocatorsConstants.LOGIN_BAD_EMAIL)
    driver.find_element(By.XPATH, LocatorsConstants.INPUT_PASSWORD).clear()
    driver.find_element(By.XPATH, LocatorsConstants.INPUT_PASSWORD)\
        .send_keys(LocatorsConstants.PASSWORD)
    driver.find_element(By.XPATH, LocatorsConstants.BUTTON_LOGIN).click()
    error_text = driver.find_element(By.XPATH, LocatorsConstants.ERROR_TEXT)

    assert error_text.is_displayed(), "error text not displayed or changed"
