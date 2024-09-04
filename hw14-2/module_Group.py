
class UserException(Exception):
    pass


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
