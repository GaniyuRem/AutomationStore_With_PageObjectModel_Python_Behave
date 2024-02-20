from features.pages.BasePage import BasePage

class RegisterPage(BasePage):
  def __init__(self,driver) -> None:
    super().__init__(driver)
    self.__first_name_xpath="//div[@class='registerbox form-horizontal'][1]/fieldset/div[1]/div/input[@type='text']"
    self.__last_name_xpath="//div[@class='registerbox form-horizontal'][1]/fieldset/div[2]/div/input[@type='text']"
    self.__email_xpath="//div[@class='registerbox form-horizontal'][1]/fieldset/div[3]/div/input[@type='text']"
    self.__telephone_xpath="//div[@class='registerbox form-horizontal'][1]/fieldset/div[4]/div/input[@type='text']"
    self.__fax_number_xpath="//div[@class='registerbox form-horizontal'][1]/fieldset/div[5]/div/input[@type='text']"
    self.__company_xpath="//div[@class='registerbox form-horizontal '][1]/fieldset/div[1]/div/input"
    self.__address_one_xpath="//div[@class='registerbox form-horizontal '][1]/fieldset/div[2]/div/input"
    self.__address_two_xpath="//div[@class='registerbox form-horizontal '][1]/fieldset/div[3]/div/input"
    self.__city_name_xpath="//div[@class='registerbox form-horizontal '][1]/fieldset/div[4]/div/input"
    self.__zip_code_xpath="//div[@class='registerbox form-horizontal '][1]/fieldset/div[6]/div/input"
    self.__user_name_xpath="//div[@class='registerbox form-horizontal'][2]/fieldset/div[1]/div/input"
    self.__password_xpath="//div[@class='registerbox form-horizontal'][2]/fieldset/div[2]/div/input"
    self.__cofirm_password_xpath="//div[@class='registerbox form-horizontal'][2]/fieldset/div[3]/div/input"
    self.__subscribe_yes_xpath="//div[@class='registerbox form-horizontal'][3]/fieldset/div/div/label/input[@id='AccountFrm_newsletter1']"
    self.__subscribe_no_xpath="//div[@class='registerbox form-horizontal'][3]/fieldset/div/div/label/input[@id='AccountFrm_newsletter0']"
    self.__privacy_policy_xpath="//div[@class='col-md-12']/label/input"
    self.__register_button_xpath="//div[@class='col-md-12']/div/button"
    self.__succesful_account_registration_xpath="//div[@class='col-md-9 col-xs-12 mt20']/div/h1/span"
    self.__not_succesful_account_registration_xpath="//div[@class='col-md-12 col-xs-12 mt20']/div/div[1]"
    # ERRORR PATHS
    self.__first_name_error_xpath="//div[@class='registerbox form-horizontal'][1]/fieldset/div[@class='form-group has-error'][1]/span[@class='help-block'][1]"
    self.__last_name_error_xpath="//div[@class='registerbox form-horizontal'][1]/fieldset/div[@class='form-group has-error'][2]/span[@class='help-block'][1]"
    # self.__email_error_xpath="//div[@class='registerbox form-horizontal'][1]/fieldset/div[@class='form-group has-error'][3]/span[@class='help-block'][1]"

    self.__address_one_error_xpath="//div[@class='registerbox form-horizontal '][1]/fieldset/div[@class='form-group has-error'][1]/span[@class='help-block'][1]"
    self.__address_two_error_xpath="//div[@class='registerbox form-horizontal '][1]/fieldset/div[@class='form-group has-error'][2]/span[@class='help-block'][1]"
    self.__region_or_state_error_xpath="//div[@class='registerbox form-horizontal '][1]/fieldset/div[@class='form-group has-error'][3]/span[@class='help-block'][1]"
    self.__zip_code_or_postal_code_error_xpath="//div[@class='registerbox form-horizontal '][1]/fieldset/div[@class='form-group has-error'][4]/span[@class='help-block'][1]"
    self.__login_name_error_xpath="//div[@class='registerbox form-horizontal'][2]/fieldset/div[@class='form-group has-error'][1]/span[@class='help-block'][1]"
    self.__password_error_xpath="//div[@class='registerbox form-horizontal'][2]/fieldset/div[@class='form-group has-error'][2]/span[@class='help-block'][1]"

  def set_email_error_xpath_options(self,check_email_err_msg):
      if check_email_err_msg == "Error: E-Mail Address is already registered!":
          return "//div[@class='col-md-12 col-xs-12 mt20']/div/div[@class='alert alert-error alert-danger']"
      elif check_email_err_msg == "Email Address does not appear to be valid!":
          return "//div[@class='registerbox form-horizontal'][1]/fieldset/div[@class='form-group has-error'][3]/span[@class='help-block'][1]"
      else:
        return "//div[@class='col-md-12 col-xs-12 mt20']/div/div[@class='alert alert-error alert-danger']"

  def enter_first_name(self,first_name):
    self.send_keys_on_element("_xpath",self.__first_name_xpath,first_name)


  def enter_last_name(self,last_name):
    self.send_keys_on_element("_xpath",self.__last_name_xpath,last_name)

  
  def enter_email(self,email):
    self.send_keys_on_element("_xpath",self.__email_xpath,email)

  
  def enter_phone_number(self,telephone):
    self.send_keys_on_element("_xpath",self.__telephone_xpath,telephone)

    
  def enter_fax_number(self,fax_number):
    self.send_keys_on_element("_xpath",self.__fax_number_xpath,fax_number)

  
  def enter_company_name(self,company):
    self.send_keys_on_element("_xpath",self.__company_xpath,company)

  
  def enter_address_one(self,adress_one):
    self.send_keys_on_element("_xpath",self.__address_one_xpath,adress_one)


  def enter_address_two(self,adress_two):
    self.send_keys_on_element("_xpath",self.__address_two_xpath,adress_two)


  def enter_city(self,city_name):
    self.send_keys_on_element("_xpath",self.__city_name_xpath,city_name)


  def enter_region_or_state(self,region_or_state_name):
    self.driver.execute_script("document.val = document.getElementsByClassName('registerbox form-horizontal')[1].childNodes[1].getElementsByClassName('form-group')[4].childNodes[3].getElementsByTagName('select')[0].children")
    for i in range(self.driver.execute_script(f'return document.val.length')):
      if self.driver.execute_script(f"return document.val{[i]}.innerText") == region_or_state_name:
        self.driver.execute_script(f"document.getElementsByClassName('registerbox form-horizontal')[1].childNodes[1].getElementsByClassName('form-group')[4].childNodes[3].getElementsByTagName('select')[0].selectedIndex={[i]}")     
        

  def enter_zip_code(self,zip_code):
    self.send_keys_on_element("_xpath",self.__zip_code_xpath,zip_code)


  def enter_country(self,country_name):
    self.driver.execute_script("document.val = document.getElementsByClassName('registerbox form-horizontal')[1].childNodes[1].getElementsByClassName('form-group')[6].childNodes[3].getElementsByTagName('select')[0].children")
    for i in range(self.driver.execute_script(f'return document.val.length')):
      if self.driver.execute_script(f"return document.val{[i]}.innerText") == country_name:
        self.driver.execute_script(f"document.getElementsByClassName('registerbox form-horizontal')[1].childNodes[1].getElementsByClassName('form-group')[6].childNodes[3].getElementsByTagName('select')[0].selectedIndex={[i]}")     
        

  def enter_login_name(self,user_name):
    self.send_keys_on_element("_xpath",self.__user_name_xpath,user_name)

  def enter_password(self,password):
    self.send_keys_on_element("_xpath",self.__password_xpath,password)


  def enter_confirm_password(self,confirm_password):
    self.send_keys_on_element("_xpath",self.__cofirm_password_xpath,confirm_password)

  def click_subcribe_options(self,subscribe):
    """
      Takes in string text : "Yes" or "No"
    """   
    if subscribe.lower() == "yes":
        self.click_on_element("_xpath",self.__subscribe_yes_xpath)
    elif subscribe.lower() == "no":
      self.click_on_element("_xpath",self.__subscribe_no_xpath)
      
  def click_privacy_and_policy(self):
    self.click_on_element("_xpath",self.__privacy_policy_xpath)

  def click_register_button(self):
    self.click_on_element("_xpath",self.__register_button_xpath)

  def display_successful_user_registration_message(self,succesfully_expected_warning_text):
    succesful_registration=self.retieve_display_text_status("_xpath",self.__succesful_account_registration_xpath)
    return succesful_registration.text.__eq__(succesfully_expected_warning_text)
  
  def display_error_user_registration_message(self,first_name_err_msg=None,last_name_err_msg=None,email_err_msg=None,address_one_err_msg=None,address_two_err_msg=None,region_or_state_err_msg=None,zip_code_or_postal_code_err_msg=None,login_name_err_msg=None,password_err_msg=None):
    first_name_err_elm=self.retieve_display_text_status("_xpath",self.__first_name_error_xpath)
    last_name_err_elm=self.retieve_display_text_status("_xpath",self.__last_name_error_xpath)
    email_err_elm=self.retieve_display_text_status("_xpath",self.set_email_error_xpath_options(email_err_msg))
    address_one_err_elm=self.retieve_display_text_status("_xpath",self.__address_one_error_xpath)
    address_two_err_elm=self.retieve_display_text_status("_xpath",self.__address_two_error_xpath)
    region_or_state_err_elm=self.retieve_display_text_status("_xpath",self.__region_or_state_error_xpath)
    zip_code_or_postal_code_err_elm=self.retieve_display_text_status("_xpath",self.__zip_code_or_postal_code_error_xpath)
    login_name_err_elm=self.retieve_display_text_status("_xpath",self.__login_name_error_xpath)
    password_err_elm=self.retieve_display_text_status("_xpath",self.__password_error_xpath)


    if first_name_err_msg==None and last_name_err_msg==None and email_err_msg==None and address_one_err_msg==None and address_two_err_msg==None and region_or_state_err_msg==None and zip_code_or_postal_code_err_msg==None and login_name_err_msg!=None and password_err_msg==None:
      print(login_name_err_msg)
      if login_name_err_elm.text.__eq__(login_name_err_msg):
        return True
      else:
        return False
    

    elif first_name_err_msg==None and last_name_err_msg==None and email_err_msg!=None and address_one_err_msg==None and address_two_err_msg==None and region_or_state_err_msg==None and zip_code_or_postal_code_err_msg==None and login_name_err_msg==None and password_err_msg==None:
      """
      Checks if email is a Duplicate Email 
        "Error: E-Mail Address is already registered!": "Email Address does not appear to be valid!"

      """
      if email_err_msg == "Error: E-Mail Address is already registered!":
        print("check me out",email_err_elm.text.split("\n")[1])
        if email_err_elm.text.split("\n")[1].__eq__(email_err_msg):
          return True
        else:
          return False
      elif email_err_msg == "Email Address does not appear to be valid!":
        if email_err_elm.text.__eq__(email_err_msg):
          return True
        else:
          return False

    elif first_name_err_msg!=None and last_name_err_msg!=None and email_err_msg!=None and address_one_err_msg!=None and address_two_err_msg!=None and region_or_state_err_msg!=None and zip_code_or_postal_code_err_msg!=None and login_name_err_msg!=None and password_err_msg!=None:
      if first_name_err_elm.text.__eq__(first_name_err_msg) and last_name_err_elm.text.__eq__(last_name_err_msg) and email_err_elm.text.__eq__(email_err_msg) and address_one_err_elm.text.__eq__(address_one_err_msg) and address_two_err_elm.text.__eq__(address_two_err_msg) and region_or_state_err_elm.text.__eq__(region_or_state_err_msg) and zip_code_or_postal_code_err_elm.text.__eq__(zip_code_or_postal_code_err_msg) and login_name_err_elm.text.__eq__(login_name_err_msg) and password_err_elm.text.__eq__(password_err_msg):
        return True
      else:
        return False
    
    