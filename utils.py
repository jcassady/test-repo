import time
import random

def time_travel(destination):
    """Simulate time travel to a given destination."""
    print("🔧 Winding up the time machine... 🕰️")
    time.sleep(2)
    print(f"🌟 Traveling to {destination}... 🚀")
    time.sleep(3)
    print(f"✨ Arrived in {destination}! 🌐")
    
def random_event():
    """Generate a random event."""
    events = [
        "🐲 Encounter a dragon!",
        "👽 Meet some friendly aliens!",
        "🏰 Visit a medieval castle!",
        "🦖 Run from a T-Rex!",
        "🚢 Sail the seven seas with pirates!"
    ]
    return random.choice(events)

def travel_back():
    """Simulate traveling back to the present."""
    print("🔄 Returning to the present... ⏰")
    time.sleep(2)
    print("🏡 Back in the present! 🏠\n")
