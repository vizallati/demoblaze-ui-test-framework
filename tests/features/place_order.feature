Feature: Place Order Pop Up
  As a user, I should be able to place an order for available products


  Scenario Outline: Place order for each category
    Given I have a product with "<category_option>" added to cart
    When I click on the "cart" option on the navigation bar
    And I place an order with "<customer_name>", "<country>", "<city>", "<credit_card>", "<month>" and "<year>"
    Then Order was successfully placed
    Examples:
      |category_option  |customer_name | country       |city   |credit_card       |month |year   |
      |phones           |Alexis Tucker |Sweden         |Boden  | 4413653914776074 |   08 | 2027  |
      |laptops          |Ike Smith     |Burkina Faso   |Dori   | 4285408151715953 |   07 | 2028  |
      |monitors         |Edward Dillon |Zimbabwe       |Harare | 4692798690640127 |   01 | 2029  |