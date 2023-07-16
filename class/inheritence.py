# Buat parent class
class Person:
    def __init__(self, name, age, height, weight):
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight
    
    def activity(self, move):
        self._move = move
        print(self._name, "sedang melakukan", self._move)

# Buat subclass students yang mewarisi dari class Person
class Student(Person):
    def __init__(self, name, age, height, weight, nim, classes):
        super().__init__(name, age, height, weight)
        self._nim = nim
        self._classes = classes
    
    def student(self):
        print("NIM siswa tersebut", self._nim, "dari kelas", self._classes)

# Contoh penggunaan class Person dan Student
joko = Person("Joko", 16, 168, 55)
joko.activity("lari")

budi = Student("Budi", 18, 170, 60, "123456", "XII-A")
budi.activity("berenang")
budi.student()
