import pytest

from pages.homepage import HomePage
from pages.loginpage import LoginPage
from utilities.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestHomePage():

    def test_home_page(self):
        lp=LoginPage(self.driver)
        lp.do_login(ReadConfig.getUserName(),ReadConfig.getPassword())
        hp=HomePage(self.driver)
        assert hp.is_hometab_exists()==True
        assert hp.is_attendancetab_exists()==True
        assert hp.get_CurrentDate()=="14-12-2022"
        assert hp.verify_background_color_of_current_date()=="#ffef8f"




