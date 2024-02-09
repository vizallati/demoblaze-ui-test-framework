Feature: Contact
  As a user, I should be able to send message from contact pop up

  Scenario Outline: Send message
    Given I navigate to the homepage
    When I click on the "contact" option on the navigation bar
    And I fill in "<email>", "<name>", "<message>" and click the send message button
    Then Alert returns "Thanks for the message!!"
    Examples:
      |email                | name| message|
      |randomemail@yahoo.com| Jake| What's the status of my order|
