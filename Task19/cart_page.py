# -*- coding: utf-8 -*-
#Версия Python 2.7
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def dl_dick(self):
        all_product_order = self.driver.find_elements_by_css_selector('li.item')
        ft = [str(li_num) for li_num in range(1, len(all_product_order) + 1)]
        ft.reverse()
        for rd in ft:
            if rd == '2': self.driver.find_element_by_css_selector('#box-checkout-cart > ul > li:nth-child(2) > a').click()#После удаления одного товара товары не переключаются. Возможно дефект.
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.item:nth-child(' + rd + ') button[value="Remove"]'))).click()#Дожидаемся когда появится нужный нам товар и удаляем его
            rd_1 = str(int(rd) + 1)
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="order_confirmation-wrapper"]/table/tbody/tr[' + rd_1 + ']/td[3]')))#Дожидаемся пока обновится таблица внизу
