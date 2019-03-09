# Apa itu Methods?
"""
method itu adalah misalnya jika ada tombol nih
nah si tombolnya misalnya klo di klik(method) warnanya berubah
atau kalau tombolnya di klik maka bentuknya berubah
nah something yang berubah itu method
nah si method ini dapat digunakan berulang ulang
lah perbedaannya sama class apa dooong???
ya ga tau lah
ya bedalah
Gini gampangnya
Method ini seperti function, tetapi posisi dia ada di dalam class
nah, kalau function ini ada di luar class maka dia disebut ya function
kalau di dalam CLASS ya METHOD
gitu toh

ada method yang langsung berinteraksi dengan client,
ada yang berinteraksi dengan class lain

langsung aja ke CONTOH
"""
class Hero:
    # class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # === Nah ini nih yang di sebut METHODS ===
    # ini METHOD TANPA RETURN,tanpa ARGUMEN
    def siapa(self):
        print("namaku adalah " + self.name)

    # ini METHOD dengan ARGUMEN, TANPA RETURN
    def healthUp(self, up):
        self.health += up

    # ini METHOD dengan RETURN
    def getHealth(self):
        return self.health

hero1 = Hero('sniper', 100, 10, 5)
hero2 = Hero('mario bros', 90, 5, 10)

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa()
print(hero1.getHealth())
hero1.healthUp(1000)
print(hero1.getHealth())


""" hasil di console
{'health': 100, 'armor': 5, 'name': 'sniper', 'power': 10}
{'health': 90, 'armor': 10, 'name': 'mario bros', 'power': 5}
snipper
100
1100
"""
