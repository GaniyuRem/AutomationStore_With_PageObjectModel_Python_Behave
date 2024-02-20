from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from features.pages.BasePage import BasePage


class LoginPage(BasePage):

 def __init__(self,driver):
  super().__init__(driver)
  self.err_login_details="Error: Incorrect login or password provided."
  self.enter_login_name_xpath='//form[@id="loginFrm"]//fieldset/div/div/input[@id="loginFrm_loginname"]'
  self.enter_password_xpath='//form[@id="loginFrm"]//fieldset/div[2]/div/input[@id="loginFrm_password"]'
  self.login_btn_xpath='//div[@class="col-sm-6 returncustomer"]/div/form/fieldset/button'
  self.login_error_status_xpath="//div[@class='alert alert-error alert-danger']"


 def enter_login_name(self,email):
  self.send_keys_on_element("_xpath",self.enter_login_name_xpath,email)

 
 def enter_password(self,password):
   self.send_keys_on_element("_xpath",self.enter_password_xpath,password)
   
 def click_on_the_login_btn(self):
  self.click_on_element("_xpath",self.login_btn_xpath)
 

 def display_status_of_error_loggin(self,expected_condition):
  diplay_status_expected_condition_login_page= self.retieve_display_text_status("_xpath",self.login_error_status_xpath)
  return diplay_status_expected_condition_login_page.text.split("\n")[1].__eq__(expected_condition)


