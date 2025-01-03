class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: ",self.name)
        print("Age: ",self.age)
        print("Grade: ",self.grades)


    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

s1 = Student("Pranav", 18, [85, 90, 88])
s1.display_details()
print("Average Grade: ", s1.calculate_average())
