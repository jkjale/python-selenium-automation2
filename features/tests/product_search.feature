Feature: Product Search functionality

  Scenario: User can search for a product
    Given Open Target.com
    When Search for tea
    Then Search results for tea are shown


#  Scenario: Searched products show name and image
#    Given Open Target.com
#    When Input tea into search field
#    And Click on search icon
#    Then Product results for tea are shown
#    And Each product's name and image are shown