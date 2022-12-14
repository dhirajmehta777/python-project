import pytest

from pages.loginpage import LoginPage
from utilities.readproperties import ReadConfig


@pytest.mark.usefixtures("setup")
class TestLoginPage():

    def test_login_page(self):
        lp=LoginPage(self.driver)
        actual_title=lp.get_login_page_title()
        if actual_title == "SYNERZIP":
            assert True
        else:
            self.driver.save_screenshot(".//screenshots//" + "login_Page_title.png")
            assert False
        assert lp.is_signinWithGoogle_exists()==True
        lp.do_login(ReadConfig.getUserName(),ReadConfig.getPassword())