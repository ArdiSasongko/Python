#membuat class
class Cat:
    def characteristic(self, color, height, weight):
        self.__color = color
        self.__height = height
        self.__weight = weight
    def cat(self):
        print("Kucing ini berwarna", self.__color, "tinggi", self.__height, "cm dan berat", self.__weight, "kg")


jenis = input("Masukan Jenis kucing ")
warna = input("Masukan Warna kucing ")
tinggi = input("Masukan Tinggi kucing ")
berat = input("Masukan Berat kucing ")

#membuat instance dari class
jenis = Cat()
jenis.characteristic(warna,tinggi,berat)
jenis.cat()