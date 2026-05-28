import pytest
from pages.dashboard_page import DashboardPage

class TestDashboard:
    def test_logout(self, driver, login_page):
        # 1. Pastikan user login terlebih dahulu
        login_page.login('tomsmith', 'SuperSecretPassword!')
        assert login_page.is_login_successful(), 'Login valid harus berhasil'
        # 2. Verifikasi user berhasil masuk ke Dashboard
        dashboard = DashboardPage(driver)
        assert dashboard.is_on_dashboard(), 'User harusnya berada di Dashboard'
        # 3. Eksekusi fungsi logout
        dashboard.logout()
        # 4. Verifikasi user kembali ke halaman login
        assert login_page.is_visible(login_page.LOGIN_BTN), 'User harus kembali ke halaman login setelah logout'
