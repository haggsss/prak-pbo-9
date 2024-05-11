# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:11:39 2024

@author: kusfi
"""

class P9e2:
    @staticmethod
    def methodTambah(x, y=None):
        if y is None:
            return 4.5 * x  # Jika hanya satu argumen, maka kembalikan hasil perkalian dengan 4.5
        else:
            return x + y    # Jika dua argumen, kembalikan hasil penjumlahan
    
myNum1 = P9e2.methodTambah(8)    # Akan menggunakan metode untuk float
myNum2 = P9e2.methodTambah(8, 5)  # Akan menggunakan metode untuk integer
myNum3 = P9e2.methodTambah(6.5, y=6.5)  # Akan menggunakan metode untuk float
print("int:", myNum1)
print("int:", myNum2)
print("float:", myNum3)

