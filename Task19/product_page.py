# -*- coding: utf-8 -*-
#Версия Python 2.7
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
#Класс для работы со страницей продукта
class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    #Модуль добаления продуктов
    def add_duck_pg(self,dk_p):
        if dk_p == "Yellow Duck": Select(self.driver.find_element_by_css_selector('div.information select')).select_by_visible_text('Small')
        after_prop_1 = self.driver.find_element_by_css_selector('#cart > a.content > span.quantity').get_attribute('textContent')  # Запоминаем сколько товаров лежит в карзине
        self.driver.find_element_by_css_selector('td.quantity button').click()  # Добавляем утку в карзину
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart > a.content > span.quantity"),str(int(after_prop_1) + 1)))  # Ждем пока утка добавиться в карзину
    #Возращение на предыдущую страницу
    def go_start(self):
        self.driver.back()
