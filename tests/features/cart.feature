Feature: Cart Page
  As a user, I should be able to sign into my an account by filling username and password fields in the sign in pop up window


  Scenario Outline: Check cart content for each category
    Given I navigate to the homepage
    When I click on the "<category_option>" category
    Then Products are filtered to reflect "<category_option>" category
    When I select a product from "<category_option>"
    And I click on add product to cart button
    Then Alert returns "Product added"
    When I click on the "cart" option on the navigation bar
    Then Cart page has all the has all required content(total price, place order button, pic, title, price and delete)
    Examples:
      |category_option  |
      |phones           |
      |laptops          |
      |monitors         |
