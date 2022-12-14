from selenium.webdriver.common.by import By

class LoginPage():
    SignInWithGoogle_Xpath = "//a[text()='Sign in with Google']"
    Username_Id = "txtUsername"
    Password_Id = "txtPassword"
    Login_btn_xpath = "//*[text()='Login ']"

    def __init__(self, driver):
        self.driver = driver

    def get_login_page_title(self):
        return self.driver.title

    def is_signinWithGoogle_exists(self):
        element=self.driver.find_element(By.XPATH, self.SignInWithGoogle_Xpath)
        return bool(element)

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.Username_Id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.Password_Id).send_keys(password)

    def clickOnLoginBtn(self):
        self.driver.find_element(By.XPATH, self.Login_btn_xpath).click()

    def do_login(self,username,password):
        self.setUserName(username)
        self.setPassword(password)
        self.clickOnLoginBtn()


