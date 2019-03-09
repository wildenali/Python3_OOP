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

""" hasilnya
{'name': 'lina', 'health': 100, '_Hero__private': 'privatecoy', '_protected': 'protectedbang'}
100
{'name': 'lina', 'health': 100, '_Hero__private': 'privatecoy', '_protected': 'protectedbang'}
protectedbang
{'name': 'lina', 'health': 100, '_Hero__private': 'privatecoy', '_protected': 'testing'}
testing
{'__dict__': <attribute '__dict__' of 'Hero' objects>, '__doc__': None, '_Hero__privateJumlah': 0, '__init__': <function Hero.__init__ at 0x7f0191677730>, 'jumlah': 0, '__weakref__': <attribute '__weakref__' of 'Hero' objects>, '__module__': '__main__'}
"""
