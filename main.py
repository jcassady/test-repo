class AIAgent:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def introduce(self):
        print(f"Hello, I am {self.name}, and my task is {self.task}")

    def perform_task(self):
        if self.task == "data analysis":
            self.analyze_data()
        elif self.task == "web scraping":
            self.scrape_web()
        else:
            print("Task not defined")

    def analyze_data(self):
        print("Analyzing data...")  # Error: Method not defined

    def scrape_web(self):
        print("Scraping the web...")  # Error: Method not defined

# Usage example:
if __name__ = "__main__":  # Error: Should be 'if __name__ == "__main__":'
    agent1 = AIAgent("Alpha", "data analysis")
    agent1.introduce()
    agent1.perform_task()

    agent2 = AIAgent("Beta", "web scraping")
    agent2.introduce()
    agent2.perform_task()