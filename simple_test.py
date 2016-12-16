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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# enable browser logging
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(desired_capabilities=d)
driver.get('http://localhost/litecart/admin/login.php')
driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[1]/td[2]/span/input').send_keys('admin')
driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[2]/td[2]/span/input').send_keys('admin')
driver.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button').click()
driver.find_element_by_css_selector('#box-apps-menu li:nth-child(2)').click()
tov = driver.find_elements_by_css_selector('form[name="catalog_form"] tr.row')
for y in tov:
    nm = y.find_element_by_css_selector('td:nth-child(1)').get_attribute('innerHTML')
    fgbnm
    if nm == 'categories[1]':
        y.click()
        for jk in driver.find_elements_by_css_selector('form[name="catalog_form"] tr.row input'):
            print jk.get_attribute('name')

for l in driver.get_log('browser'):
    print l
driver.quit()