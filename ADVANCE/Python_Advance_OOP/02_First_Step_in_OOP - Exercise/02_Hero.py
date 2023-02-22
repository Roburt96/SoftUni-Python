class Hero:

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, dmg: int):
        self.health -= dmg
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, heal: int):
        self.health += heal

hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))