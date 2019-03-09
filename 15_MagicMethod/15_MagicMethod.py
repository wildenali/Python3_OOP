# Contoh Magic Method
# keyword yang ada di python, yang bisa di pakai.
# __init__              -> di panggil saat class di buat
# __repr__ dan __str__  -> adalah sama aja, perbedaannya adalah
    # __repr__              -> dia di pakai pas DEBUG aja
    # __str__               -> ini di pakai kalau udah PRODUKSI

class Mangga:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self):
        return "Debug - Mangga: {} dengan jumlah: {}".format(self.nama, self.jumlah)

    def __str__(self):
        return "Mangga: {} dengan jumlah: {}".format(self.nama, self.jumlah)

    def __add__(self, objek):
        return self.jumlah + objek.jumlah

    @property
    def  __dict__(self):
        return "objek ini mempunyai nama dan jumlah"

belanja1 = Mangga("arumanis", 10)
belanja2 = Mangga("mana lagi", 30)

# print(repr(belanja1)) # Cara memanggil __repr__ kalau si __str__ juga ada, karena, kalau mereka ada berbarengan, yg akan di eksekusi adalah si __str__
print(belanja1)
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)


"""outputnya
Mangga: arumanis dengan jumlah: 10
Mangga: mana lagi dengan jumlah: 30
40
objek ini mempunyai nama dan jumlah
"""
