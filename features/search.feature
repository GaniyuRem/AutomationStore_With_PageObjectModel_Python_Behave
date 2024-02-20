Feature: Search Functionality
    @Search
    Scenario: Search for a valid proudct
        Given I got navigated to Home Page
        When I enter valid product the Search word "Shaving cream" into the box field
        And Search product should be valid for dispaly as result
        Then Valid product should get displayed in Search results

    @Search
    Scenario: Search for an invalid product
        Given I got navigated to HomePage to search for a product
        When I enter invalid product the Search word "Sugar" into the box field
        When I click on search button for invalid search
        Then message of invalid product be dispalyed
    @Search
    Scenario: Search without entering any product
        Given I got navigated to Home page move cursor to search field
        When I dont any input text in the Search box field
        When I click on search button to process empty field
        Then message of no results should be dispalyed

