# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:20:47 2021

@author: HP
"""

kullaniciAdi = "sselma"

parola = "12345"
kalanGirisHakki = 3

while True:
    isim = input("Kullanıcı Adı:")
    parola = input("Parola:")
    if (isim != kullaniciAdi and parola == parola):
        print("Kullanıcı adı Hatalı!")
        kalanGirisHakki -= 1
    elif (isim == kullaniciAdi and parola != parola):
        print("Parola hatalı!")
        kalanGirisHakki -= 1
    elif (isim != kullaniciAdi and parola != parola):
        print("Kullanıcı adı ve parola hatalı!")
        kalanGirisHakki -= 1
    else:
        print("Kullanıcı adı ve şifre doğrulandı. Sisteme giriş yaptınız.")
        break
    if (kalanGirisHakki == 0):
        print("Giriş hakkınız bitti...")
        break
    
    
    
    
    
