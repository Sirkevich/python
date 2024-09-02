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
                f"{self.first_name} {self.last_name}\n"
                f"Gender: {self.gender}\n"
                f"Age: {self.age}\n"
                f"Record book: {self.record_book}\n\n")


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        res = self.find_student(last_name)
        if res in self.group:
            self.group.remove(res)
        else:
            return print("Student not in the group")

    def find_student(self, last_name):

        for elem in list(self.group):
            if last_name in str(elem):
                return print(elem)
            else:
                return None

    def __str__(self):
        all_students = ''
        for elem in self.group:
            all_students += str(elem)

        return (f'Number:{self.number}'
                f'\n{all_students}')


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 21, 'Tim', 'Kuk', 'AN146')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)

print(gr)

gr.find_student('Jobs')

# gr.delete_student('Taylor')
#
# print(gr)

# print(str(gr.find_student('Jobs2')) == str(st1))
# print(isinstance(gr.find_student('Jobs'), Student))
