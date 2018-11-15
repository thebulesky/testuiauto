# -*- coding: utf8 -*-

from test.sellerhoutai import *
from time import sleep
import unittest
from tools import HTMLTestRunner
class seller(unittest.TestCase):
    def setUp(cls):
        cls.driver = openchrame()
        cls.driver.maximize_window()
        login(cls.driver)
        cls.timeout=30

    def testshop(cls):
        driver=cls.driver
        openshangpin(driver)
    def testjiaoyi(cls):
        driver=cls.driver
        openorder(driver)
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    report = 'E:\\web_ui2\\report\\report.html'
    file_result = open(report,'wb')
    st = unittest.TestSuite()
    st.addTest(seller("testshop"))
    st.addTest(seller('testjiaoyi'))
    #file_path = "F:\\RobotTest\\result.html"
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title='My Report')
    runner.run(st)

