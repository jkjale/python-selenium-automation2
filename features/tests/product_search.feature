Feature: Product Search functionality

  Scenario: User can search for a product
    Given Open Target.com
    When Input tea into search field
    And Click on search icon
    Then Product results for tea are shown