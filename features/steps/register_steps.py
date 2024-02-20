from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.WebElement import Element
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage
import time

@given(u'I navigated to Register Page with all field')
def step_impl(context):
 context.home_page=HomePage(context.driver)
 context.home_page.click_on_login_or_register_account_link()
 context.home_page.click_on_register_continue_button()

 
@when(u'I enter a details in all fields')
def step_impl(context):
 context.register=RegisterPage(context.driver)
 context.register.enter_first_name(context.fake.first_name())
 context.register.enter_last_name(context.fake.last_name())
 context.register.enter_email(context.fake.email())
 for row in context.table:
  context.register.enter_phone_number(row["phone_num"])
  context.register.enter_fax_number(row["fax_num"])
  context.register.enter_address_one(row["address_one"])
  context.register.enter_address_two(row["address_two"])
  context.register.enter_city(row["city_name"])
  context.register.enter_region_or_state(row["region_or_state"])
  context.register.enter_zip_code(row["zip_code"])
  context.register.enter_country(row["country"])
  context.register.enter_password(row["password"])
  context.register.enter_confirm_password(row["confirm_password"])
 context.register.enter_company_name(context.fake.company())
 context.register.enter_login_name(context.fake.user_name())
 time.sleep(4)


@when(u'I click to accept all policy for all fields')
def step_impl(context):
  context.register.click_subcribe_options("yes")
  context.register.click_privacy_and_policy()

@when(u'I clcik on Register button with field given')
def step_impl(context):
  context.register.click_register_button()


@then(u'Account should get created with all fields')
def step_impl(context):
 assert context.register.display_successful_user_registration_message("YOUR ACCOUNT HAS BEEN CREATED!")


@given(u'I navigated to Register Page with mandatory field required')
def step_impl(context):
  context.home_page=HomePage(context.driver)
  context.home_page.click_on_login_or_register_account_link()
  context.home_page.click_on_register_continue_button()


@when(u'I enter details into mandatory fields')
def step_impl(context):
  context.register=RegisterPage(context.driver)
  context.register.enter_first_name(context.fake.first_name())
  context.register.enter_last_name(context.fake.last_name())
  context.register.enter_email(context.fake.email())
  context.register.enter_login_name(context.fake.user_name())

  for row in context.table:
    context.register.enter_address_one(row["address_one"])
    context.register.enter_city(row["city_name"])
    context.register.enter_region_or_state(row["region_or_state"])
    context.register.enter_zip_code(row["zip_code"])
    context.register.enter_country(row["country"])
    context.register.enter_password(row["password"])
    context.register.enter_confirm_password(row["confirm_password"])
 

@when(u"I click to accept all policy for mandatory fields")
def step_impl(context):
  context.register.click_subcribe_options("yes")
  context.register.click_privacy_and_policy()


@when(u'I clcik on Register button with mandatory field required')
def step_impl(context):
  context.register.click_register_button()



@then(u'Account should get created with mandatory fields')
def step_impl(context):
  assert context.register.display_successful_user_registration_message("YOUR ACCOUNT HAS BEEN CREATED!")





@given(u'I navigated to Register Page with duplicate email address')
def step_impl(context):
#  J1001 user_testing
# duplicate emails address to be used john@gmail.com
 context.home_page=HomePage(context.driver)
 context.home_page.click_on_login_or_register_account_link()
 context.home_page.click_on_register_continue_button()



@when(u'I enter only duplicate email account as "{duplicate_email_acc}"')
def step_impl(context,duplicate_email_acc):
  context.register=RegisterPage(context.driver)
  context.register.enter_email(duplicate_email_acc)

@when(u'I accept all privacy policy for a duplicate email address')
def step_impl(context):
  context.register.click_subcribe_options("yes")
  context.register.click_privacy_and_policy()


@when(u'I clcik on Register button with a duplicate email address')
def step_impl(context):
   context.register.click_register_button()

  


@then(u'Warning display informing about duplicate email address')
def step_impl(context):
  assert context.register.display_error_user_registration_message(email_err_msg="Error: E-Mail Address is already registered!")


@given(u'I navigated to Register Page with duplicate username')
def step_impl(context):
 #  apple_pie user_testing
# duplicate emails address to be used john@gmail.com
  context.home_page=HomePage(context.driver)
  context.home_page.click_on_login_or_register_account_link()
  context.home_page.click_on_register_continue_button()

@when(u'I enter only duplicate username as "{duplicate_user_name}"')
def step_impl(context,duplicate_user_name):
  context.register=RegisterPage(context.driver)
  context.register.enter_login_name(duplicate_user_name)

@when(u'I accept all privacy policy to proceed duplicate username')
def step_impl(context):
  context.register.click_subcribe_options("yes")
  context.register.click_privacy_and_policy()


@when(u'I clcik on Register button to proceed duplicate username')
def step_impl(context):
  context.register.click_register_button()


@then(u'Warning display informing about duplicate username account')
def step_impl(context):
  context.register.display_error_user_registration_message(login_name_err_msg="This login name is not available. Try different login name!")
  


@given(u'I navigated to Register page without any credentials')
def step_impl(context):
  context.home_page=HomePage(context.driver)
  context.home_page.click_on_login_or_register_account_link()
  context.home_page.click_on_register_continue_button()



@when(u'I leave the Registration field blank')
def step_impl(context):
  context.register=RegisterPage(context.driver)
  context.register.enter_first_name("")
  context.register.enter_last_name("")
  context.register.enter_email("")
  context.register.enter_phone_number("")
  context.register.enter_fax_number("")
  context.register.enter_company_name("")
  context.register.enter_address_one("")
  context.register.enter_address_two("")
  context.register.enter_city("")
  context.register.enter_region_or_state("")
  context.register.enter_zip_code("")
  context.register.enter_country("")
  context.register.enter_login_name("")
  context.register.enter_password("")
  context.register.enter_confirm_password("")



@when(u'I accept all privacy policy to proceed without filling any values in fields')
def step_impl(context):
  context.register.click_subcribe_options("yes")
  context.register.click_privacy_and_policy()

@when(u'I clcik on Register button with blank Registration fields')
def step_impl(context):
   context.register.click_register_button()

@then(u'Warning display informing about Registration field empty')
def step_impl(context):
  assert context.register.display_error_user_registration_message(first_name_err_msg="First Name must be between 1 and 32 characters!",last_name_err_msg="Last Name must be between 1 and 32 characters!",email_err_msg="Email Address does not appear to be valid!",address_one_err_msg="Address 1 must be between 3 and 128 characters!",address_two_err_msg="City must be between 3 and 128 characters!",region_or_state_err_msg="Please select a region / state!",zip_code_or_postal_code_err_msg="Zip/postal code must be between 3 and 10 characters!",login_name_err_msg="Login name must be alphanumeric only and between 5 and 64 characters!",password_err_msg="Password must be between 4 and 20 characters!")

@given(u'I navigated to Register Page without filling mandatory field required')
def step_impl(context):
  context.home_page=HomePage(context.driver)
  context.home_page.click_on_login_or_register_account_link()
  context.home_page.click_on_register_continue_button()

@when(u'I enter details into leaving out mandatory fields')
def step_impl(context):
  context.register=RegisterPage(context.driver)
  for row in context.table:
    context.register.enter_phone_number(row["phone_num"])
    context.register.enter_fax_number(row["fax_num"])
    context.register.enter_address_two(row["address_two"])
  context.register.enter_company_name(context.fake.company())

@when(u'I accept all privacy policy to proceed without mandotory fields with any values')
def step_impl(context):
  context.register.click_subcribe_options("yes")
  context.register.click_privacy_and_policy()

@when(u'I clcik on Register button with mandatory field required not filled')
def step_impl(context):
   context.register.click_register_button()

@then(u'I should get error and account should not be  created')
def step_impl(context):
  assert context.register.display_error_user_registration_message(first_name_err_msg="First Name must be between 1 and 32 characters!",last_name_err_msg="Last Name must be between 1 and 32 characters!",email_err_msg="Email Address does not appear to be valid!",address_one_err_msg="Address 1 must be between 3 and 128 characters!",address_two_err_msg="City must be between 3 and 128 characters!",region_or_state_err_msg="Please select a region / state!",zip_code_or_postal_code_err_msg="Zip/postal code must be between 3 and 10 characters!",login_name_err_msg="Login name must be alphanumeric only and between 5 and 64 characters!",password_err_msg="Password must be between 4 and 20 characters!")

