# Base class
class Superhero:
    def __init__(self, name, power, costume_color):
        self.name = name
        self.power = power
        self.costume_color = costume_color

    def show_details(self):
        print(f"{self.name} wears a {self.costume_color} costume and has the power of {self.power}.")

    def move(self):
        print(f"{self.name} moves mysteriously...")  # Default move (can be overridden)


# Subclass 1
class FlyingHero(Superhero):
    def move(self):
        print(f"{self.name} flies through the sky! ✈️")


# Subclass 2
class StrongHero(Superhero):
    def move(self):
        print(f"{self.name} smashes through walls! 💪")


# Creating objects
hero1 = FlyingHero("SkyShadow", "flight", "blue")
hero2 = StrongHero("RockBreaker", "super strength", "red")

# Showing details and demonstrating polymorphism
hero1.show_details()
hero1.move()  # Should show flying behavior

print()  # Spacer

hero2.show_details()
hero2.move()  # Should show smashing behavior
