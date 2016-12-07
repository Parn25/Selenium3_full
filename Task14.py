# -*- coding: utf-8 -*-
#Версия Python 2.7
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@pytest.fixture
def start(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver
def test(start):
    #Открываем стартовую страницу, авторизируемся
    start.get('http://localhost/litecart/admin/login.php')
    start.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[1]/td[2]/span/input').send_keys('admin')
    start.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[2]/td[2]/span/input').send_keys('admin')
    start.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button').click()
    #Открываем меню Countries и первую страну в списке
    start.find_element_by_css_selector('#box-apps-menu li:nth-child(3)').click()
    start.find_element_by_css_selector('table.dataTable tr.row td:nth-child(5) a').click()
    all_link = start.find_elements_by_css_selector('#content > form a:not([id="address-format-hint"])')#Находим все ссылки на стрнице в соотвествии с заданием
    #Итерируемся по ссылкам
    for lk in all_link:
        mn_win = start.current_window_handle #Запоминаем заголовок текущего окна(стартового)
        all_old_win = start.window_handles #Сохраняем заголовки  всех открытых окон
        lk.click()#Кликаем по ссылке
        #Проверяем открылась ли новое окно
        new_win_hn = []
        while (new_win_hn == []):
            all_win = start.window_handles #Запоминаем загаловки всех открытых окон
            new_win_hn = (list(set(all_win) - set(all_old_win))) #Находим заголовок открытого окна. Из множества зоголовков открытых окон(после lk.click()) вычетаем множество заголовков ранее открытых окон(до lk.click())
        start.switch_to.window(new_win_hn[0])#  Переключаемся на новое открытое окно
        WebDriverWait(start,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'body')))#Дожидаемся пока откроется содержимое страницы
        start.close()#Закрываем новое окно
        start.switch_to.window(mn_win)# Переключаемся на стартовое
