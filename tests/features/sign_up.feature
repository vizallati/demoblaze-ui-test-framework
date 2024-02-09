Feature: Sign Up
  As a user, I should be able to create an account by filling username and password fields in the sign up pop up window

  Scenario: Create account
    Given I navigate to the homepage
    When I click on the "sign_up" option on the navigation bar
    And I fill in my username, password and click on the signup button
    Then Alert returns correct "Sign up successful." message

  Scenario: Create account with preexisting username
    Given I have a user already created
    When I try to create account with preexisting username
    Then Alert returns correct "This user already exist." message

  Scenario: Signup without filling username and password
    Given I navigate to the homepage
    And I click on the "sign_up" option on the navigation bar
    When I click signup button without filling in username and password
    Then Alert returns correct "Please fill out Username and Password." message

  Scenario Outline: Signup without filling one of required values
    Given I navigate to the homepage
    And I click on the "sign_up" option on the navigation bar
    When I fill in only "<required_value>" and click on the signup button
    Then Alert returns correct "Please fill out Username and Password." message
    Examples:
      |required_value  |
      |username        |
      |password        |

