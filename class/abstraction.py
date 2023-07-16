from abc import ABC, abstractmethod

class Bentuk(ABC): #buat class parent
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

class Persegi(Bentuk): #buat child class
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi

class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def luas(self):
        return 3.14 * self.radius ** 2

    def keliling(self):
        return 2 * 3.14 * self.radius

#untuk mengakses fungsi pada class parent kita tidak bisa mengakses secara langsung melalui objec
#tetapi harus membuat child class yang mewarisi fungsi dari parent class
persegi = Persegi(5)
print("Luas persegi:", persegi.luas())
print("Keliling persegi:", persegi.keliling())

lingkaran = Lingkaran(3)
print("Luas lingkaran:", lingkaran.luas())
print("Keliling lingkaran:", lingkaran.keliling())
