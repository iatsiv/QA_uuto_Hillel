class LocatorsConstants:
    URL = 'https://admin-demo.nopcommerce.com/'
    URL_AFTER_AUTH = 'https://admin-demo.nopcommerce.com/admin/'
    INPUT_EMAIL = '//*[@id="Email"]'
    INPUT_PASSWORD = '//*[@id="Password"]'
    BUTTON_LOGIN = '//button[@class="button-1 login-button"]'
    LOGIN_EMAIL = 'admin@yourstore.com'
    LOGIN_BAD_EMAIL = 'a@re.com'
    PASSWORD = 'admin'
    USER_NAME_IN_HEADER = '//a[text()="John Smith"]'
    CONTENT_HEADER = '//div[@class="content-header"]'
    ERROR_TEXT = '//*[text()="No customer account found"]'






    ACCEPT_LICENCE_XPATH = "//*[text()='Zaakceptuj wszystko']"
    SEARCH_FIELD_XPATH = "//*[@title='Szukaj']"
    SEARCH_BUTTON_XPATH = "//div[@class='FPdoLc lJ9FBc']//input[@value='Szukaj w Google']"
    GOOGLE_ICO_XPATH = "//img[@class='jfN4p']"

        # driver.find_element(By.XPATH, "//*[@title='Szukaj']").send_keys(123)
        # driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@value='Szukaj w Google']").click()
        # google_ico = driver.find_element(By.XPATH, "//img[@class='jfN4p']")