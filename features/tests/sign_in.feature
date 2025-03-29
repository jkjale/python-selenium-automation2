Feature: Login functionality

#  Scenario: Logged out user can access Sign In
#    Given Open Target.com
#    When Click Sign In
#    Then From side navigation menu, click Sign In
#    And Verify Sign In form opened
#
#
#  Scenario: User is redirected to home page after signing in
#    Given Open Target.com
#    When Click Sign In
#    Then From side navigation menu, click Sign In
#    And Input username and password on Sign In page
#    And Click Sign In button
#    And Verify user is logged in and redirected to home page


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target.com
    When Click Sign In
    Then From side navigation menu, click Sign In
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original