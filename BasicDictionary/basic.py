person1 = {
    "Name" : "Budi",
    "Age" : 20,
    "Address" : "Bandung"
}

print(person1)
#menambahkan key-value ke dictionary
person1["Height"] = 180
print(person1)
#mengubah value dari dictionary
person1["Age"] = 22
print(person1)
#menghapus key-value dari dictionary
del person1["Height"]
print(person1)

#function and operator

print(len(person1))
print("Name" in person1)