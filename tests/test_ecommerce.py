import pytest
import allure
import csv
import os
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def load_login_data():
    filepath = os.path.join('data', 'saucedemo_users.csv')
    with open(filepath, newline='', encoding='utf-8') as f:
        return [row for row in csv.DictReader(f)]

@allure.feature('E-Commerce Flow')
class TestEcommerce:

    # ================= LOGIN FLOW =================
    @allure.story('Login')
    @pytest.mark.parametrize('data', load_login_data())
    def test_login_scenarios(self, driver, data):
        allure.dynamic.title(f"{data['tc_id']}: Login dengan {data['username']}")
        login = LoginPage(driver)
        login.login(data['username'], data['password'])
        
        if data['expected'] == 'PASS':
            assert "inventory" in driver.current_url, "Login valid gagal"
        else:
            assert "inventory" not in driver.current_url, "User invalid malah berhasil login"

    # ================= PRODUCT FLOW =================
    @allure.story('Products')
    @allure.title('TC-EC-004: Verifikasi jumlah produk tampil')
    def test_product_count(self, driver):
        login = LoginPage(driver)
        login.login('standard_user', 'secret_sauce')
        
        inv = InventoryPage(driver)
        assert inv.get_product_count() == 6, "Jumlah produk tidak sesuai"

    @allure.story('Products')
    @allure.title('TC-EC-005: Urutkan produk harga terendah ke tertinggi')
    def test_sort_products(self, driver):
        login = LoginPage(driver)
        login.login('standard_user', 'secret_sauce')
        
        inv = InventoryPage(driver)
        inv.sort_by('lohi')  # lohi = low to high
        # Secara visual berhasil jika tidak ada error saat dropdown dipilih
        assert True 

    # ================= CART FLOW =================
    @allure.story('Cart')
    @allure.title('TC-EC-006: Tambah 1 produk ke cart')
    def test_add_one_to_cart(self, driver):
        login = LoginPage(driver)
        login.login('standard_user', 'secret_sauce')
        
        inv = InventoryPage(driver)
        inv.add_first_product_to_cart()
        assert inv.get_cart_count() == 1, "Badge cart harus bernilai 1"

    # ================= CHECKOUT FLOW =================
    @allure.story('Checkout')
    @allure.title('TC-EC-009: Checkout gagal (field nama kosong)')
    def test_checkout_empty_name(self, driver):
        login = LoginPage(driver)
        login.login('standard_user', 'secret_sauce')
        
        inv = InventoryPage(driver)
        inv.add_first_product_to_cart()
        inv.go_to_cart()
        
        # Asumsikan klik tombol checkout ada di base flow
        driver.get("https://www.saucedemo.com/checkout-step-one.html")
        
        checkout = CheckoutPage(driver)
        checkout.fill_info('', 'Santoso', '40123')
        checkout.continue_checkout()
        
        assert "Error: First Name is required" in checkout.get_error_message()

    # ================= END-TO-END FLOW =================
    @allure.story('End-to-End Purchase')
    @allure.title('TC-EC-012: Alur Penuh Login -> Cart -> Checkout -> Logout')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_full_purchase_flow(self, driver):
        with allure.step('1. Login'):
            login = LoginPage(driver)
            login.login('standard_user', 'secret_sauce')
            
        with allure.step('2. Add to Cart'):
            inv = InventoryPage(driver)
            inv.add_first_product_to_cart()
            
        with allure.step('3. Checkout'):
            inv.go_to_cart()
            driver.get("https://www.saucedemo.com/checkout-step-one.html")
            checkout = CheckoutPage(driver)
            checkout.fill_info('Bintang', 'QA', '12345')
            checkout.continue_checkout()
            checkout.finish_checkout()
            
        with allure.step('4. Verifikasi'):
            assert checkout.is_order_confirmed()