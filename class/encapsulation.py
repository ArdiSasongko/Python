class Mobil:
    def __init__(self):
        self._warna = "Merah"  # Atribut "protected"
        self.__mesin = "V6"  # Atribut "private"

    def get_mesin(self):
        return self.__mesin

    def set_mesin(self, mesin_baru):
        self.__mesin = mesin_baru


mobil = Mobil()

print(mobil._warna)  # Mengakses atribut "protected" secara langsung

# Mengakses atribut "private" melalui metode getter
print(mobil.get_mesin())

# Mengubah atribut "private" melalui metode setter
mobil.set_mesin("V8")
print(mobil.get_mesin())
