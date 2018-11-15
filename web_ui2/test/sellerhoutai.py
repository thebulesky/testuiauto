# -*- coding: utf8 -*-
from selenium import webdriver
import time
from config.sellerconfig import *
from tools.tools_ui import *
def openchrame ():
    s = webdriver.Chrome()
    s.get(openurl)
    #log.DEBUG("打开浏览器地址%s"%openurl)
def openshangpin(driver):
    #fxpath_click(driver,"/html/body/div[2]/div/div/ul/li[2]/a")
    fxpath(driver,zhucaidan["shangpin"])
    #log.info("打开商品菜单")
    fxpath_click(driver,shangpins["guanli"])
    #log.info("打开菜单商品管理")

def openorder(driver):
    fxpath(driver,zhucaidan["jiaoyi"])
    #log.info("打开交易菜单")
    fxpath_click(driver,dingdan["dingdan"])
    #log.info("打开菜单订单管理")


def fabushagnpin(driver):
    fid_click(driver, "/html/body/div[9]/div/div[2]/div/div[1]/div/div/div[2]/button")
    fid_vals(driver, "ProductName", "uiziodnghua" + str(int(time.time())) [-4:])
    fid_click(driver, "ProductCategory")
    fxpath_click(driver, "/html/body/div[8]/div/div/div/ul[1]/li[5]")
    fxpath_click(driver, "/html/body/div[8]/div/div/div/ul[2]/li[1]")
    fxpath_click(driver, "/html/body/div[8]/div/div/div/ul[3]/li[1]")
    fxpath_click(driver,"/html/body/div[3]/div/div[1]/div/div[2]/div/div[1]/div[2]/form/div/div[3]/div/div[2]/div/div[""1]/input")
    fxpath_click(driver,"/html/body/div[3]/div/div[1]/div/div[2]/div/div[1]/div[2]/form/div/div[3]/div/div[2]/div/div[""1]/div/div[1]")
    fxpath_click(driver,"/html/body/div[3]/div/div[1]/div/div[2]/div/div[1]/div[3]/form/div/div/div/div[2]/div/div[1]/div[""1]/div[4]/label")
    fxpath_vals(driver,"/html/body/div[3]/div/div[1]/div/div[2]/div/div[1]/div[3]/form/div/div/div/div[2]/div/div[1]/div[""1]/div[4]/label","C:\\Users\Public\Pictures\Sample Pictures\菊花.jpg")
    fid_vals(driver, "productDetailDesc", "dasfasdfasdfasdfsdfasdfasdf")
    fid_vals(driver, "fPrice_SELFDEFINE-1", 100)
    fid_vals(driver, "Num_SELFDEFINE-1", 100)
    fid_click(driver,"/html/body/div[3]/div/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div[" "1]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]/div/label/span[1]/input")
    fid_click(driver,"/html/body/div[3]/div/div[1]/div/div[2]/div/div[4]/div/form/div[2]/div[1]/div/div[2]/div/div[2]/label[""2]/span[1]/input")
    fid_click(driver, "/html/body/div[3]/div/div[1]/div/div[2]/div/div[4]/div/form/div[3]/div/button[1]")
    driver.switch_to_alert().accept()
    time.sleep(2)
def login(driver):
    fid_vals(driver,"loginName",data["loginName"])
    fid_vals(driver,"loginPwd",data["loginPwd"])
    fid_click(driver,"btnSubmit")
    #log.info("登陆成功账号:%s"%data["loginName"]+"密码：%s"%data["loginPwd"])
