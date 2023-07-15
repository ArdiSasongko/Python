number = [1,2,3,4,5,6]
names = ["joko", "budi", "pojo", "tritin"]
index = 0

while index < len(number):
    print("nomor ke : ", number[index])
    index += 1

index = 0

while index < len(names):
    print(names[index])
    if len(names[index]) < 5:
        print("Panjang nama kurang dari 5")
    else:
        print("Panjang nama sama atau lebih dari 5")
    index += 1