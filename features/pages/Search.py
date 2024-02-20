from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage

class SearchPage(BasePage):

 def __init__(self,driver) -> None:
  self.driver=driver
  self.search_product_input_field_xpath='//div[@class="block_4"]/form/div/input'

  self.search_button_icon_click_xpath='//div[@class="block_4"]/form/div/div/i'
  self.search_result_condition_product_found="//div[@id='product_details']/div/div[2]/div/div/h1/span"
  self.search_result_condition_product_not_found_xpath="//div[@class='col-md-12 col-xs-12 mt20']/div/div/h4[2]"

 def __set_display_search_result_expected_conditions_xpath(self,expected_conditions):
   if expected_conditions == "Products meeting the search criteria":
     return self.search_result_condition_product_not_found_xpath
   else:
     return self.search_result_condition_product_found

 def search_product(self,search_product):
  self.send_keys_on_element("_xpath",self.search_product_input_field_xpath,search_product)

 def click_on_search_button(self):
  self.click_on_element("_xpath",self.search_button_icon_click_xpath)
  
 def display_search_result_expected_conditions(self,expected_condition):
   display_expected_result = self.retieve_display_text_status("_xpath",self.__set_display_search_result_expected_conditions_xpath(expected_condition))
   return display_expected_result.text.__eq__(expected_condition)


