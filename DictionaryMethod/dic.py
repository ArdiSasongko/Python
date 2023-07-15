data = {
    'a':10,
    'b':20,
    'c':30,
    'd':40
}

data2 = {
    'a':10,
    'b':20,
    'c':30,
    'd':40
}

#mengambil spesifik value
print(data.get('a'))
b = data.get('e',50)
print(b)

#pop() menghapus secara spesific
print(data.pop('b'))

#popitem() menghapus list terakhir
print(data.popitem())

#clear menghapus dictionary
data.clear()
print(data)
print(" ")

#update dic, jika data yang diupdate tidak ada maka akan terinput ke dic
print(data2)
data2.update(a=15)
data2.update(e=50)
print(data2)

#copy dictionary, menggunakan copy
data3 = data2.copy()
print(data3)

#deepcopy untuk double dictionary
doubledictionary = {'a':{'ayam':20}, 'b':{'ayam':15,'bebek':20}}
print(doubledictionary)
import copy
doubledictionary2 = copy.deepcopy(doubledictionary)
print(doubledictionary2)
#update
doubledictionary2['b']['bebek']=25
print(doubledictionary2)