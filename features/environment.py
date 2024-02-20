from selenium import *
import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from behave import fixture
# -- FILE: features/environment.py
from behave import fixture, use_fixture
# from behave4my_project.fixtures import wsgi_server
from selenium import webdriver
from utilities import ConfigReader
from faker import Faker
from datetime import datetime


def before_scenario(context,scenario):
 browser_name = ConfigReader.read_configuration("Selenium Properties","browser")
 if browser_name.__eq__("Chrome"):
   context.driver = webdriver.Chrome()
 elif browser_name.__eq__("Firefox"):
  context.driver = webdriver.Firefox()
 context.driver.maximize_window()
 context.driver.wait=WebDriverWait(context.driver,20)
 context.driver.actions=ActionChains(context.driver)
 context.driver.get(ConfigReader.read_configuration("Selenium Properties","url"))
 context.fake= Faker()
 context.datetime=datetime.now().strftime("%Y_%m_%d,%H_%M,%S")
 
def after_scenario(context,step):
 context.driver.quit()


def after_step(context,step):
 if step.status == 'failed':
  allure.attach(
            context.driver.get_screenshot_as_png(),
            name="failed_screenshot", attachment_type=allure.attachment_type.PNG)