from datetime import datetime


class Person:
    def __init__(self, first_name, last_name=None, middle_name=None, birth_date=None, death_date=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date) if death_date else None
        self.gender = gender

    def parse_date(self, date_str):
        date_formats = ["%d.%m.%Y", "%d %m %Y", "%d/%m/%Y", "%d-%m-%Y"]
        for fmt in date_formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                pass
        raise ValueError("Incorrect date format")

    def calculate_age(self):
        end_date = self.death_date if self.death_date else datetime.now()
        age = end_date.year - self.birth_date.year - ((end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def __str__(self):
        gender_str = "чоловік" if self.gender == "m" else "жінка" if self.gender == "f" else "невідомо"
        age = self.calculate_age()
        death_info = f"Помер: {self.death_date.strftime('%d.%m.%Y')}" if self.death_date else "Живий"
        return f"{self.first_name} {self.last_name or ''} {self.middle_name or ''} {age} років, {gender_str}. Народився: {self.birth_date.strftime('%d.%m.%Y')}. {death_info}."
