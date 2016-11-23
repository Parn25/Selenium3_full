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
        start.get('http://localhost/litecart/admin/login.php')
        start.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[1]/td[2]/span/input').send_keys('admin')
        start.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[2]/td[2]/span/input').send_keys('admin')
        start.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button').click()
        """Находим все пункт меню"""
        all_link = start.find_elements_by_css_selector('#box-apps-menu li')
        """Подсчитываем их количество"""
        l=0
        for el in all_link:
            l+=1
        """Кликаем по родительскому пункту меню"""
        for li_web in [ str(li_num) for li_num in range(1,l+1)]:
            link_st='//*[@id="box-apps-menu"]/li['+li_web+']'
            start.find_element_by_xpath(link_st).click()
            """Проверям заголовок у родительского пункта меню"""
            try:
                start.find_element_by_xpath('//*[@id="content"]/h1/span')
            except NoSuchElementException:
                start.quit()
            """Получаем список дочерних пунктов меню"""
            dt_li=start.find_elements_by_xpath(link_st+'/ul/li')
            """Если есть дочернии пункты меню кликаем по ним"""
            if dt_li != []:
                """Подсчитываем количестов дочерних пунктов меню"""
                d=0
                for er in dt_li:
                    d += 1
                """Кликаем по дочерним пунктам меню"""
                for dt_clik in [ str(li_num1) for li_num1 in range(1,d+1)]:
                    start.find_element_by_xpath(link_st+'/ul/li['+dt_clik+']').click()
                    """Проверяем заголовок дочерних пунктов меню"""
                    try:
                        start.find_element_by_xpath('//*[@id="content"]/h1/span')
                    except NoSuchElementException:
                        start.quit()




