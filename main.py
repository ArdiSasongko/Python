#latihan input

panjang = int(input("Masukan panjang : "))
lebar = int(input("Masukan lebar : "))

result = panjang*lebar

#nested if-else
if result >= 100 :
    print(str(result) + " besar dari 100")
    if result % 2 == 0 :
        print("Bilangan Genap")
    else :
        print("Bilangan Ganjil")
elif result >= 20 :
    print(str(result) +" besar dari 20")
    if result % 2 == 0 :
        print("Bilangan Genap")
    else :
        print("Bilangan Ganjil")
else :
    print(str(result) +" Kecil dari 20")
    if result % 2 == 0 :
        print("Bilangan Genap")
    else :
        print("Bilangan Ganjil")


