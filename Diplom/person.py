from datetime import datetime  # Імпортуємо клас datetime для роботи з датами


class Person:
    def __init__(self, first_name, last_name=None, middle_name=None, birth_date=None, death_date=None, gender=None):
        # Конструктор класу Person для ініціалізації атрибутів
        self.first_name = first_name  # Ім'я
        self.last_name = last_name  # Прізвище (необов'язкове)
        self.middle_name = middle_name  # По-батькові (необов'язкове)
        self.birth_date = self.parse_date(birth_date)  # Дата народження, оброблена через метод parse_date
        self.death_date = self.parse_date(death_date) if death_date else None  # Дата смерті, якщо вказана
        self.gender = gender  # Стать (необов'язкова)

    def parse_date(self, date_str):
        # Метод для парсингу дати з рядка
        if date_str and date_str != "-":  # Перевіряємо, що рядок не порожній і не "-"
            for fmt in ("%d.%m.%Y", "%d %m %Y", "%m/%d/%Y", "%m-%d-%Y"):  # Список форматів для парсингу
                try:
                    return datetime.strptime(date_str, fmt).date()  # Повертаємо об'єкт дати
                except ValueError:
                    continue  # Продовжуємо, якщо формат не підходить
        return None  # Повертаємо None, якщо парсинг не вдався

    def calculate_age(self):
        # Метод для обчислення віку
        if not self.birth_date:  # Якщо дата народження не вказана
            raise ValueError("Дата народження не вказана")  # Викидаємо виключення

        # Використовуємо поточну дату, якщо дата смерті не вказана
        end_date = self.death_date if self.death_date else datetime.now().date()  # Визначаємо дату закінчення

        # Обчислюємо вік
        age = end_date.year - self.birth_date.year - (
                (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day))  # Ураховуємо, чи був день народження в поточному році
        return age  # Повертаємо вік

    def __str__(self):
        # Метод для строкового представлення об'єкта
        # Визначаємо строкове представлення статі
        gender_str = "чоловік" if self.gender == "m" else "жінка" if self.gender == "f" else "невідомо"

        # Формуємо частини ПІБ, додаючи лише за наявності
        full_name = self.first_name  # Починаємо з імені
        if self.middle_name:  # Якщо по-батькові вказано
            full_name += f" {self.middle_name}"  # Додаємо по-батькові
        if self.last_name:  # Якщо прізвище вказано
            full_name += f" {self.last_name}"  # Додаємо прізвище

        # Функція для підбору правильного закінчення для слова "рік"
        def get_year_ending(age):
            if 11 <= age % 100 <= 14:  # Вік від 11 до 14 років
                return "років"  # Завжди "років"
            elif age % 10 == 1:  # Якщо остання цифра 1
                return "рік"  # "рік"
            elif 2 <= age % 10 <= 4:  # Якщо остання цифра 2, 3 або 4
                return "роки"  # "роки"
            else:
                return "років"  # В усіх інших випадках "років"

        # Форматування: ПІБ, вік, стать, дата народження
        if self.birth_date:  # Якщо дата народження вказана
            age = self.calculate_age()  # Обчислюємо вік
            age_str = f"{age} {get_year_ending(age)}"  # Формуємо строку з віком
            output = f"{full_name}, {age_str}, {gender_str}. Народився: {self.birth_date.strftime('%d.%m.%Y')}."  # Форматуємо вихідне повідомлення
        else:
            output = f"{full_name} народився: дата невідома."  # Якщо дата народження не вказана

        # Додаємо інформацію про дату смерті, якщо вона є
        if self.death_date:  # Якщо дата смерті вказана
            output += f" Помер: {self.death_date.strftime('%d.%m.%Y')}."  # Додаємо дату смерті до виходу

        return output.strip()  # Повертаємо відформатований рядок

