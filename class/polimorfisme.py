class People:
    def __init__(self, name, kendaraan):
        self._name = name
        self._kendaraan = kendaraan

    def kegiatan(self):
        pass

    def kendaraan(self):
        pass

class Pelajar(People):
    def __init__(self, name, kendaraan):
        super().__init__(name, kendaraan)

    def kegiatan(self):
        print(self._name, "Belajar di sekolah")
    
    def kendaraan(self):
        print("Ke sekolah menggunakan kendaraan umum yaitu", self._kendaraan)

class Karyawan(People):
    def kegiatan(self):
        print("Bekerja di kantor")
    
    def kendaraan(self):
        print("Ke kantor menggunakan kendaraan umum yaitu", self._kendaraan)

Budi = Pelajar("Budi", "Motor Beat")
Joko = Karyawan("Joko", "Mobil Sedan")

for objek in (Budi, Joko):
    objek.kegiatan()
    objek.kendaraan()
