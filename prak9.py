# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:18:04 2024

@author: kusfi
"""

import math

class BangunRuang:
    def volume(self, *args):
        if len(args) == 1:
            # Volume Kubus
            sisi = args[0]
            return sisi ** 3
        elif len(args) == 3:
            # Volume Balok
            panjang, lebar, tinggi = args
            return panjang * lebar * tinggi
        elif len(args) == 2:
            # Volume Tabung
            jari_jari, tinggi = args
            return math.pi * jari_jari ** 2 * tinggi
        else:
            return "Jumlah argumen salah, tidak bisa untuk menghitung volume"

bangun_ruang = BangunRuang()
print("===============================\nNama : Syahrul Arifin\nNIM : 064002300031\n===============================")
print("Volume Kubus dengan sisi 5 adalah :", bangun_ruang.volume(5))
print("Volume Balok dengan panjang 3, lebar 4, dan tinggi 7 adalah :", bangun_ruang.volume(3, 4, 5))
print("Volume Tabung dengan jari-jari 2 dan tinggi 6 adalah :", bangun_ruang.volume(2, 6))
