# Validators file has been used to validate the password with different conditions.
import re # regular expressions are used to check the password conditions
from django.core.exceptions import ValidationError

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8 or len(password) > 14:
            raise ValidationError("Password must be between 8 and 14 characters.")

        # checking for atleast 1 uppercase character - [A-Z]
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        # checking for atleast 1 lowercase character - [a-z]
        if not re.search(r'[a-z]', password):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'\d', password):
            raise ValidationError("Password must contain at least one digit.")
        if not re.search(r'[@$!%*?&]', password):
            raise ValidationError("Password must contain at least one special character.")

    def get_help_text(self):
        return "Password must be 8-14 chars, include upper, lower, number, special character."