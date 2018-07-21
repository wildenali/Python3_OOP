"""
Apa itu Encapsulasi (Menyembunyikan Informasi)???
Menjaga variable private di dalam constructor

Intinya si encapsulasi itu biar si variable class tidak mudah untuk di ubah dari luar class
"""

class Hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    """
    gini coy, kan si name itu di variable yg di private ya
    nah sekarang gimana caranya kita mengakses atau mengganti si variable yg private tersebut di luar class
    caranya adalah kita bikin dulu method, namanya
    GETTER dan SETTER
    """

    # getter, untuk menampilkan data aja
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter, untuk mengubah nilai si variable private tersebut
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self, nilaiBaru):
        self.__attPower = nilaiBaru

# awal dari game
eartshaker = Hero('eartshaker', 50, 5)

# game berjalan
print(eartshaker.getName())
print(eartshaker.getHealth())
eartshaker.diserang(5)
print(eartshaker.getHealth())
