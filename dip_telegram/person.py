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
        if date_str and date_str != "-":
            for fmt in ("%d.%m.%Y", "%d %m %Y", "%m/%d/%Y", "%m-%d-%Y"):
                try:
                    return datetime.strptime(date_str, fmt).date()
                except ValueError:
                    continue
        return None

    def calculate_age(self):
        if not self.birth_date:
            raise ValueError("Дата народження не вказана")

        # Використовуємо поточну дату, якщо дата смерті не вказана
        end_date = self.death_date if self.death_date else datetime.now().date()

        age = end_date.year - self.birth_date.year - (
                (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def __str__(self):
        gender_str = "чоловік" if self.gender == "m" else "жінка" if self.gender == "f" else "невідомо"

        # Формуємо частини ПІБ, додаючи лише за наявності
        full_name = self.first_name
        if self.middle_name:
            full_name += f" {self.middle_name}"
        if self.last_name:
            full_name += f" {self.last_name}"

        # Форматування: ПІБ, вік, стать, дата народження
        if self.birth_date:
            age = self.calculate_age()
            output = f"{full_name}, {age} років, {gender_str}. Народився: {self.birth_date.strftime('%d.%m.%Y')}."
        else:
            output = f"{full_name} народився: дата невідома."

        # Додаємо інформацію про дату смерті, якщо вона є
        if self.death_date:
            output += f" Помер: {self.death_date.strftime('%d.%m.%Y')}."
        else:
            output += " Живий."

        return output.strip()
