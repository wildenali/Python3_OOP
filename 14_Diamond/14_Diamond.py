# diamond problem
"""
    A
   / \
  /   \
 B     C
  \   /
   \ /
    D

si D akan mengambil jalan yang mana?
jawabannya adalah B
dari D
ke   B
ke   C
ke   A
"""


class A:
    def show(self):
        print("ini adalah show A")

# coba yg class B di pass aja, hasilnya pasti si C
class B(A):
    def show(self):
        print("ini adalah show B")

class C(A):
    def show(self):
        print("ini adalah show C")

class D(B,C):
    pass

objek = D()
objek.show()
"""outputnya
ini adalah show B
"""

"""
cara tau kenapa dia outputnya adalag classB
check menggunkan
help(objek)
"""

help(objek)
"""outputnya
Help on D in module __main__ object:

class D(B, C)
 |  Method resolution order:
 |      D
 |      B
 |      C
 |      A
 |      builtins.object
 |
 |  Methods inherited from B:
 |
 |  show(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from A:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
(END)
"""
