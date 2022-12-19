import configparser


config=configparser.RawConfigParser()
config.read(".//configurations//config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return  url

    @staticmethod
    def getUserName():
        usr = config.get('common info', 'username')
        return usr

    @staticmethod
    def getPassword():
        pwd = config.get('common info', 'password')
        return pwd

    @staticmethod
    def getInvalidUserName():
        invalidusr = config.get('common info', 'invalidusername')
        return invalidusr

    @staticmethod
    def getInvalidPassword():
        invalidpwd = config.get('common info', 'invalidpassword')
        return invalidpwd

    @staticmethod
    def getExpectedTitleOfPage():
        title = config.get('common info', 'page_title')
        return title

    @staticmethod
    def getExpectedInvaliCredentialMessage():
        message = config.get('common info', 'invalid_message')
        return message

    @staticmethod
    def getExpectedCurrentDate():
        date = config.get('common info', 'current_date')
        return date

    @staticmethod
    def getExpectedBackGroundColor():
        color = config.get('common info', 'calender_bc_color')
        return color

    @staticmethod
    def getExpectedLeaveBalance():
        leave = config.get('common info', 'leave_balance')
        return leave