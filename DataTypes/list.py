numbers = [10,40,15,21,55,45]

#Panjang List
print(len(numbers))


# #print list
# print(numbers)
# #print index list
# print(numbers[0])
# #mengakses dengan negatif, dimulai dari akhir list
# print(numbers[-6])


#addition dan deletion pada list

#(+) digunakan untuk menggabungkan list

data1 = ["Joko", 15, 165, 50]
data2 = ["Budi", 18, 166, 52]
allData = data1 + data2
print(allData)
print(" ")
#append(). digunakan untuk menambahkan single value ke list
print(data1)
data1.append("Jakarta")
print(data1)
print(" ")
#extend() menambhakn list ke belakang list
print(data2)
data3 = ["Pojo", 22, 170, 66]
print(data3)
data2.extend(data3)
print(data2)
print(" ")
#del untuk menghapus index dalam list
angka = [0,1,2,3,4,5,6,7,8]
print(angka)
del angka[0]
print(angka)
print(" ")
#pop() menghapus value index terakhir pada list
angka.pop()
print(angka)
print(" ")
#remove digunakan untuk menghapus value tanpa mengetahui index ke berapa
angka2 = [1,2,3,2,5,2,8,10]
print(angka2)

while 2 in angka2:
    angka2.remove(2)

print(angka2)
print(" ")
#slicing, mengambil index tertentu dari list
angka3 = [1,2,3,4,5,6,7,8,9,10]
print(angka3)
print(angka3[2:5])
print(" ")

#in digunakan untuk menghasilakn boolean
print(5 in angka3) #true
print(11 in angka3) #false
print(5 not in angka3) #false
print(11 not in angka3) #true