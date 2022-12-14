from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.support.color import Color

class HomePage:
    HomeTab_Xpath = "//*[text()='Home']"
    Attendance_Xpath="//*[text()='Attendance']"
    current_dt_Xpath="(//*[contains(@class,'ui-state-highlight')])[1]"

    def __init__(self,driver):
        self.driver=driver

    def is_hometab_exists(self):
        Helement=self.driver.find_element(By.XPATH, self.HomeTab_Xpath)
        return bool(Helement)

    def is_attendancetab_exists(self):
        Aelement=self.driver.find_element(By.XPATH, self.Attendance_Xpath)
        return bool(Aelement)

    def get_CurrentDate(self):
        current_dt = datetime.datetime.now()
        return current_dt.strftime("%d-%m-%Y")

    def verify_background_color_of_current_date(self):
        bc_color=self.driver.find_element(By.XPATH, self.current_dt_Xpath).value_of_css_property("background-color")
        hex_bc_color=Color.from_string(bc_color).hex
        return hex_bc_color


