import time
import random

def spooky_greeting():
    print("👻🎃 Welcome to the Spooky Python Halloween Party! 🎃👻")
    
def pick_costume():
    costumes = ["🧛‍♂️ Vampire", "👻 Ghost", "🧟 Zombie", "🦇 Bat", "🎃 Pumpkin"]
    costume = random.choice(costumes)
    print(f"Tonight, you will be dressed as: {costume}")

def trick_or_treat():
    treats = ["🍬 Candy", "🍫 Chocolate", "🍭 Lollipop", "🍪 Cookie", "🧁 Cupcake"]
    trick_or_treat_result = random.choice(["Trick", "Treat"])
    if trick_or_treat_result == "Treat":
        treat = random.choice(treats)
        print(f"Treat time! You got a {treat}!")
    else:
        print("Uh oh! It's a trick! 🎃 Better luck next time!")

def spooky_story():
    stories = [
        "Once upon a time, in a haunted mansion... 👻🏚️",
        "In the dark of the night, the wind whispered... 🌬️🦇",
        "Beneath the full moon, shadows came alive... 🌕🧟",
        "A mysterious figure appeared at midnight... ⏳🧛‍♂️",
        "The cemetery gates creaked open, revealing... ⚰️👻"
    ]
    story = random.choice(stories)
    print(f"Story time: {story}")

if __name__ == "__main__":
    spooky_greeting()
    pick_costume()
    for _ in range(3):  # Let's do trick-or-treat 3 times
        trick_or_treat()
        time.sleep(1)  # Pause for dramatic effect
    spooky_story()
    print("🎃👻 Thanks for celebrating Halloween with Python! 🎃👻")
