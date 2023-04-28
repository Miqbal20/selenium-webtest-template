import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://www.saucedemo.com/'


class TestAuthentication(unittest.TestCase):
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=s)

    def test_login(self):
        # Init
        driver = self.browser
        driver.get(link)
        driver.maximize_window()

        # Wait for initialize, in seconds
        wait = WebDriverWait(driver, 10)
        try:
            element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login_logo")))
            time.sleep(3)
        except ValueError:
            driver.quit()

        # Verify by element
        response_data = driver.find_element(By.CLASS_NAME, "login_logo").text
        self.assertEqual('Swag Labs', response_data)

        # Verify bu status code
        response_data = requests.get(link).status_code
        self.assertEqual(200, response_data)

        # Verify by URL
        response_data = driver.current_url
        self.assertEqual(link, response_data)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
