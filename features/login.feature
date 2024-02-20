Feature: Login Functionality

 @Login
 Scenario: Login with invalid email and invalid password
  Given I navigated to Login Page with invalid email and invalid password
  When I enter invalid email and invalid password into the fields
    | password     | 
    | babe4Rea     | 
  And I click on the Login button check invalid email and invalid password
  Then I should get a warning login invalid message

    
 @Login 
 Scenario: Login with a valid email and valid password
  Given I navigated to Login page with valid email and valid password
  When I enter a valid email and valid password into the fields
     | email        | password  | 
     | apple_pie    | babe4Real |
  And I click on the Login button checks valid email and valid password
  Then I should Login succesfully to User Details

 @Login
 Scenario: I navigated to Login page with valid email and invalid password
  Given I navigated to Login page with valid email and invalid password
  When I enter valid email and invalid password into the fields
   | email        | 
   | apple_pie    | 
  And I click on Login button checks the valid email and invalid password
  Then I should get a invalid credentials warning message

 @Login
 Scenario: Login without enterning any credentials
  Given I navigated to Login page without any credentials
  When I leave the login email and password field blank
  And I click on the Login button checks if fields has login credentials
  Then I should get fields empty or error message