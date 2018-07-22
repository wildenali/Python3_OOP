"""
OVERRIDE METHOD adalah
menimpa
"""

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("showInfo di class Hero")
        print("{} health: {}".format(
            self.name,
            self.health
            )
        )

class Hero_intelligent(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100)  # ini adalah cara menggunakan Inheritance si class, tapi ada cara lain yaitu dengan menggunakan super, ini contohnya
        super().__init__(name, 100)

    # override
    def showInfo(self):
        print("showInfo di subclass Hero_intelligent")
        print("{} \n\tTipe: intelligent, \n\thealth: {}".format(
            self.name,
            self.health
            )
        )


class Hero_strength(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name 200)
        super().__init__(name, 200)

lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

lina.showInfo()
axe.showInfo()

# jadi si show info si lina meng override showInfo nya si class Hero
# sedangkan si showInfo si axe, dia menggunakan showInfo si class Hero
