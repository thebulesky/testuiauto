# -*- coding: utf8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from tools.logging import *
log =Log()
def fid(driver,id):
    try:
        driver.find_element_by_id(id)
    except Exception:
        log.error("fid:%s%s"%id)
def fxpath(driver,xpath):
    try:
        click=driver.find_element_by_xpath(xpath)
        ActionChains(driver).move_to_element(click).perform()
    except Exception:
        log.error("fid:%s%s"%id)
def fid_vals(driver,id,name):
    try:
        driver.find_element_by_id(id).send_keys(name)
    except Exception:
        log.error("执行fid失败:%s%s"%id)

def fid_click(driver,id):
    try:
        driver.find_element_by_id(id).click()
    except Exception:
        log.error("执行id_click失败")

def fname_vals(driver,name,vals):
    try:
        driver.find_element_by_name(name).send_keys(vals)
    except Exception:
        log.error("执行fname_click失败")
def fname_click(driver,name):
    try:
        driver.find_element_by_name(name).click()
    except Exception:
        log.error("执行fname_click失败")


def fxpath_click (driver,xpath):
    try:
        driver.find_element_by_xpath(xpath).click()
    except Exception:
        log.error("执行fxpath_click失败")

def fxpath_vals (driver,xpath,vals):
    try:
        driver.find_element_by_xpath(xpath).send_keys(vals)
    except Exception:
        log.error("执行fxpath_vals失败")


def sleept(times):
    if type(times)==str:
        time.sleep(int(times))
    elif type(times)==int:
        time.sleep(times)
    else:
        pass
