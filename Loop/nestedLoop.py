#break dan continue

word = "indonesia"

for i in word :
    if i in ['a','e','i','u','o'] :
        break
    print(i)

#tidak menghasilkan kata/huruf karena huruf awal berada pada huruf vokal
print("end")

for i in word :
    if i in ['a','e','i','u','o'] :
        continue
    print(i)

print("end")


for i in range(1, 6):
    for j in range(1, 6):
        hasil = i * j
        print(i, "*", j, "=", hasil)

