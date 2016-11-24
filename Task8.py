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
        product = start.find_elements_by_css_selector('li.product')#Находми все товары
        for i in product: #Итерируемся по все товарам и проверяем у каждого товара наличие по одному стикеру
            sticker=i.find_elements_by_css_selector('div.sticker')
            assert len(sticker) == 1
