from selenium import webdriver
import time
class Add_Customer:
    txt_AdminEmail_ID="Email"
    txt_Adminpassword_ID="Password"
    Btn_Login_Class="button-1 login-button"
    link_CustomerMenu_xpath="/html/body/div[3]/div[2]/div/ul/li[4]/a/span"
    link_CustomerSubMenu_xpath="/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span"
    Btn_Addnew_Class="btn bg-blue"
    txt_AddNewEmail_xpath="//*[@id=Email]"
    txt_AddNewPassword_xpath="//*[@id=Password]"
    txt_AddNewFirstName_ID="FirstName"
    txt_AddNewLastName_ID="LastName"
    txt_CustomersRole_class="k-multiselect-wrap k-floatwrap"
    listItems_Administrator_Xpath="//li[contains(text(),'Administrators')]"
    listItems_Registred_Xpath = "//li[contains(text(),'Registered')]"
    listItems_Guests_Xpath="//li[contains(text(),'Guests')]"
    listItems_Vendors_Xpath = "//li[contains(text(),'Vendors')]"
    listItems_ForumModerators_Xpath = "//li[contains(text(),'Forum Moderators')]"
    drpGender_xpath="//*[@id=customer-info]/div[2]/div[1]/div[5]/div[1]/div"
    rdGender_Male_ID="Gender_Male"
    rdGender_Female_ID="Gender_Female"
    txt_DateofBirth_ID="DateOfBirth"
    txt_Company_name="Company"
    check_Istaxexempt_ID="IsTaxExempt"
    txt_AdminComment_xpath="AdminComment"
    txt_Savebutton_name="save"
    #constructor
    def __init__(self,driver):
        self.driver=driver
    def inputadminemailid(self,AdminEmail):
        self.driver.find_element_by_ID(self.txt_AdminEmail_ID).send_keys(AdminEmail)
    def inputPasswordID(self,AdminPassword):
        self.driver.find_element_by_ID(self.txt_Adminpassword_ID).send_keys(AdminPassword)
    def clickButton(self):
        self.driver.find_element_by_ID(self.Btn_Login_Class).click()


