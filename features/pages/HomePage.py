from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver  
from utilities.WebElement import Element



class HomePage:

 def __init__(self,driver):
  self.driver=driver
  self.invalid_email = Element(driver)
  self.err_login_details="Error: Incorrect login or password provided."
  self.invalid_email_val=["apple_pi","babe4Real"]
  self.search_keyword_xpath="//div[@class='block_4']/form/div/input"

 def click_on_login_or_register_account_link(self):
  self.click_login_link=self.driver.wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Login or register')))
  self.click_login_link.click()

 def click_on_register_continue_button(self):
  click_reg_continue=self.driver.wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@class="col-sm-6 newcustomer"]/div/form/fieldset/button')))
  click_reg_continue.click()

 
 def click_on_search_keyword_button(self):
  click_reg_continue=self.driver.wait.until(EC.visibility_of_element_located((By.XPATH,self.search_keyword_xpath)))
  click_reg_continue.click()
