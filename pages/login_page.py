from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = 'https://the-internet.herokuapp.com/login'
    
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[type=submit]')
    FLASH_OK = (By.CSS_SELECTOR, '.flash.success')
    
    def login(self, username, password):
        self.open(self.URL)
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        
    def is_login_successful(self):
        return self.is_visible(self.FLASH_OK)