from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.WebElement import Element
from selenium.webdriver.common.action_chains import ActionChains


class AccountPage:

 def __init__(self,driver):
  self.driver=driver
 
 
 def display_edit_status_of_current_login_user(self):
  self.move_to_ele=self.driver.wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@class="block_2"]/div')))
  self.driver.actions.move_to_element(self.move_to_ele).perform()
  move_to_current_ele=self.driver.wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@class="block_2"]/div/ul/li/ul/li[3]')))
  move_to_current_ele.click()
  confirm_user=self.driver.wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Edit account details')))
  assert confirm_user.is_displayed()