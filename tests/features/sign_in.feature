Feature: Sign In
  As a user, I should be able to sign into my an account by filling username and password fields in the sign in pop up window

  Scenario: Login to account
    Given I have a user already created
    When I click on the "login" option on the navigation bar
    And I fill in my username, password and click on the sign in button
    Then I'm successfully logged into my account


  Scenario: Login without filling username and password
    Given I navigate to the homepage
    When I click on the "login" option on the navigation bar
    When I click signin button without filling in username and password
    Then Alert returns correct "Please fill out Username and Password." message

  Scenario Outline: Login without filling one of required values
    Given I navigate to the homepage
    When I click on the "login" option on the navigation bar
    When I fill in only "<required_value>" and click on the login button
    Then Alert returns correct "Please fill out Username and Password." message
    Examples:
      |required_value  |
      |username        |
      |password        |

  Scenario: Logout from account
    Given I have an account successfully created and logged in
    When I click on the "logout" option on the navigation bar
    Then I should be successfully logged out

