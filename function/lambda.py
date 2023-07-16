add = lambda x,y : x+y

print(add(20,10))

list = [19,20,21,22,23]

#mengguanakan fungsi filter pada lambda
print("Umur diatas 19 ")
for i in filter(lambda x : x > 19, list):
    print(i, end=' Tahun ')

#menggunakan fungsi map pada lambda
for i in map(lambda x : x**2, list):
    print(i)
