Feature: Product Page
  As a user, I should be able to view respective product pages with laid out content

  Scenario Outline: Check content of product page for each product category
    Given I navigate to the homepage
    And I click on the "<category_option>" category
    When I select a product from "<category_option>"
    Then Product page has all required content (picture, product name, description, add to cart button and price)
    Examples:
      |category_option  |
      |phones           |
      |laptops          |
      |monitors         |

  Scenario Outline: Add product to cart for each category
    Given I navigate to the homepage
    And I click on the "<category_option>" category
    When I select a product from "<category_option>"
    And I click on add product to cart button
    Then Alert returns "Product added"
    Examples:
      |category_option  |
      |phones           |
      |laptops          |
      |monitors         |
