Feature: Cart Page
  As a user, I should be able to interact with the cart page with actions like adding products to cart...


  Scenario Outline: Check cart content for each category
    Given I have a product with "<category_option>" added to cart
    When I click on the "cart" option on the navigation bar
    Then Cart page has all the has all required content(total price, place order button, pic, title, price and delete)
    Examples:
      |category_option  |
      |phones           |
      |laptops          |
      |monitors         |
