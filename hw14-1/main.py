class UserException(Exception):
    pass


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

    def __init__(self, number, max_students_value=10):
        self.max_students_value = max_students_value
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.max_students_value:
            raise UserException(f"Cannot add student: {student.first_name} {student.last_name}. "
                                f"Maximum students value reached ({self.max_students_value}).")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)

        if student:
            self.group.remove(student)
        else:
            return print("Student not in the group\n")

    def find_student(self, last_name):
        res = None

        for student in self.group:
            if student.last_name == last_name:
                res = student
                break
        return res

    def __str__(self):
        all_students = ''

        for student in self.group:
            all_students += str(student)

        return (f'Group_Number:{self.number}'
                f'\n{all_students}')


try:
    st1 = Student('Male', 22, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st3 = Student('Male', 24, 'Alex', 'Bingo', 'AN146')
    st4 = Student('Female', 18, 'Lina', 'Kostenko', 'AN147')
    st5 = Student('Male', 19, 'Alex', 'Yarem', 'AN148')
    st6 = Student('Female', 21, 'Inna', 'Demid', 'AN149')
    st7 = Student('Male', 19, 'Andrii', 'Yuskiv', 'AN150')
    st8 = Student('Female', 19, 'Ann', 'Sapiha', 'AN152')
    st9 = Student('Male', 23, 'Ivan', 'Kim', 'AN152')
    st10 = Student('Female', 24, 'Olena', 'Pchilka', 'AN153')
    st11 = Student('Male', 25, 'Bohdan', 'Shulha', 'AN154')

    gr = Group('PD1')

    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)

    print(gr)

except UserException as e:
    print(e)
