import pytest
import csv
import os

# Fungsi untuk membaca file CSV
def load_csv(filename):
    filepath = os.path.join('data', filename)
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

class TestRegisterDDT:
    # Memasukkan data CSV ke dalam parameter test
    @pytest.mark.parametrize('row', load_csv('register_data.csv'))
    def test_register_from_csv(self, driver, row):
        # Asumsi menginisialisasi RegisterPage
        page = RegisterPage(driver)
        
        # Eksekusi langkah registrasi menggunakan data dari CSV
        page.register(row['username'], row['email'], row['password'])
        
        # Validasi berdasarkan kolom 'expected' di CSV
        if row['expected'] == 'PASS':
            assert page.is_register_successful(), f"Test Gagal: {row['description']}"
        else:
            assert page.is_register_failed(), f"Test Gagal: {row['description']}"