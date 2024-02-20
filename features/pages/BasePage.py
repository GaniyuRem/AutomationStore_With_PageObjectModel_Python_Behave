from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

  def __init__(self,driver) -> None:
    self.driver=driver

 
  def click_on_element(self,locator_type,locator_value):
    """
    Locator_type : takes in string either _xpath or _link_text

    locator_value sample [_xpath, //div[@class="input-group col-sm-4"]//span]

    locator_value sample [_link_text, Login or Register]

    """
    if locator_type.endswith("_xpath"):
      element=self.driver.wait.until(EC.visibility_of_element_located((By.XPATH,locator_value)))
    elif  locator_type.endswith("_link_text"):
      element=self.driver.wait.until(EC.visibility_of_element_located((By.LINK_TEXT,locator_value)))

    element.click()
  
  
  def send_keys_on_element(self,locator_type,locator_value,send_keys_value):
    """
        Locator_type : takes in string either _xpath or _link_text

        locator_value sample [//div[@class="input-group col-sm-4"]//span]

        send_keys_value sample ["Adam ogunkoya"]

        complete sample [_xpath,//div[@class="input-group col-sm-4"]//span,"Adam ogunkoya"]

        """
    if locator_type.endswith("_xpath"):
      element=self.driver.wait.until(EC.visibility_of_element_located((By.XPATH,locator_value)))
    elif  locator_type.endswith("_link_text"):
      element=self.driver.wait.until(EC.visibility_of_element_located((By.LINK_TEXT,locator_value)))

    element.send_keys(send_keys_value)


  def retieve_display_text_status(self,locator_type,locator_value):
    if locator_type.endswith("_xpath"):
      self.err_or_succes_message_text=self.driver.wait.until(EC.visibility_of_element_located((By.XPATH,locator_value)))
      return self.err_or_succes_message_text
 
  
