
class Element:
 
  def __init__(self,driver):
    self.__driver=driver

    self.__element_length=[]
    self.__element_types=[]
    
    self.__fields_value={"populate_input_fields":[]}

  def __set_field_values(self,field_list_value=[]):
    if "SELECT" in self.__element_types:
      self.__fields_value.update({"populate_input_fields":field_list_value})
      self.update_field_value=self.__input_only_field_value()

      if len(self.update_field_value) < len(self.__element_types):
        raise IndexError(f"""
                      Missing 1 or More values Func Takes in List with {len(self.__element_types)} str value
                      """)
      
      if len(self.update_field_value) > len(self.__element_types):
        raise IndexError(f"""
                      Func Takes in List with {len(self.__element_types)} str value : {len(self.__fields_value["populate_input_fields"])} str value passed
                      """)
       
    if "SELECT" not in self.__element_types:
      self.__fields_value.update({"populate_input_fields":field_list_value})
      self.update_field_value=self.__input_only_field_value()

      if len(self.update_field_value) < len(self.__element_types):

        raise IndexError(f"""
                      Missing 1 or More values Func Takes in List with {len(self.__element_types)} str value we
                      """)
      if len(self.update_field_value) > len(self.__element_types):
        raise IndexError(f"""
                      Func Takes in List with {len(self.__element_types)} str value : {len(self.__fields_value["populate_input_fields"])} str value passed
                      """)
      
  def __input_only_field_value(self):
    return self.__fields_value["populate_input_fields"]

  def __find_element_types(self,element_one,element_two,element_three=None):
    self.check_element_tag_type=''
    
    self.__element_length.append(element_one)
    self.__element_length.append(element_two)
    self.__element_length.append(".length")
    self.__element_length_value=''.join(self.__element_length)

    self.element_input_field=[]
    self.element_input_field.append(element_one)
    self.element_input_field.append(element_two)
    if element_three == None:
      element_three = None
    else:
      self.element_input_field.append(element_three)
      
    for index in range(0,self.__driver.execute_script(self.__element_length_value)):
      self.element_input_field.insert(2,str([index]))
      self.element_input_field.insert(4,"childNodes[1].nodeName")
      self.check_element_tag_type=''.join(self.element_input_field)

      self.__element_types.append(self.__driver.execute_script(self.check_element_tag_type))

      del self.element_input_field[2]
      del self.element_input_field[3]

  def input_select_elm(self,element_one,element_two,element_three,input_values):
    self.__find_element_types(element_one,element_two,element_three)
    try:
      if "INPUT" in self.__element_types and "SELECT" in self.__element_types:
        self.__set_field_values(input_values)
        self.user_list_input_field_value=self.__input_only_field_value()

        self.element_types_input=[]
        self.store_element_types_input=''
        self.element_types_input.append(element_one)
        self.element_types_input.append(element_two)
        self.element_types_input.append(element_three)


        self.element_types_select=[]
        self.store_element_types_select=''
        self.element_types_select.append(element_one)
        self.element_types_select.append(element_two)
        self.element_types_select.append(element_three)

        for index_t,element_tag_name in enumerate(self.__element_types):
          if self.__element_types[index_t] == "INPUT":
            self.element_types_input.insert(2,str([index_t]))
       
            self.element_types_input.append(f"getElementsByTagName('{self.__element_types[index_t].lower()}')[0].value='{self.user_list_input_field_value[index_t]}'")
    
            self.store_element_types_input=''.join(self.element_types_input)

            self.__driver.execute_script(self.store_element_types_input)

            del self.element_types_input[2]
            del self.element_types_input[3]
            
          if self.__element_types[index_t] == "SELECT":
            self.element_types_select.insert(2,str([index_t]))
       
            self.element_types_select.append(f"getElementsByTagName('{self.__element_types[index_t].lower()}')[0].selectedIndex='{self.user_list_input_field_value[index_t]}'")
    
            self.store_element_types_select=''.join(self.element_types_select)

            self.__driver.execute_script(self.store_element_types_select)

            del self.element_types_select[2]
            del self.element_types_select[3]
            
      else:
        raise TypeError(f"{self.input_select_elm.__name__}: Param must be INPUT & SELECT WebElement")
    except TypeError as err:
      print(err)
    
  def  input_elm(self,element_one,element_two,element_three,input_values):
    self.__find_element_types(element_one,element_two,element_three)

    try:
      if "INPUT" in self.__element_types and "SELECT" not in self.__element_types:
        self.__set_field_values(input_values)

        self.user_list_input_field_value=self.__input_only_field_value()

        self.stand_alone_elm_input=[]
        self.store_stand_alone_elm_input=''
        self.stand_alone_elm_input.append(element_one)
        self.stand_alone_elm_input.append(element_two)
        self.stand_alone_elm_input.append(element_three)

        for index_t,element_tag_name in enumerate(self.__element_types):
          if self.__element_types[index_t] == "INPUT":
            self.stand_alone_elm_input.insert(2,str([index_t]))
       
            self.stand_alone_elm_input.append(f"getElementsByTagName('{self.__element_types[index_t].lower()}')[0].value='{self.user_list_input_field_value[index_t]}'")
    
            self.store_stand_alone_elm_input=''.join(self.stand_alone_elm_input)

            self.__driver.execute_script(self.store_stand_alone_elm_input)

            del self.stand_alone_elm_input[2]
            del self.stand_alone_elm_input[3]
      else:
        raise ValueError("Element_two take in a INPUT Element")
    except ValueError as err:
      print(err)