# Constructor adalah method yang akan dipanggil pertama kali secara otomatis
# perbedaannya sama method biasa seperti class adalah dia harus di panggil manual

# Constructor yang digunakan adalah __init__
class Gorengan:
    def __init__(self, namagorengan): #self itu adalah gorengan1, gorengan2, dll
        self.nama = namagorengan

gorengan1 = Gorengan("cireng")
gorengan2 = Gorengan("gehu")

print(gorengan1.nama)
print(gorengan2.nama)

""" hasil di console
cireng
gehu
"""
