# -- coding: utf-8 --
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from dslO2O.testCase.util.MysqlUtil import MyMySQL
# from dslO2O.testCase.util.Sql import getGoodNoSql


class myUnit(unittest.TestCase):
    driver = webdriver.Firefox()


    # @classmethod
    # def setUpClass(cls,driver=driver):
    def setUp(self):
        #浏览器
        print('setUpClass正在执行...')
        print("setUp执行url为%s"%self.driver.current_url)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()


    # @classmethod
    # def tearDownClass(cls):
    def tearDown(self):
        print("tearDownClass执行完毕！")
        # cls.driver.close()



if __name__ == '__main__':
    unittest.main()
