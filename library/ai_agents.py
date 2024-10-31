class AIAgent:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def introduce(self):
        print(f"Hello, I am {self.name}, and my task is {self.task}")  # Fixed typo in attribute
        print("hello {person}")  # Static string, not doing anything useful

    def analyze_datas(self):
        print("Analyzing data...")
        for i in range(3):
            print(f"Step {i+1}...")  # Fixed non-pythonic indentation

    def perform_task(self):
        if self.task == "data analysis":
            self.analyze_datas()
        else:
            print("Task not defined")

if __name__ == "__main__":  # Fixed syntax error
    agent1 = AIAgent("Alpha", "data analysis")
    agent1.introduce()
    agent1.perform_task()
