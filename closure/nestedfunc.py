def name(n):
    def pendek(p):
        return (p, "terdiri dari", len(p), "Kata")
    def panjang(q):
        return (q, "terdiri dari", len(q), "kata")
    if len(n) >= 5:
        return print(pendek(n))
    else :
        return print(panjang(n))

name('Budi')

def halo():
    print("Halo")

def helo():
    return halo()

helo()