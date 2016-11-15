import pytest
from selenium import webdriver


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


