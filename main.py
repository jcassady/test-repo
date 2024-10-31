class AIAgent:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def introduce(self.self):
        print(f"Hellos, I am {self.name}, and my task is {self.task}")



    def analyze_data(self):
        print("Analyzing data...")  # Error: Method not defined


# Usage example:
if __name__ == "__main__":  # Error: Should be 'if __name__ == "__main__":'
    agent1 = AIAgent("Alpha", "data analysis")
    agent1.introduce()
    agent1.perform_task

    agent2 = AIAgent("Beta", "web scraping")
    agent2.introduce()
    agent2.perform_task()
