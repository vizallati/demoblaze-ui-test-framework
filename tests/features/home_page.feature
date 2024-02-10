Feature: Home Page
  As a user, I should be to navigate to the homepage and filter between available categories

  Scenario Outline: Select Category
    Given I navigate to the homepage
    When I click on the "<category_option>" category
    Then Products are filtered to reflect "<category_option>" category
    Examples:
      |category_option  |
      |phones           |
      |laptops          |
      |monitors         |
