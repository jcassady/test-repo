from time_utils import time_travel, random_event, travel_back

if __name__ == "__main__":
    print("🕹️ Welcome to the Time Machine! ⏳")
    destinations = ["the Past", "the Future", "a Parallel Universe", "the Age of Dinosaurs]
    for dest in destinations:
        time_travel(dest)
        event = random_event()
        print(f"📜 In {dest}, you {event}")
        travel_back()
        
    print("🔚 Time travel adventure complete! Thanks for traveling! 🚀")
