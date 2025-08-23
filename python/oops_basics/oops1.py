class Human:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def person_details(self):
        print(f"{self.name} is {self.age} year old")
        print(f"And he/she is {self.height} tall and weights {self.weight}")
        print("------------------------------")

human1 = Human("Tim", 26, 5.9, 76.5)
human2 = Human("John", 18, 5.11, 86.25)

human1.person_details()
human2.person_details()