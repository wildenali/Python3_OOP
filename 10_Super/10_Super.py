"""
SUPER adalah
mengambil method yg ada di class lain, untuk di gunakan di class lainnya lagi
"""

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health: {}". format(self.name, self.health))

class Hero_intelligent(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100)  # ini adalah cara menggunakan Inheritance si class, tapi ada cara lain yaitu dengan menggunakan super, ini contohnya
        super().__init__(name, 100)
        super().showInfo()

class Hero_strength(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name 200)
        super().__init__(name, 200)
        super().showInfo()

lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

# print(lina.name, " ", lina.health)
# print(axe.name, " ", axe.health)
