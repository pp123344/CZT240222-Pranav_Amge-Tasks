def student_data_crud():
    students = {}

    def create_student(name, age, grades):
        students[name] = {"age": age, "grades": grades}

    def read_student(name):
        return students.get(name, "Student not found.")

    def update_student(name, age=None, grades=None):
        if name in students:
            if age:
                students[name]["age"] = age
            if grades:
                students[name]["grades"] = grades
        else:
            print("Student not found.")

    def delete_student(name):
        if name in students:
            del students[name]
        else:
            print("Student not found.")

    create_student("Alice", 20, [85, 90, 88])
    create_student("Bob", 22, [78, 81, 74])
    print(read_student("Alice"))
    update_student("Alice", grades=[90, 95, 92])
    print(read_student("Alice"))
    delete_student("Bob")
    print(students)

student_data_crud()
