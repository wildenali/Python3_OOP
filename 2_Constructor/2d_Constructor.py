# Constructor adalah method yang akan dipanggil pertama kali secara otomatis
# perbedaannya sama method biasa seperti class adalah dia harus di panggil manual

# Constructor yang digunakan adalah __init__
class Gorengan:
    def __init__(self, namagorengan, hargagorengan): #self itu adalah gorengan1, gorengan2, dll
        self.nama = namagorengan
        self.harga = hargagorengan

gorengan1 = Gorengan("cireng", 500)
gorengan2 = Gorengan("gehu", 1500)

print(gorengan1.__dict__)   # __dict__ -> cara melihat isi dari object gorengan1
print(gorengan2.__dict__)
print(gorengan1.nama)
print(gorengan2.nama)
print(gorengan1.harga)
print(gorengan2.harga)
