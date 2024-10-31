import random

class AIAgent:
    def __init__(self, name, task):
        self.name = name
        self.task = task
        self.haunted_level = random.randint(1, 10)  # Spooky: Random haunted level

    def introduce(self):
        print(f"👻 Hello, I am {self.name}, and my task is {self.task}")
        print("hello {person}")  # Static string, not doing anything useful
        if self.haunted_level > 5:
            print("😱 Beware, I am haunted!")

    def analyze_datas(self):
        print("🔮 Analyzing data with mystical powers...")
        for i in range(3):
            print(f"🔪 Step {i+1}...")  # Fixed non-pythonic indentation
        self.cause_havoc()  # Spooky: Calling a bogus method to cause havoc

    def cause_havoc(self):
        print("🕷️ Causing havoc... 👻")
        try:
            result = "mystery" + 1  # Bogus: Concatenation of string and int
        except TypeError as e:
            print(f"Error: {e}. 🦇 Something eerie just happened!")

    def perform_tasker(self):
        if self.task == "data analysis":
            self.analyze_datas()
        elif self.task == "haunt":
            self.haunt()  # Spooky: Added haunt task
        else:
            print("🚫 Task not defined")

    def haunt(self):
        print("🕸️ Haunting the system... 🎃")
        for i in range(5):
            print(f"💀 Boo! Spooky action {i+1}...")

if __name__ == "__main__":  # Fixed syntax error
    agent1 = AIAgent("Alpha", "data analysis")
    agent1.introduce()
    agent1.perform_tasker()

    agent2 = AIAgent("Beta", "haunt")
    agent2.introduce()
    agent2.perform_task()
