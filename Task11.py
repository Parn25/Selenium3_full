# -*- coding: utf-8 -*-
#Версия Python 2.7
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random, string


@pytest.fixture
def start(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver
def test(start):
    #Создаем пользователя
    start.get('http://localhost/litecart/en/create_account')#Открываем страницу
    start.find_element_by_css_selector('form[name="customer_form"]  input[name="firstname"]').send_keys("Admin")#Вводим имя
    start.find_element_by_css_selector('form[name="customer_form"]  input[name="lastname"]').send_keys("Admin")#Вводим фамилию
    start.find_element_by_css_selector('form[name="customer_form"]  input[name="address1"]').send_keys("Admin")#Вводим адрес
    start.find_element_by_css_selector('form[name="customer_form"]  input[name="postcode"]').send_keys("123456")#Вводим индекс
    start.find_element_by_css_selector('form[name="customer_form"]  input[name="city"').send_keys("Moscow")#Вводим город
    name_mail = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(5))#Генерируем имя для email
    start.find_element_by_css_selector('form[name="customer_form"]  input[name="email"]').send_keys(name_mail + "@y.com")#Вводим email
    start.find_element_by_css_selector('form[name="customer_form"]  input[type="tel"]').send_keys("+71234567890")#Вводим телефон
    start.find_element_by_css_selector('form[name="customer_form"]  input[type="password"]').send_keys("111111")#Вводим пароль
    start.find_element_by_css_selector('form[name="customer_form"]  input[name="confirmed_password"]').send_keys("111111")#Подверждаем пароль
    start.find_element_by_css_selector('#create-account > div > form > table > tbody > tr:nth-child(9) > td > button').click()#Создаем пользователя
    start.find_element_by_css_selector('#box-account > div > ul > li:nth-child(4) > a').click()#Выходим
    #Заходим созданным пользователем
    start.find_element_by_css_selector('#box-account-login > div > form > table > tbody > tr:nth-child(1) > td > input[type="text"]').send_keys(name_mail + "@y.com")
    start.find_element_by_css_selector('#box-account-login > div > form > table > tbody > tr:nth-child(2) > td > input[type="password"]').send_keys("111111")
    start.find_element_by_css_selector('#box-account-login > div > form > table > tbody > tr:nth-child(4) > td > span > button:nth-child(1)').click()
    start.find_element_by_css_selector('#box-account > div > ul > li:nth-child(4) > a').click()
