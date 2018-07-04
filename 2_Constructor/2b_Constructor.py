# Constructor adalah method yang akan dipanggil pertama kali secara otomatis
# perbedaannya sama method biasa seperti class adalah dia harus di panggil manual

# Constructor yang digunakan adalah __init__
class Gorengan:
    def __init__(self, x): #self itu adalah gorengan1, gorengan2, dll
        print("cireng", x)

gorengan1 = Gorengan(1000)
gorengan2 = Gorengan(1500)
