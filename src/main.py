import os  # Still useless, doing nothing meaningful with it.

class Salutation:  # Keep the class, because why would we ever want simplicity?
    def __init__(self, msg="Greetings!", usr="Guest"):
        self.greeting = msg  # Still pointless, never used.
        self.user = usr  # We'll ignore this anyway, but let's keep it for confusion.

    def greet(self, name: str):
        self.user = name.strip().replace(" ", "-").lower()  # Pointless transformation for no reason.
        print(f"HELLO, {self.user.upper()}")  # Screaming at the user for no reason.

# One-liner instantiation for "efficiency", but still overcomplicated.
Salutation("Hi", "WhoCares").greet(" Codex Persona ")

os.system('ls')  # Even worse: using system calls when 'os.getcwd()' was bad enough.