import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxServices
from webdriver_manager.firefox import GeckoDriverManager
from config.data_common import info_common


class BaseTest(unittest.TestCase):
    def setUp(self):
        options = FirefoxOptions()
        self.driver: webdriver.Remote = webdriver.Firefox(service=FirefoxServices(GeckoDriverManager().install()),
                                                          options=options)

        self.driver.get(info_common.enviroment)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        if self is not None:
            self.driver.close()
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
