def pkt(nilai,pangkat):
    result1 = nilai**pangkat
    result2 = nilai*pangkat
    return result1, result2

r1,r2 = pkt(pangkat=5, nilai=10)
print("Hasil pangkat : ", r1, "Hasil perkalian : ", r2)