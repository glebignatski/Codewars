import sys
import re

def validate_password(password):
    m = p.match(password)
    if m is not None:
        return "Matched"
    else:
        return "Not matched"
    # Password must be:
                        # At least 6 characters long
                        # At least one lowercase letter
                        # At least one uppercase letter
                        # At least one digit
                        # Not special characters allowed

regex = r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])[A-Za-z0-9]{6,}$" # [0-9] can be replaced with [\d]

p = re.compile(regex)
print(validate_password(sys.argv[1]))