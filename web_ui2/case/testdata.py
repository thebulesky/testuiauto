#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '
import urllib3
import requests
__author__ = 'hualai yu'

import unittest
#from methon.TestResult.common import RunMethod


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_02(cls)
    def test_02(cls):
        data1={
            "token":"fasdfasdfasd",
            "uid": 4789654
        }
        token=data1["token"]
        uid=data1["uid"]
        cls.token1=token
        cls.userId1=uid
        print(data1,"data1")
    def test03(cls):
        token2=cls.token1+"123"
        uid2=cls.userId1+123
        data2 = {
            "access_token": token2,
            "userId": uid2
        }
        print(data2,"data2")


if __name__ == '__main__':

    suit=unittest.TestSuite()
    suit.addTest("test_02")
    suit.addTest("test_03")
    runner=unittest.TextTestRunner()
    runner.run(suit)
    #test = Test()
    #test1 = test.test_01()
    #test.test_02(test1["token"], test1["uid"])