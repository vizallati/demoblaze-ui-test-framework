Feature: About Us
  As a user, I should be able to sign into my an account by filling username and password fields in the sign in pop up window


  Scenario: View content in about us pop up
    Given I navigate to the homepage
    When I click on the "about_us" option on the navigation bar
    Then Youtube video should be displayed