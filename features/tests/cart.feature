Feature: Add product into cart functionality

  Scenario: User can add a product into cart
    Given Open Target.com
    When Input tea into search field
    And Click on search icon
    Then Product results for tea are shown
    When Click on "Add to cart" button on a product
    Then Right-side navigation panel with "Add to cart" button is shown
    When Click on "Add to cart" button in the navigation panel
    And Click on the "View cart & check out" button in navigation panel
    Then Cart page is displayed with the added item and correct subtotal