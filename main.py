print("Latihan Program Basic Python")

user = {
    'name' : 'user123',
    'password' : '123',
    'money' : 24000,
}

print('Silahkan Login dahulu')

while True : 
    name = input(str("Masukan name : "))
    password = input(str("Masukan password : "))
    if name != user['name'] :
        print("Name salah")
    elif password != user['password'] :
        print("Password Salah")
    elif name == user['name'] and password == user['password']:
        print("Haloo ", user['name'])
        print("Saldo anda : Rp", user['money'])
        print("Apakah anda ingin menambahkan saldo ?")
        y = input(str("Y/N : "))
        if y == 'Y' or y == 'y' :
            print("Masukan jumlah saldo")
            saldo = input("Jumlah saldo : ")
            saldo = int(saldo)
            total = saldo + user['money']
            user['money']=total
            print("Saldo terbaru : Rp", user["money"])
            print("Terima Kasih")
        else :
            print("Terima Kasih")
        break
    else :
        print("Anda tidak terdaftar")
        break