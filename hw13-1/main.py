class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return (f"Student:"
                f" {self.first_name} {self.last_name}\n"
                f"Gender: {self.gender}\n"
                f"Age: {self.age}\n"
                f"Record book: {self.record_book}")


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        pass

    def find_student(self, last_name):
        pass

    def __str__(self):
        all_students = ''
        ...
        return f'Number:{self.number}\\n {all_students} '


worker = Human('male', 31, 'Ihor', 'Sirko')

st1 = Student('male', 20, 'Stepan', 'Bandera', 'A')

gr = Group('PD1')

gr.add_student(st1)

print(gr.group)

print(worker)
print('-' * 100)

print(st1)
print('-' * 100)


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

print(gr)
