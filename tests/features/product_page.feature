Feature: Product Page
  As a user, I should be able to sign into my an account by filling username and password fields in the sign in pop up window

  Scenario Outline: Check content of product page for each product category
    Given I navigate to the homepage
    When I click on the "<category_option>" category
    Then Products are filtered to reflect "<category_option>" category
    When I select a product from "<category_option>"
    Then Product page has all required content (picture, product name, description, add to cart button and price)
    Examples:
      |category_option  |
      |phones           |
      |laptops          |
      |monitors         |

  Scenario Outline: Add product to cart for each category
    Given I navigate to the homepage
    When I click on the "<category_option>" category
    Then Products are filtered to reflect "<category_option>" category
    When I select a product from "<category_option>"
    And I click on add product to cart button
    Then Alert returns "Product added"
    Examples:
      |category_option  |
      |phones           |
      |laptops          |
      |monitors         |
