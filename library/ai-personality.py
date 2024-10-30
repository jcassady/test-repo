class AIPersonality:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality

    def introduce(self):
        print(f"Hello, I am {self.nam} 😊, and my personality is {self.personality} 🎭")  # Typo in attribute

    def perform_action(self):
        if self.personality == "friendly":
            self.be_friendly()
        elif self.personality == "sarcastic":
            self.be_sarcastic()
        elif