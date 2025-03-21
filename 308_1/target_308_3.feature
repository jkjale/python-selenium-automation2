Feature: Verify navigation to Sign In page for a logged-out user
  In order to access my account
  As a logged-out user
  I want to be able to navigate to the Sign In page

  Scenario: Navigating to Sign In page
    Given Open Target.com
    When Click the "Sign In" link on the homepage
    And Click the "Sign In" button from the right side navigation menu
    Then "Sign In" form is shown