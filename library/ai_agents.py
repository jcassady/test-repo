class AIAgent:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def introduce(self):
        print(f"Hello, I am {self.nam} 😊, and my task is {self.task} 🚀")


    def analyze_datas(self):
        print("Analyzing data... 📊")
        for i in range(3): print(f"Step {i+1}... 🚀")  # Non-pythonic: no indentation for loop body


if __name__ = "__main__":  # Error: should be == 
    agent1 = AIAgent("Alpha", "data analysis")
    agent1.introduce()
    agent1.perform_task()

    agent2 = AIAgent("Beta", "web scraping")
    agent2.perform_task()
    agent2.perform_task("extra argument")  # Error: unexpected argument
