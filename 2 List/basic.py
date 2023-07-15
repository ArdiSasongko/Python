list = [[1,2,3],
        [3,2,4],
        [9,7,2]]

print(list)
#akses list
print(list[0])
print(list[0][2])

#update value list
list[1][1] = 15
print(list[1])

for i in list:
    for j in i:
        print(j, end= ' ')
    print(" ")

list_array = [[1,2,3],[4,5,6],[7,8,9]]
for item in list_array:
  if item == [1,2,3]:
    print("Hello!")
    continue
  print('item =',item)