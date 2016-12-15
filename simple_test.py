# -*- coding: utf-8 -*-
#Версия Python 2.7
import pytest
from selenium import webdriver
import copy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('http://localhost/litecart/admin/login.php')
driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[1]/td[2]/span/input').send_keys('admin')
driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[2]/td[2]/span/input').send_keys('admin')
driver.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button').click()
driver.find_element_by_css_selector('#box-apps-menu li:nth-child(3)').click()
driver.find_element_by_css_selector('table.dataTable tr.row td:nth-child(5) a').click()
#tl=driver.find_element_by_css_selector('head > title').get_attribute('title')
#print tl
all_link = driver.find_elements_by_css_selector('#content > form a:not([id="address-format-hint"])')
for lk in all_link:
    mn_win = driver.current_window_handle
    all_old_win = driver.window_handles
    lk.click()
    all_win = driver.window_handles
    new_win_hn=list(set(all_win) - set(all_old_win))
    WebDriverWait(driver, 10).until(EC.new_window_is_opened(new_win_hn))
    print driver.current_window_handle
    driver.switch_to.window(new_win_hn[0])
    print driver.current_window_handle
    driver.close()
    driver.switch_to.window(mn_win)
    print driver.current_window_handle


