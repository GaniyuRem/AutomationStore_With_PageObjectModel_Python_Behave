from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.WebElement import Element
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage
from features.pages.AccountPage import AccountPage
import time

@given(u'I navigated to Login Page with invalid email and invalid password')
def step_impl(context):
 context.home_page=HomePage(context.driver)
 context.home_page.click_on_login_or_register_account_link()

@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
 context.login_page=LoginPage(context.driver)
 
 context.login_page.enter_login_name(f'apple_pie'+ context.datetime)
 for row in context.table:
  context.login_page.enter_password(row["password"])


@when(u'I click on the Login button check invalid email and invalid password')
def step_impl(context):
 context.login_page.click_on_the_login_btn()

@then(u'I should get a warning login invalid message')
def step_impl(context):
 assert context.login_page.display_status_of_error_loggin("Error: Incorrect login or password provided.")



@given(u'I navigated to Login page with valid email and valid password')
def step_impl(context):
 context.home_page=HomePage(context.driver)
 context.home_page.click_on_login_or_register_account_link()


@when(u'I enter a valid email and valid password into the fields')
def step_impl(context):
 context.login_page=LoginPage(context.driver)
 for row in context.table:
  context.login_page.enter_login_name(row['email'])
  context.login_page.enter_password(row["password"])


@when(u'I click on the Login button checks valid email and valid password')
def step_impl(context):
 context.login_page.click_on_the_login_btn()

@then(u'I should Login succesfully to User Details')
def step_impl(context):
 account_login_status= AccountPage(context.driver)
 account_login_status.display_edit_status_of_current_login_user()



@given(u'I navigated to Login page with valid email and invalid password')
def step_impl(context):

 context.home_page=HomePage(context.driver)
 context.home_page.click_on_login_or_register_account_link()
 

@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
 

 context.login_page=LoginPage(context.driver)
 for row in context.table:
  context.login_page.enter_login_name(row["email"])
 context.login_page.enter_password("babe4Real"+context.datetime)


@when(u'I click on Login button checks the valid email and invalid password')
def step_impl(context):
 context.login_page.click_on_the_login_btn()


@then(u'I should get a invalid credentials warning message')
def step_impl(context):
  assert context.login_page.display_status_of_error_loggin("Error: Incorrect login or password provided.")


@given(u'I navigated to Login page without any credentials')
def step_impl(context):

 context.home_page=HomePage(context.driver)
 context.home_page.click_on_login_or_register_account_link()

 

@when(u'I leave the login email and password field blank')
def step_impl(context):
 context.login_page=LoginPage(context.driver)
 context.login_page.enter_login_name("")
 context.login_page.enter_password("")

@when(u'I click on the Login button checks if fields has login credentials')
def step_impl(context):
 context.login_page.click_on_the_login_btn()


@then(u'I should get fields empty or error message')
def step_impl(context):
  assert context.login_page.display_status_of_error_loggin("Error: Incorrect login or password provided.")



