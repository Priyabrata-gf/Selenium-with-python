from selenium import webdriver
class login:
    textbox_username_ID = "Email"
    textbox_Password_ID = "Password"
    Button_Login_Class = "ico-login"
    Link_Logout_Linktext = "/logout"

    def __init__(self,driver):
        self.driver=driver
    def username(self,username):
        self.driver.find_element_by_id(self.textbox_username_ID).clear()
        self.driver.find_element_by_id(self.textbox_username_ID).send_keys(username)
    def password(self,password):
        self.driver.find_element_by_id(self.textbox_Password_ID).clear()
        self.driver.find_element_by_id(self.textbox_Password_ID).send_keys(password)
    def clickLogin(self):
        self.driver.find_element_by_class_name(self.Button_Login_Class).click()






