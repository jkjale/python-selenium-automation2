Feature: Login functionality

  Scenario: Logged out user can access Sign In
    Given Open Target.com
    When Click Sign In
    Then From side navigation menu, click Sign In
    And Verify Sign In form opened


  Scenario: User is redirected to home page after signing in
    Given Open Target.com
    When Click Sign In
    Then From side navigation menu, click Sign In
    And Input username and password on Sign In page
    And Click Sign In button
    And Verify user is logged in and redirected to home page