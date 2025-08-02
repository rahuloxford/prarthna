# inheritance

class Species:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

    def details(self):
        print(f"Age: {self.age}, Height: {self.height}, Weight: {self.weight}")

    def sound(self):
        print("Species is making sound")

class Person(Species):
    def __init__(self, age, height, weight, qualification):
        super().__init__(age, height, weight)
        self.qualification = qualification
    
    def person_details(self):
        self.details()
        print(f"Qualification: {self.qualification}")
    
    def sound(self):
        print("Person is making sound")

class Cat(Species):
    pass

p1 = Person(19, 5.9, 84.25, "MCA")
p1.person_details()
p1.sound()

cat = Cat(5, 1, 5)

cat.sound()