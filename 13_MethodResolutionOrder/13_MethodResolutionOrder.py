# Method resolution order // multiple inheritance
# URUTAN ekesekusinya nya

class A:
    def show(self):
        print("ini adalah show A")

class B:
    def show(self):
        print("ini adalah show B")

class C(B,A):
    pass

objek = C()
objek.show()
# cara melihat urutan eksekusinya adalah
help(objek)
