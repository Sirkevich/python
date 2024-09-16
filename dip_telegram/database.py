import json
from person import Person
from datetime import datetime


class PeopleDatabase:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def search(self, query):
        # Розбиваємо пошуковий запит на окремі слова
        search_terms = query.lower().split()

        # Створюємо список для збереження результатів
        results = []

        # Проходимо по кожній людині в базі даних
        for person in self.people:
            # Об'єднуємо всі релевантні поля в одну строку для пошуку
            person_data = f"{person.first_name or ''} {person.middle_name or ''} {person.last_name or ''}".lower()

            # Перевіряємо, чи всі пошукові слова є в інформації про людину
            if all(term in person_data for term in search_terms):
                results.append(person)

        print(f"Пошуковий запит: {query}, Знайдено записів: {len(results)}")  # Для відлагодження
        return results

    def save_to_file(self, filename):
        data = [{"first_name": p.first_name, "last_name": p.last_name, "middle_name": p.middle_name,
                 "birth_date": p.birth_date.strftime("%d.%m.%Y"),
                 "death_date": p.death_date.strftime("%d.%m.%Y") if p.death_date else None, "gender": p.gender}
                for p in self.people]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for entry in data:
                person = Person(entry['first_name'], entry['last_name'], entry['middle_name'],
                                entry['birth_date'], entry['death_date'], entry['gender'])
                self.add_person(person)
