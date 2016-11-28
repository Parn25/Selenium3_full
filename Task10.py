# -*- coding: utf-8 -*-
#Версия Python 2.7
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def start(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver
def test(start):
        start.get('http://localhost/litecart/en/')
        #Получаем необходимые свойства на стартовой странице
        index_li = start.find_element_by_css_selector('#box-campaigns li a.link').get_attribute('href') #Ссылка продукта
        index_name = start.find_element_by_css_selector('#box-campaigns li div.name').get_attribute('textContent') #Имя продукта
        index_p1 = start.find_element_by_css_selector('#box-campaigns li s').get_attribute('textContent') #Цена без скидки
        index_p2 = start.find_element_by_css_selector('#box-campaigns li strong').get_attribute('textContent') #Цена со скидкой
        index_p1css = start.find_element_by_css_selector('#box-campaigns li s').value_of_css_property('color') #Стили цена без скидки
        index_p2css = start.find_element_by_css_selector('#box-campaigns li strong').value_of_css_property('color') #Стили цены со скидкой
        #Открываем страницу продукта
        start.find_element_by_css_selector('#box-campaigns li').click()
        assert index_li == start.find_element_by_css_selector('body').get_attribute('baseURI') #Проверям правильная страница открыта
        product_name = start.find_element_by_css_selector('#box-product > div:nth-child(1) > h1').get_attribute('textContent') #Проверям наименование продукта
        assert index_name == product_name
        product_p1 = start.find_element_by_css_selector('#box-product s.regular-price').get_attribute('textContent')#Сравниваем цены без скидки
        assert index_p1 == product_p1
        product_p2 = start.find_element_by_css_selector('#box-product strong.campaign-price').get_attribute('textContent') #Сравниваем цены со скидкой
        assert index_p2 == product_p2
        product_p1css = start.find_element_by_css_selector('#box-product s.regular-price').value_of_css_property('color') #Сравниваем стили цены без скидки со скидкой
        assert index_p1css == product_p1css
        product_p2csss = start.find_element_by_css_selector('#box-product strong.campaign-price').value_of_css_property('color') #Сравниваем стили цены со скидкой
        assert index_p2css == product_p2csss
