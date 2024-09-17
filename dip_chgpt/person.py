import datetime
import re


class Person:
    def __init__(self, first_name, last_name='', patronymic='', birth_date=None, death_date=None, gender='m'):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date)
        self.gender = gender

    def parse_date(self, date_str):
        """Парсить дату з різних форматів."""
        if not date_str:
            return None

        date_patterns = ['%d.%m.%Y', '%d/%m/%Y', '%d %m %Y', '%d-%m-%Y']
        for pattern in date_patterns:
            try:
                return datetime.datetime.strptime(date_str, pattern).date()
            except ValueError:
                continue
        raise ValueError(f"Неправильний формат дати: {date_str}")

    def calculate_age(self):
        """Обчислює вік людини на основі дати народження та дати смерті або поточної дати."""
        if not self.birth_date:
            return None

        end_date = self.death_date or datetime.date.today()
        age = end_date.year - self.birth_date.year - (
                    (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def __str__(self):
        """Форматує інформацію про людину для відображення."""
        gender_str = 'чоловік' if self.gender == 'm' else 'жінка'
        age = self.calculate_age()
        result = f"{self.first_name} {self.last_name} {self.middle_name} {age} років, {gender_str}. Народився {self.birth_date.strftime('%d.%m.%Y')}."
        if self.death_date:
            result += f" Помер: {self.death_date.strftime('%d.%m.%Y')}."
        return result

    @staticmethod
    def matches_query(person, query):
        """Перевіряє, чи співпадає інформація з пошуковим запитом."""
        query = query.lower()
        return any(
            query in (getattr(person, field) or '').lower() for field in ['first_name', 'last_name', 'middle_name'])
