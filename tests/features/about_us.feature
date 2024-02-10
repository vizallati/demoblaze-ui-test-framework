Feature: About Us
  As a user, I should be able to navigate to the about us pop on the navigation bar and view the content


  Scenario: View content in about us pop up
    Given I navigate to the homepage
    When I click on the "about_us" option on the navigation bar
    Then Youtube video should be displayed