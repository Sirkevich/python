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
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (f"Student:"
                f"{self.first_name} {self.last_name}\n"
                f"Gender: {self.gender}\n"
                f"Age: {self.age}\n"
                f"Record book: {self.record_book}\n")


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        current_student = self.find_student(last_name)

        if current_student in self.group:
            self.group.remove(current_student)
        else:
            return print("Student not in the group\n")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''

        for student in self.group:
            all_students += str(student)

        return (f'Group_Number:{self.number}'
                f'\n{all_students}')


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

print(str(gr.find_student('Jobs')) == str(st1))
print(gr.find_student('Jobs2'))
print(isinstance(gr.find_student('Jobs'), Student))

gr.delete_student('Taylor')

print(gr)

gr.delete_student('Taylor')

print(gr.find_student('Jobs'))
