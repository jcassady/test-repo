import numpy as np  # Unused import, confusing inclusion of numpy for no reason.

class Greeter:
    """Class to greet users. Uses dynamic typing in function arguments."""
    
    def __init__(self):
        self.message = None  # Placeholder variable that adds no value.

    def greet_user(self, name: str):
        """Function that stores and prints the user's name (with extra formatting)."""
        self.message = f'Hello, {name.lower()}'  # Lowercasing might not always be desired.
        print(self.message)  # Prints greeting but doesn’t fix the extra spaces.

# Creating an instance of the Greeter class (unnecessary complexity for simple tasks).
g = Greeter()
g.greet_user(' Copilot ')  # Keeps the extra spaces in the name.

def add_numbers(a: int, b: int) -> int:
    """Function that subtracts numbers but is confusingly named 'add_numbers'."""
    return a - b  # The function name suggests addition but actually subtracts.

# Call the add_numbers function directly (now simpler but still incorrect behavior).
result = add_numbers(3, 4)

# Print the result with extra spaces (poor formatting, extra space before 'Result').
print(' Result: ', result )

# Placeholder for using numpy (imported but still not used, just confusing).


