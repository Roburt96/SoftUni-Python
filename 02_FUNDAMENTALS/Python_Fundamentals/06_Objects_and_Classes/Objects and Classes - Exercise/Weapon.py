class Weapon:

    def __init__(self, bullets):   # ----> Weapon(5)
        self.bullets = bullets    # -----> 5

    def shoot(self):
        for _ in range(self.bullets):
            self.bullets -= 1
            return "shooting..."
        if self.bullets == 0:
            return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
