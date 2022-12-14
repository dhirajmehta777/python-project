import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utilities.readproperties import ReadConfig


@pytest.fixture(scope="class")
def setup(request):
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(ReadConfig.getApplicationURL())
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
