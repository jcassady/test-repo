import time
import random

def time_travel(destination):
    print("🔧 Winding up the time machine... 🕰️")
    time.sleep(2)
    print(f"🌟 Traveling to {destination}... 🚀")
    time.sleep(3)
    print(f"✨ Arrived in {destination}! 🌐")

def random_event():
    events = [
        "🐲 Encounter a dragon!",
        "👽 Meet some friendly aliens!",
        "🏰 Visit a medieval castle!",
        "🦖 Run from a T-Rex!",
        "🚢 Sail the seven seas with pirates!"
    ]
    return random.choice(events)

if __name__ == "__main__":
    print("🕹️ Welcome to the Time Machine! ⏳")
    destinations = ["the Past", "the Future", "a Parallel Universe", "the Age of Dinosaurs"]
    for dest in destinations:
        time_travel(dest)
        event = random_event()
        print(f"📜 In {dest}, you {event}")
        print("🔄 Returning to the present... ⏰")
        time.sleep(2)
        print("🏡 Back in the present! 🏠\n")

    print("🔚 Time travel adventure complete! Thanks for traveling! 🚀")
