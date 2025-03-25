Feature: Cart functionality on Target.com
  In order to ensure users can interact with the cart correctly
  As a customer
  I want to be able to see if my cart is empty when I visit it.

  Scenario: Verify the cart is empty
    Given Open Target.com
    When Click on the Cart icon
    Then "Your cart is empty" message is shown