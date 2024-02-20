Feature: Register Account Functionality

 @Register
 Scenario: Register with all fields
  Given I navigated to Register Page with all field
  When I enter a details in all fields
     | phone_num    | fax_num       | address_one     | address_two   | city_name    | region_or_state  | zip_code  |  country         |  password | confirm_password   |
     | 07465740342  | 02039495043   | 80 Edge Street  | Liverpool Way | HarshFord    | Greater London   | S90 1NZ   |  United Kingdom  |  bbbbbb   |  bbbbbb            |
  And I click to accept all policy for all fields
  And I clcik on Register button with field given
  Then Account should get created with all fields

 @Register
 Scenario: Register with mandatory fields
  Given I navigated to Register Page with mandatory field required
  When I enter details into mandatory fields
      | address_one     | city_name    | region_or_state  | zip_code  |  country         |  password | confirm_password   |
      | 80 Edge Street  | HarshFord    | Greater London   | S90 1NZ   |  United Kingdom  |  bbbbbb   |  bbbbbb            |
  And I click to accept all policy for mandatory fields
  And I clcik on Register button with mandatory field required
  Then Account should get created with mandatory fields

 @Register
 Scenario: Register with a duplicate email address
  Given I navigated to Register Page with duplicate email address
  When I enter only duplicate email account as "john@gmail.com"
  And I accept all privacy policy for a duplicate email address
  And I clcik on Register button with a duplicate email address
  Then Warning display informing about duplicate email address


 @Register
 Scenario: Register with a duplicate username
  Given I navigated to Register Page with duplicate username
  When I enter only duplicate username as "apple_pie"
  And I accept all privacy policy to proceed duplicate username
  And I clcik on Register button to proceed duplicate username
  Then Warning display informing about duplicate username account


 @Register
 Scenario: Register without enterning filling any fields
  Given I navigated to Register page without any credentials
  When I leave the Registration field blank
  And I accept all privacy policy to proceed without filling any values in fields
  And I clcik on Register button with blank Registration fields
  Then Warning display informing about Registration field empty

@Register
 Scenario: Register without filling mandatory fields
  Given I navigated to Register Page without filling mandatory field required
  When I enter details into leaving out mandatory fields
      | phone_num    | fax_num       | address_two   |
      | 07465740342  | 02039495043   | Liverpool Way |
  And I accept all privacy policy to proceed without mandotory fields with any values
  And I clcik on Register button with mandatory field required not filled
  Then I should get error and account should not be  created

