Feature: Cart functionality

  Scenario: User can add a product into cart
    Given Open Target.com
    When Search for tea
    And Click on "Add to cart" button on the product
    Then Side navigation menu is shown
    When Click on "Add to cart" button in side navigation menu
    And Click on "View cart & check out" button in side navigation menu
    Then Cart page is displayed with the added item and correct subtotal


  Scenario: "Your cart is empty" message is shown for empty cart
    Given Open Target.com
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown