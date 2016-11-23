import pytest
from selenium import webdriver

def test():
    driver = webdriver.Firefox("C:/bin1/chromedriver_win32")
    driver.get('https://mail.ru/')
    driver.quit()

