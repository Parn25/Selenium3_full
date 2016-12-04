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
    start.get('http://localhost/litecart/en/')
    product_1 = start.find_elements_by_css_selector('li.product')
    #Добавляем желтую утку в карзину
    for pr in product_1:
        if pr.find_element_by_css_selector('a div.name').get_attribute('textContent') == "Yellow Duck":#Нохид на стартовой страницы нужную утку
            pr.find_element_by_css_selector('a.link').click()#Кликаем на нее
            Select(start.find_element_by_css_selector('div.information select')).select_by_visible_text('Small')#У желтой утки выбераем размер
            after_prop_1 = start.find_element_by_css_selector('#cart > a.content > span.quantity').get_attribute('textContent')#Запоминаем сколько товаров лежит в карзине
            start.find_element_by_css_selector('td.quantity button').click()#Добавляем утку в карзину
            WebDriverWait(start, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart > a.content > span.quantity"),str(int(after_prop_1) + 1)))#Ждем пока утка добавиться в карзину
            break
#Возвращаемся на стартовую страницу и добавляем вторую  голубую утку
    start.back()
    product_2 = start.find_elements_by_css_selector('li.product')
    for pr2 in product_2:
        if pr2.find_element_by_css_selector('a div.name').get_attribute('textContent') == "Blue Duck":
            pr2.find_element_by_css_selector('a.link').click()
            after_prop_12 = start.find_element_by_css_selector('#cart > a.content > span.quantity').get_attribute('textContent')
            start.find_element_by_css_selector('td.quantity button').click()
            WebDriverWait(start, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart > a.content > span.quantity"),str(int(after_prop_12) + 1)))
            break
#Возвращаемся на стартовую страницу и добавляем третью  зеленую утку
    start.back()
    product_3 = start.find_elements_by_css_selector('li.product')
    for pr3 in product_3:
        if pr3.find_element_by_css_selector('a div.name').get_attribute('textContent') == "Green Duck":
            pr3.find_element_by_css_selector('a.link').click()
            after_prop_13 = start.find_element_by_css_selector('#cart > a.content > span.quantity').get_attribute('textContent')
            start.find_element_by_css_selector('td.quantity button').click()
            WebDriverWait(start, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart > a.content > span.quantity"),str(int(after_prop_13) + 1)))
            break
#Переходим в корзину и удаляем товар
    start.find_element_by_css_selector('#cart > a.link').click()
    all_product_order = start.find_elements_by_css_selector('li.item')
    ft = [str(li_num) for li_num in range(1, len(all_product_order) + 1)]
    ft.reverse()
    for rd in ft:
        if rd == '2': start.find_element_by_css_selector('#box-checkout-cart > ul > li:nth-child(2) > a').click()#После удаления одного товара товары не переключаются. Возможно дефект.
        WebDriverWait(start, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.item:nth-child(' + rd + ') button[value="Remove"]'))).click()#Дожидаемся когда появится нужный нам товар и удаляем его
        rd_1 = str(int(rd) + 1)
        WebDriverWait(start, 10).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="order_confirmation-wrapper"]/table/tbody/tr[' + rd_1 + ']/td[3]')))#Дожидаемся пока обновится таблтца внизу

