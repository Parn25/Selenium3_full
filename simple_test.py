# -*- coding: utf-8 -*-
#Версия Python 2.7
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random, string
import time


driver = webdriver.Chrome()
driver.get('http://localhost/litecart/admin/login.php')
driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[1]/td[2]/span/input').send_keys('admin')
driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[2]/td[2]/span/input').send_keys('admin')
#Открываем страницу добавления нового продукта
driver.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button').click()
driver.find_element_by_css_selector('#box-apps-menu li:nth-child(2)').click()
before_check = driver.find_elements_by_css_selector('table.dataTable > tbody > tr.row [name*="products"]')#Подсчитываем сколько товаров отображается на странице до добавления нового
#Зпонлняем вкладку General
driver.find_element_by_css_selector('#content > div:nth-child(3) > a:nth-child(2)').click()
driver.find_element_by_css_selector('#tab-general input[name="status"][value="1"]').click()#Отмечаем товар как доступный
driver.find_element_by_css_selector('#tab-general input[name="name[en]"]').send_keys("Good duck")#Вводим наименование товара
driver.find_element_by_css_selector('#tab-general input[name="code"]').send_keys("25")#Вводим код продукта
driver.find_element_by_css_selector('#tab-general input[name="product_groups[]"][value="1-3"]').click()#Указываем группу
driver.find_element_by_css_selector('#tab-general input[name="quantity"]').clear() #Добавляем поле Quantity
driver.find_element_by_css_selector('#tab-general input[name="quantity"]').send_keys("5")
driver.find_element_by_css_selector('#tab-general input[name="new_images[]"]').send_keys('C:\duck.png') #Добавляем картинку
driver.find_element_by_css_selector('#tab-general > table > tbody > tr:nth-child(10) > td > input[type="date"]').send_keys('10.06.2017')
driver.find_element_by_css_selector('#tab-general > table > tbody > tr:nth-child(11) > td > input[type="date"]').send_keys('10.08.2017')
#Заполняем вкладку Information
driver.find_element_by_css_selector('#content > form > div > ul > li:nth-child(2) > a').click()
Select(driver.find_element_by_css_selector('#tab-information > table > tbody > tr:nth-child(1) > td > select')).select_by_visible_text('ACME Corp.')#Выбираем производителя поле Manufacturer
driver.find_element_by_css_selector('#tab-information > table > tbody > tr:nth-child(3) > td > input[type="text"]').send_keys('Duck')#Заполняем поле Keywords
driver.find_element_by_css_selector('#tab-information > table > tbody > tr:nth-child(4) > td > span > input[type="text"]').send_keys('Duck')#Заполняем поле Short Description
driver.find_element_by_css_selector('#tab-information > table > tbody > tr:nth-child(5) > td > span > div > div.trumbowyg-editor').send_keys('Good duck') #Заполняем поле Description
driver.find_element_by_css_selector('#tab-information > table > tbody > tr:nth-child(6) > td > span > input[type="text"]').send_keys('Good duck')#Заполняем поле Head Title
driver.find_element_by_css_selector('#tab-information > table > tbody > tr:nth-child(7) > td > span > input[type="text"]').send_keys('Good duck')#Заполняем поле Meta Description
#Заполняем вкладку Price
driver.find_element_by_css_selector('#content > form > div > ul > li:nth-child(4) > a').click()
driver.find_element_by_css_selector('#tab-prices > table:nth-child(2) > tbody > tr > td > input[type="number"]').send_keys('25')#Заполняем поле Purchase Price
Select(driver.find_element_by_css_selector('#tab-prices > table:nth-child(2) > tbody > tr > td > select')).select_by_visible_text('US Dollars') #Выбираем валюту
driver.find_element_by_css_selector('#tab-prices > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(1) > span > input[type="text"]').send_keys('26') #Заполняем поле Price
driver.find_element_by_css_selector('#content > form > p > span > button:nth-child(1)').click()
#Проверям добавился продукт или нет
afte_check=driver.find_elements_by_css_selector('table.dataTable > tbody > tr.row [name*="products"]')
print len(before_check), len(afte_check)
#tab-information > table > tbody > tr:nth-child(3) > td > input[type="text"]