from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AttendancePage:

    Attendance_Tab_Xpath="//*[text()='Attendance']"
    My_Records_Xpath="//*[text()='My Records']"
    Attendancepage_logo_Xpath="//*[contains(@src,'cropped-synerzip-logo-with-Inc5000.png')]"
    Attendancepage_Hiring_Xpath="//*[contains(@src, 'hiring_icon.png')]"
    From_Calendar_Xpath=""
    From_Date_Month_Xpath=""
    From_Date_Year_Xpath=""
    To_Calendar_Xpath = ""
    To_Date_Month_Xpath = ""
    To_Date_Year_Xpath = ""




    def __init__(self,driver):
        self.driver=driver

    def click_on_attendance_tab(self):
        attendance_tab=self.driver.find_element(By.XPATH, self.Attendance_Tab_Xpath)
        my_records=self.driver.find_element(By.XPATH, self.My_Records_Xpath)
        actions=ActionChains(self.driver)
        actions.move_to_element(attendance_tab).click().perform()
        actions.move_to_element(my_records).click().perform()

    def verify_logo_with_INC5000_on_performancepage(self):
        AttendancepageLogo_element = self.driver.find_element(By.XPATH, self.Attendancepage_logo_Xpath)
        return bool(AttendancepageLogo_element)

    def verify_hiring_logo_on_performancepage(self):
        AttendancepageHiringLogo_element = self.driver.find_element(By.XPATH, self.Attendancepage_Hiring_Xpath)
        return bool(AttendancepageHiringLogo_element)

    def select_from_date_to_check_attendance_record(self):
        self.driver.find_element(By.XPATH, self.From_Calendar_Xpath).click()
        month_from=self.driver.find_element(By.XPATH, self.From_Date_Month_Xpath)
        year_from=self.driver.find_element(By.XPATH, self.From_Date_Year_Xpath)
        month_ele_from=Select(month_from)
        month_ele_from.select_by_visible_text("Jul")
        year_ele_from = Select(year_from)
        year_ele_from.select_by_visible_text("2022")




    def select_to_date_to_check_attendance_record(self):
        pass

