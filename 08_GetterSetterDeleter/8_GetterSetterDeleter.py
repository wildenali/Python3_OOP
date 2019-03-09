# decorator yg namanya @property  ,, merubah sebuah method menjadi seperti variable

# ini cara encapsulation dengan menggunakan @property

class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

        # awalnya ini
        # self.info = "name {} : \n\thealth: {}".format(self.name, self.__health)

    @property   # decorator yg namanya @property  ,, merubah sebuah method menjadi seperti variable
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter   # ini untuk menampilkan aja
    def armor(self):
        return self.__armor

    @armor.setter   # ini untuk mengubah
    def armor(self, input):
        self.__armor = input

    @armor.deleter  # ini untuk menghapus aja
    def armor(self):
        print('armor di delet')
        self.__armor = None

sniper = Hero('sniper', 100, 10)

print('merubah info')
print(sniper.info)
sniper.name = 'dadang'
print(sniper.info)

print('getter dan setter untuk __armor')
print(sniper.armor)
print(sniper.__dict__)
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)

print('delete armor')
del sniper.armor
print(sniper.armor)
print(sniper.__dict__)


""" outputnya
merubah info
name sniper :
	health: 100
name dadang :
	health: 100
getter dan setter untuk __armor
10
{'_Hero__health': 100, '_Hero__armor': 10, 'name': 'dadang'}
50
{'_Hero__health': 100, '_Hero__armor': 50, 'name': 'dadang'}
delete armor
armor di delet
None
{'_Hero__health': 100, '_Hero__armor': None, 'name': 'dadang'}
"""
