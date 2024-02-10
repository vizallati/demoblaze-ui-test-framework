Feature: Home Page
  As a user, I should be able to sign into my an account by filling username and password fields in the sign in pop up window

  Scenario Outline: Select Category
    Given I navigate to the homepage
    When I click on the "<category_option>" category
    Then Products are filtered to reflect "<category_option>" category
    Examples:
      |category_option  |
      |phones           |
      |laptops          |
      |monitors         |
