# -*- coding: utf-8 -*-
#Версия Python 2.7
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
wd = webdriver.Chrome()
wd.get('http://localhost/litecart/en/')
product_1 = wd.find_elements_by_css_selector('li.product')
for pr in product_1:
    if  pr.find_element_by_css_selector('a div.name').get_attribute('textContent') == "Yellow Duck":
        pr.find_element_by_css_selector('a.link').click()
        Select(wd.find_element_by_css_selector('div.information select')).select_by_visible_text('Small')
        after_prop_1 = wd.find_element_by_css_selector('#cart > a.content > span.quantity').get_attribute('textContent')
        wd.find_element_by_css_selector('td.quantity button').click()
        WebDriverWait(wd, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart > a.content > span.quantity"),str(int(after_prop_1)+1)))
        break

wd.back()
product_2 = wd.find_elements_by_css_selector('li.product')
for pr2 in product_2:
    if  pr2.find_element_by_css_selector('a div.name').get_attribute('textContent') == "Blue Duck":
        pr2.find_element_by_css_selector('a.link').click()
        after_prop_12 = wd.find_element_by_css_selector('#cart > a.content > span.quantity').get_attribute('textContent')
        wd.find_element_by_css_selector('td.quantity button').click()
        WebDriverWait(wd, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart > a.content > span.quantity"),str(int(after_prop_12)+1)))
        break

wd.back()
product_3 = wd.find_elements_by_css_selector('li.product')
for pr3 in product_3:
    if  pr3.find_element_by_css_selector('a div.name').get_attribute('textContent') == "Green Duck":
        pr3.find_element_by_css_selector('a.link').click()
        after_prop_13 = wd.find_element_by_css_selector('#cart > a.content > span.quantity').get_attribute('textContent')
        wd.find_element_by_css_selector('td.quantity button').click()
        WebDriverWait(wd, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart > a.content > span.quantity"),str(int(after_prop_13)+1)))
        break


wd.find_element_by_css_selector('#cart > a.link').click()
all_product_order=wd.find_elements_by_css_selector('li.item')
ft=[ str(li_num) for li_num in range(1,len(all_product_order)+1)]
ft.reverse()
for rd in ft:
    if rd == '2': wd.find_element_by_css_selector('#box-checkout-cart > ul > li:nth-child(2) > a').click()
    WebDriverWait(wd,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.item:nth-child('+rd+') button[value="Remove"]'))).click()
    rd_1=str(int(rd)+1)
    WebDriverWait(wd,10).until(EC.invisibility_of_element_located((By.XPATH,'//*[@id="order_confirmation-wrapper"]/table/tbody/tr['+rd_1+']/td[3]')))


