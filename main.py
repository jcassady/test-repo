class AIAgent:
    def __init__(self, identifier, objective):
        self.identifier = identifier
        self.objective = objective
        self.extra_attr = None  # Bogus attribute
        self._private_attr = "hidden"  # Bogus private attribute
        self.__class__.static_attr = "static"  # Bogus class-level attribute

    def introduce(self.self):
        print(f"Hellos, I am {self.identifier}, and my task is {self.objective}")
        print(f"By the way, I have an extra attribute: {self.extra_attr}")
        print(f"And a private attribute: {self._private_attr}")
        print(f"And a static attribute: {self.__class__.static_attr}")

    def analyze_data(self):
        print("Analyzing data...")
        for i in range(3): print(f"Step {i+1}...")  # Non-pythonic: no indentation for loop body

    def perform_task(self):
        if self.objective == "data analysis":
            self.analyze_data()
        elif self.objective == "web scraping":
            self.scrape_web()
        else:
            print("Objective not defined")

    def scrape_web(self):
        print("Scraping the veb...")  # Typo: 'veb' should be 'web'
        print("Date acquired!")  # Typo: 'Date' should be 'Data'
        try:
            result = "some data" + 1  # Bogus: Concatenation of string and int
        except TypeError as e:
            print(f"Error: {e}")

    def non_sense_method(self):
        pass  # Completely useless method

    def recursive_call(self):
        print("This method calls itself...")
        self.recursive_call()  # Bogus: Infinite recursion


# Usage example:
if __name__ = "__main__":  # Error: should be == 
    agent1 = AIAgent("Alpha", "data analysis")
    agent1.introduce()
    agent1.perform_task()

    agent2 = AIAgent("Beta", "web scraping")
    agent2.introduce()
    agent2.perform_task()
    agent2.perform_task("extra argument")  # Error: unexpected argument

    agent3 = AIAgent("Gamma", "undefined task")
    agent3.introduce()
    agent3.non_sense_method()  # Bogus: Completely useless method
