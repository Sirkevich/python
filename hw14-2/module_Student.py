from module_Human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return (f"Student:"
                f"{self.first_name} {self.last_name}\n"
                f"Gender: {self.gender}\n"
                f"Age: {self.age}\n"
                f"Record book: {self.record_book}\n")
