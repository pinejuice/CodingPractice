import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver_path = 'driver/93.0.4577.63/chromedriver.exe'

class TestSele(unittest.TestCase):
    def setUp(self):
        """各試験ケースごとに呼び出される前処理
        """
        pass

    @classmethod
    def setUpClass(self):
        """試験実施時に1回だけ呼び出される前処理
        """
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("enable-automation")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # CLIでの実行の場合は必須
        # options.add_argument("--headless")
        # Driverのバージョンに指定がある場合
        # self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        # Driverのバージョンが最新でOKな場合
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)
        
    def tearDown(self):
        """各試験ケースごとに呼び出される後処理
        """
        pass

    @classmethod
    def tearDownClass(self):
        """試験実施時に1回だけ呼び出される後処理
        """
        self.driver.quit()
        
    def test_01(self):
        """試験ケース
        """
        self.driver.get('https://www.google.com')
        self.assertEqual(self.driver.current_url, 'https://www.google.com')

if __name__ == '__main__':
    unittest.main()
    