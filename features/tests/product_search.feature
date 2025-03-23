Feature: Product Search functionality

  Scenario: User can search for a product
    Given Open Target.com
    When Search for tea
    Then Verify search results shown for tea
    And Verify tea in URL


#  Scenario: Searched products show name and image
#    Given Open Target.com
#    When Input tea into search field
#    And Click on search icon
#    Then Product results for tea are shown
#    And Each product's name and image are shown