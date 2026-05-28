from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def open(self, url):
        self.driver.get(url)
        
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
        
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        
    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)
        
    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False