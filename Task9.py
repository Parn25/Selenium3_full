# -*- coding: utf-8 -*-
#Версия Python 2.7
import pytest
from selenium import webdriver
import copy
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
        #Проверяем отсортированы ли страны в меню Countries. Получаем список всех стран из меню Countries
        start.find_element_by_css_selector('#box-apps-menu li:nth-child(3)').click()
        all_counters=start.find_elements_by_css_selector('tr.row td:nth-child(5)')
        sp_country=[]
        cp_country=[]
        #Последовательно проходим по всему списку и сохраняем в объект языка Python страны в том порядке, в котором видет пользователь
        for count in all_counters:
            sp_country.append(count.get_attribute("outerText"))
        cp_country=copy.deepcopy(sp_country) #Создаем копию
        cp_country.sort()#Выполянем сортировку скопированного списка стран
        assert sp_country == cp_country #Выполняем проверку
        #Проверяем сортировку зон у стран  где они присутствую. Находим на странице все страны.
        all_zone = start.find_elements_by_css_selector('tr.row')
        link_count = []
        #Для каждой из стрна находим элемент, который показывает сколько зон в стране. Получаем атрибут количество зон и если количество зон не равно 0 копируем WEB ссылку этой сттраны.
        for count_zone in all_zone:
            if count_zone.find_element_by_css_selector("td:nth-child(6)").get_attribute("outerText") != '0':
                lk = count_zone.find_element_by_css_selector("td:nth-child(5) a").get_attribute("href")
                link_count.append(lk)
        #В браузере открываем WEB страницы найденых стран и проверяем сартировку зон
        for o_link in link_count:
            start.get(o_link)
            tr_zone = []
            cp_tr_zone = []
            lt_zone = start.find_elements_by_css_selector('#table-zones tr > td > input[type="hidden"][name*="[name]"]')
            for t in [str(zone_num) for zone_num in range(2, len(lt_zone) + 2)]:
                l = '//*[@id="table-zones"]/tbody/tr[' + t + ']/td[3]'
                tr_zone.append(start.find_element_by_xpath(l).get_attribute("textContent"))
            cp_tr_zone=copy.deepcopy(tr_zone)
            cp_tr_zone.sort()
            assert tr_zone==cp_tr_zone
        #Проверям сортировку зон стран, расположенных в меню GeoZone. Открываем меню Geo Zone и находим все страны расположенные на этой странице.
        start.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')
        zone_edit = start.find_elements_by_css_selector('tr.row td:nth-child(3) a')#Из свойст получаем ссылку на страницу каждой страны.
        lk = []
        for op_link in zone_edit:
            lk.append(op_link.get_attribute('href'))
        #Открываем WEB страницу страны. Проверям сортировку списка зон страны.
        for O in lk:
            start.get(O)
            zone = start.find_elements_by_css_selector('#table-zones > tbody > tr > td:nth-child(3) > select [selected=selected]')#На открытой WEB странице находми список зон
            code_zone = []
            cp_code_zone=[]
            for I in zone: #Проверяем сортирован ли список зон по алфавиту
                code_zone.append(I.get_attribute('textContent'))
            cp_code_zone=copy.deepcopy(code_zone)
            cp_code_zone.sort()
            assert  code_zone == cp_code_zone



