class Gorengan:
    pass

gorengan1 = Gorengan()
gorengan2 = Gorengan()
gorengan3 = Gorengan()
gorengan4 = Gorengan()
gorengan5 = Gorengan()

gorengan1.nama = "bala-bala"
gorengan1.harga = 500

gorengan2.nama = "gehu"
gorengan2.harga = 550

gorengan3.nama = "cireng"
gorengan3.harga = 700

gorengan4.nama = "pisang"
gorengan4.harga = 800

gorengan5.nama = "karoket"
gorengan5.harga = 650

# cek gorengan, dia object atau bukan
print(gorengan1)

# cara cek isinya ada apa aja
print(gorengan1.__dict__)

# cara menggunakan attributnya gimana
print(gorengan1.nama)

print()

print(gorengan3.nama)
print(gorengan3.harga)
