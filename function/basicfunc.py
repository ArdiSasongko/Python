#Basic penggunaan function
def sum(m,n): #m dan n merupakan parameter
    return m+n

print(sum(10,20))

#* tanda tersebut digunakan untuk jumlah argumen yang tidak diketahui, digunakan pd perulangan
def greating(*name): 
    for i in name:
        print("Halo", i)

greating("Budi","Joko","Tingkir")

#Default parameter, jika kita tidak menyertakan argumen maka default paramter yang digunaka

def loop(n=1):
    for i in range(n):
        print("*")

loop() #tidak menyertakan argumen
loop(2)