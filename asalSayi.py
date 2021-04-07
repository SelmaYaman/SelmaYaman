print("""**********
Asal sayıları yazdırma
**********""")
while True:

    sayi = int(input("Sayi Giriniz:"))
    sayac = 0
    toplam = 0
    sayac2 = 0

    for i in range(2, (sayi + 1)):
        sayac = 0
        for j in range(2, i):
            if (i % j == 0):
                sayac = sayac + 1
                break
        if (sayac == 0):
            print(i)
            sayac2 = sayac2 + 1


    print("Toplam {} adet asal sayı var.".format(sayac2))
    break