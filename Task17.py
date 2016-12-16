# -*- coding: utf-8 -*-
#Версия Python 2.7
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def start(request):
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities=d)
    request.addfinalizer(driver.quit)
    return driver
def test(start):
    start.get('http://localhost/litecart/admin/login.php')
    start.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[1]/td[2]/span/input').send_keys('admin')
    start.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[2]/td[2]/span/input').send_keys('admin')
    start.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button').click()
    start.find_element_by_css_selector('#box-apps-menu li:nth-child(2)').click()
    #Открываем категории если они присуствую на странице
    tov = start.find_elements_by_css_selector('form[name="catalog_form"] tr.row')
    for y in tov:
        nm = y.find_element_by_css_selector('td:nth-child(1)').get_attribute('innerHTML')
        if 'categories' in nm:
            y.find_element_by_css_selector('a').click()
    #После открытия страница находим все товары на странице
    tov_after = start.find_elements_by_css_selector('form[name="catalog_form"] tr.row')
    ln_l = []
    for d in tov_after:
        if 'products' in d.find_element_by_css_selector('td:nth-child(1)').get_attribute('innerHTML'):
            ln_l.append(d.find_element_by_css_selector('a').get_attribute('href'))#Считываем ссылки все товаров
    #Последовательно открываем страницы и проверям есть ли сообщения
    for f in ln_l:
        start.get(f)
        for i in start.get_log('browser'):
            assert i.get(u'level')!=''
