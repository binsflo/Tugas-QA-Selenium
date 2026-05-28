from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    # Locator untuk elemen di halaman Dashboard
    LOGOUT_BTN = (By.CSS_SELECTOR, "a.button.secondary.radius") 
    DASHBOARD_HEADER = (By.TAG_NAME, "h2")
    # Method untuk verifikasi apakah user berada di halaman Dashboard
    def is_on_dashboard(self):
        return self.is_visible(self.DASHBOARD_HEADER)
    # Method untuk melakukan aksi klik tombol logout
    def logout(self):
        self.click(self.LOGOUT_BTN)
