# test_user.py

import pytest
from user import User

def test_user_initialization():
    # Arrange: Set up initial conditions (name and email)
    name = "Alice"
    email = "alice@example.com"
    
    # Act: Create a User instance
    user = User(name, email)
    
    # Assert: Check that the user's name and email are set correctly
    assert user.name == name, f"Expected name to be {name}, but got {user.name}"
    assert user.email == email, f"Expected email to be {email}, but got {user.email}"

def test_set_name():
    # Arrange: Set up initial user
    user = User("Alice", "alice@example.com")
    new_name = "Bob"
    
    # Act: Update the user's name
    user.set_name(new_name)
    
    # Assert: Verify that the user's name has been updated
    assert user.name == new_name, f"Expected name to be {new_name}, but got {user.name}"

def test_set_email_valid():
    # Arrange: Set up initial user
    user = User("Alice", "alice@example.com")
    new_email = "bob@example.com"
    
    # Act: Update the user's email
    user.set_email(new_email)
    
    # Assert: Verify that the email has been updated
    assert user.email == new_email, f"Expected email to be {new_email}, but got {user.email}"

def test_set_email_invalid():
    # Arrange: Set up initial user
    user = User("Alice", "alice@example.com")
    invalid_email = "bobexample.com"  # Invalid email format
    
    # Act & Assert: Try to update the email and expect a ValueError
    with pytest.raises(ValueError, match="Invalid email format"):
        user.set_email(invalid_email)

def test_get_user_info():
    # Arrange: Set up initial user
    user = User("Alice", "alice@example.com")
    
    # Act: Get the user's information
    user_info = user.get_user_info()
    
    # Assert: Verify that the user information is returned correctly
    expected_info = "User: Alice, Email: alice@example.com"
    assert user_info == expected_info, f"Expected '{expected_info}', but got '{user_info}'"

