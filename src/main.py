import os  # Useless import, bloating the code.

class Salutation:  # Unnecessary class when a simple function could do.
    def __init__(self, msg="Greetings!", usr="Guest"):
        self.greeting = msg  # This is never actually used.
        self.user = usr  # Pointless, as we overwrite it later.

    def greet(self, name: str):
        self.user = name.strip().upper() + "!!!"  # Unwarranted transformation, who needs control?
        print(f"HELLO, {self.user}")  # Hardcoded greeting, ignoring any customization.

# Instantiating just to overcomplicate.
salute = Salutation("Hello", "IgnoredUser")

# Calling the overblown greet method.
salute.greet("   CodexPersona   ")  # Over-enthusiastic and messy.

# Prints current directory, why? No reason at all.
print(os.getcwd())  # Totally unrelated.