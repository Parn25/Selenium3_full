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
    start = webdriver.Chrome()
    start.get('http://localhost/litecart/admin/login.php')
    start.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[1]/td[2]/span/input').send_keys('admin')
    start.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[2]/td[2]/span/input').send_keys('admin')
    start.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button').click()
    start.find_element_by_css_selector('#box-apps-menu li:nth-child(3)').click()
    start.find_element_by_css_selector('table.dataTable tr.row td:nth-child(5) a').click()
    all_link = start.find_elements_by_css_selector('#content > form a:not([id="address-format-hint"])')
    for lk in all_link:
        mn_win = start.current_window_handle
        all_old_win = start.window_handles
        lk.click()
        all_win = start.window_handles
        new_win_hn=list(set(all_win) - set(all_old_win))
        print start.current_window_handle
        start.switch_to.window(new_win_hn[0])
        WebDriverWait(start,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'body')))
        print start.current_window_handle
        start.close()
        start.switch_to.window(mn_win)
        print start.current_window_handle