import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAuth(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_Register(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("dummy")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("dummy@dummy.com")
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("dummy123")
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(1)
        
    def test_b_Login_valid(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("dummy@dummy.com")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("dummy123")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_c_Login_email_invalid(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("dummy2@dummy.com")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("dummy123")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
    
    def test_d_Login_password_invalid(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("dummy@dummy.com")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("dummy1234")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_e_Login_data_kosong(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()