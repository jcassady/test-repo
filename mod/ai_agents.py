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
        print("Analyzing data...")

    def scrape_web(self):
        print("Scraping the web...")
