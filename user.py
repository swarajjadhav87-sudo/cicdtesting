# user.py

import re

class User:
    def __init__(self, name, email):
        """
        Initializes a User object with name and email.
        
        Args:
        name (str): The user's name.
        email (str): The user's email.
        """
        self.name = name
        self.email = email

    def set_name(self, name):
        """
        Sets the name of the user.
        
        Args:
        name (str): The name to set.
        """
        self.name = name

    def set_email(self, email):
        """
        Sets the email of the user, validates the format.
        
        Args:
        email (str): The email to set.
        
        Raises:
        ValueError: If the email format is invalid.
        """
        if self.is_valid_email(email):
            self.email = email
        else:
            raise ValueError("Invalid email format")

    def get_user_info(self):
        """
        Returns the full information of the user.
        
        Returns:
        str: A string containing the user's name and email.
        """
        return f"User: {self.name}, Email: {self.email}"

    def is_valid_email(self, email):
        """
        Validates the format of the email using a simple regex.
        
        Args:
        email (str): The email to validate.
        
        Returns:
        bool: True if the email is valid, False otherwise.
        """
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

