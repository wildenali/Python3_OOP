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

"""ini outputnya adalah
ini adalah show B
"""
# terus kenapa ini adalah show A nya ga KELUAR coba?
# cara cek nya adalah
"""
cara melihat urutan eksekusinya adalah
help(objek)
"""

help(objek)

""" bakal keluar informasi seperti berikut, jadi ini urutan programnya
Help on C in module __main__ object:

class C(B, A)
 |  Method resolution order:
 |      C
 |      B
 |      A
 |      builtins.object
 |
 |  Methods inherited from B:
 |
 |  show(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from B:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
(END)
"""
