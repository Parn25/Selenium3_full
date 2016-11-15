import pytest
from selenium import webdriver

def test():
    driver = webdriver.Chrome()
    driver.get('https://mail.ru/')
    driver.quit()

