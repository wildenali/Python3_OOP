class Hero:

    # private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # Method ini hanya berlaku untuk objek, tidak bisa dipakai untuk class
    def getJumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk objek, tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    # method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    # @classmethod nempel di class,
    @classmethod
    def getJumlah3(cls):    # cls hanya contoh, bisa di ganti apa aja, yg ini lebih elegan, karena langsung ke class nya
        return cls.__jumlah

    # @staticmethod dan @classmethod hampir sama aja, bedanya cuma di return nya aja, lebih elegan pakai @classmethod karena jika nama kelasnya berubah, maka dia balak ngikutin
    # tapi kalau pakai @staticmethod, misal Hero nya di ganti jadi Jawara, maka
    # return Hero.__jumlah harus diubah menjadi return Jawara.__jumlah

sniper = Hero('sniper')
# print(Hero.__jumlah)    # kita tidak bisa mengakses ini, karea ini private variable di class, supaya bisa di akses, bikin def getJumlah(self)
# print(Hero.getJumlah())   # ini juga bakal error
print(sniper.getJumlah())   # kalau ini bisa, tapi kan ini nempel di si objek snipper, pengennya nempel di si class Hero


# nah jadi kalau mau bisa akses si __jumlah , pakai @staticmethod   maka dia akan nempel di class Hero
print(Hero.getJumlah2())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah2())
drowranger = Hero('drowranger')
print(Hero.getJumlah3())


"""output
1
1
2
3
"""
