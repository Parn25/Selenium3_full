# -*- coding: utf-8 -*-
#Версия Python 2.7
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def start(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver
def test(start):
        start.get('http://localhost/litecart/en/')
        most_product = start.find_elements_by_css_selector('#box-most-popular li.product') #Находми все товары в этой секции
        most_sticker = start.find_elements_by_css_selector('#box-most-popular div.sticker') #Находми все стикеры в этой секции
        assert len(most_product) == len(most_sticker) #Если число товаров и стикеров  не совпадает возбуждаем исключение
        #Проверяем секцию Campaigns
        cam_product = start.find_elements_by_css_selector('#box-campaigns li.product')
        cam_sticker= start.find_elements_by_css_selector('#box-campaigns div.sticker')
        assert len(cam_product) == len(cam_sticker)
        #Проверяем секцию Latest Products
        last_product = start.find_elements_by_css_selector('#box-latest-products li.product')
        last_sticker = start.find_elements_by_css_selector('#box-latest-products div.sticker')
        assert len(last_product) == len(last_sticker)