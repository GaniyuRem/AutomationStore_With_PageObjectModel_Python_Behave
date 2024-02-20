from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.HomePage import HomePage
from features.pages.Search import SearchPage

@given(u'I got navigated to Home Page')
def step_impl(context):
 home_page=HomePage(context.driver)
 home_page.click_on_search_keyword_button()


@when(u'I enter valid product the Search word "{search_word_pass}" into the box field')
def step_impl(context,search_word_pass):
 context.search_page=SearchPage(context.driver)
 context.search_page.search_product(search_word_pass)


@when(u'Search product should be valid for dispaly as result')
def step_impl(context):
 context.search_page.click_on_search_button()

@then(u'Valid product should get displayed in Search results')
def step_impl(context):
  assert context.search_page.display_search_result_expected_conditions("Shaving cream")
 

@given(u'I got navigated to HomePage to search for a product')
def step_impl(context):
  home_page=HomePage(context.driver)
  home_page.click_on_search_keyword_button()



@when(u'I enter invalid product the Search word "{search_word_fall}" into the box field')
def step_impl(context,search_word_fall):
 context.search_page=SearchPage(context.driver)
 context.search_page.search_product(search_word_fall)

@when(u'I click on search button for invalid search')
def step_impl(context):
  context.search_page.click_on_search_button()



@then(u'message of invalid product be dispalyed')
def step_impl(context):
  context.search_page.display_search_result_expected_conditions("Products meeting the search criteria")



@given(u'I got navigated to Home page move cursor to search field')
def step_impl(context):
  home_page=HomePage(context.driver)
  home_page.click_on_search_keyword_button()

@when(u'I dont any input text in the Search box field')
def step_impl(context):
 context.search_page=SearchPage(context.driver)
 context.search_page.search_product("")


@when(u'I click on search button to process empty field')
def step_impl(context):
  context.search_page.click_on_search_button()


@then(u'message of no results should be dispalyed')
def step_impl(context):
  context.search_page.display_search_result_expected_conditions("Products meeting the search criteria")

