class Hero:
    # class Variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # variable instance private
        self.__private = "privatecoy"

        # variable instance protected
        self._protected = "protectedbang"

lina = Hero("lina", 100)
print(lina.__dict__)
print(lina.health)
# print(lina.__private)   # kalau ini di aktifin maka, akan error pas di line ini, karena __private tidak bisa di akses
print(lina.__dict__)
print(lina._protected)
lina._protected = "testing"
print(lina.__dict__)
print(lina._protected)


# testing __privateJumlah
print(Hero.__dict__)
# print(Hero.__privateJumlah)  # tidak bisa di akses, karena private
