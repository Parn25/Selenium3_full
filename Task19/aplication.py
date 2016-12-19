# -*- coding: utf-8 -*-
#Версия Python 2.7
from cart_page import CartPage
from product_page import ProductPage
from selenium import webdriver
from start_page import StartPage

#Класс добавления продукта
class Aplication:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.start_pg = StartPage(self.driver)
        self.product_pg = ProductPage(self.driver)
        self.cart_pg = CartPage(self.driver)

    def quit(self):
        self.driver.quit()

    def st_open(self):
        self.start_pg.op_start()

    def add_duck(self,dk_s):
        self.start_pg.find_duck(dk_s)
        self.product_pg.add_duck_pg(dk_s)
        self.product_pg.go_start()

    def d_all_duck(self):
        self.start_pg.go_cart()
        self.cart_pg.dl_dick()

