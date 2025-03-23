Feature: Add product into cart functionality

#  Scenario: User can add a product into cart
#    Given Open Target.com
#    When Search for tea
#    Then Verify search results shown for tea
#    When Click on "Add to cart" button on a product
#    Then Side navigation panel with "Add to cart" button is shown
#    When Click on "Add to cart" button in the navigation panel
#    And Click on the "View cart & check out" button in navigation panel
#    Then Cart page is displayed with the added item and correct subtotal


  Scenario: "Your cart is empty" message is shown for empty cart
    Given Open Target.com
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown