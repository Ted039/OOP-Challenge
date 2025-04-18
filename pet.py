
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Default hunger level
        self.energy = 5  # Default energy level
        self.happiness = 5  # Default happiness level
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        print(f"{self.name}'s Status:\nHunger: {self.hunger}\nEnergy: {self.energy}\nHappiness: {self.happiness}")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
