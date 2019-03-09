# Constructor adalah method yang akan dipanggil pertama kali secara otomatis
# perbedaannya sama method biasa seperti class adalah dia harus di panggil manual

# Constructor yang digunakan adalah __init__
class Gorengan:
    jumlah = 0 # class variable

    def __init__(self, namagorengan, hargagorengan): #self itu adalah gorengan1, gorengan2, dll
        self.nama = namagorengan    # instance variable
        self.harga = hargagorengan  # instance variable
        Gorengan.jumlah += 1
        print("Gorengan " + namagorengan)

gorengan1 = Gorengan("cireng", 500)
print(Gorengan.jumlah)
gorengan2 = Gorengan("gehu", 1500)
print(Gorengan.jumlah)
print(Gorengan.__dict__)


""" hasil di console
Gorengan cireng
1
Gorengan gehu
2
{'__dict__': <attribute '__dict__' of 'Gorengan' objects>, 'jumlah': 2, '__init__': <function Gorengan.__init__ at 0x7fec444947b8>, '__module__': '__main__', '__weakref__': <attribute '__weakref__' of 'Gorengan' objects>, '__doc__': None}
"""
