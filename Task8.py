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
        most_all=start.find_elements_by_css_selector('#box-most-popular li')
        sticker_most=start.find_elements_by_css_selector("#box-most-popular div.sticker")
        l = 0
        for el in most_all:
            l += 1
        for li_web in [str(li_num) for li_num in range(1, l + 1)]:
            try:
                st=start.find_element_by_xpath('//*[@id="box-most-popular"]/div/ul/li['+li_web+']/a[1]/div[1]/div').get_attribute('class')
            except NoSuchElementException:
                start.quit()
