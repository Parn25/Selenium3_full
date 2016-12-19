# -*- coding: utf-8 -*-
#Версия Python 2.7
from selenium.webdriver.support.wait import WebDriverWait
#Класс для работы со стартовой страницей
class StartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    #Модуль открытия стартовой страницы
    def op_start(self):
        self.driver.get('http://localhost/litecart/en/')
    #Модуль поиска нужного товара
    def find_duck(self,dk):
        product_1 = self.driver.find_elements_by_css_selector('li.product')
        # Находим нужную нам утку и кликаем на нее
        for pr in product_1:
                if pr.find_element_by_css_selector('a div.name').get_attribute('textContent') == dk:  # Нохидим на стартовой страницы нужную утку
                    pr.find_element_by_css_selector('a.link').click()
                    break
    #Модуль перехода со стартовой страницы в корзину
    def go_cart(self):
        self.driver.find_element_by_css_selector('#cart > a.link').click()