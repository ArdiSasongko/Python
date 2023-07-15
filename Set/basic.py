data = [5,6,7,8,9,10]
data2 = (3,5,7,9,11,13)

#membuat set menggunakan {}
dataset3 = {1,2,3,4,5,6,7}

#membuat set dari list dan tuple
dataset = set(data)
dataset2 = set(data2)

for i in dataset3:
    print(i)

#menambahkan dan menghapus set
dataset3.add(10)
print(dataset3)
dataset3.remove(4)
print('Dataset : ', dataset)
print('Dataset 2 : ', dataset2)
print('Dataset 3 : ', dataset3)

#union '|' dan intersection '&'
print('union : ', dataset | dataset2)
print('intersection : ', dataset2 & dataset3)

#diference set '-' dan simetric set '^'
print('difference : ', dataset - dataset2)
print('Simetric : ', dataset2 ^ dataset3)