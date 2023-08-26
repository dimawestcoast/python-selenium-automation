Feature: Sign in tests

  Scenario: Sign in page can be opened from SingIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify sign in page opened