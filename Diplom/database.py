        import json  # Імпортуємо модуль json для роботи з файлами формату JSON
        from person import Person  # Імпортуємо клас Person для роботи з особами
        from datetime import datetime  # Імпортуємо клас datetime для роботи з датами


        class PeopleDatabase:
            def __init__(self):
                self.people = []  # Ініціалізуємо порожній список для зберігання осіб

            def add_person(self, person):
                # Метод для додавання особи до бази даних
                self.people.append(person)  # Додаємо об'єкт особи до списку

            def search(self, query):
                # Метод для пошуку осіб за запитом
                search_terms = query.lower().split()  # Розбиваємо пошуковий запит на окремі слова

                results = []  # Створюємо список для збереження результатів пошуку

                for person in self.people:  # Проходимо по кожній людині в базі даних
                    # Об'єднуємо всі релевантні поля в одну строку для пошуку
                    person_data = f"{person.first_name or ''} {person.middle_name or ''} {person.last_name or ''}".lower()

                    # Перевіряємо, чи всі пошукові слова є в інформації про людину
                    if all(term in person_data for term in search_terms):  # Якщо всі терміни знайдені
                        results.append(person)  # Додаємо людину до результатів

                print(f"Пошуковий запит: {query}, Знайдено записів: {len(results)}")  # Виводимо результати для відлагодження
                return results  # Повертаємо результати пошуку

            def save_to_file(self, filename):
                # Метод для збереження даних у файл
                data = [{"first_name": p.first_name, "last_name": p.last_name, "middle_name": p.middle_name,
                         "birth_date": p.birth_date.strftime("%d.%m.%Y"),
                         "death_date": p.death_date.strftime("%d.%m.%Y") if p.death_date else None, "gender": p.gender}
                        for p in self.people]  # Створюємо список словників для збереження
                with open(filename, 'w', encoding='utf-8') as f:  # Відкриваємо файл для запису
                    json.dump(data, f, ensure_ascii=False)  # Записуємо дані у файл у форматі JSON

            def load_from_file(self, filename):
                # Метод для завантаження даних з файлу
                with open(filename, 'r', encoding='utf-8') as f:  # Відкриваємо файл для читання
                    data = json.load(f)  # Завантажуємо дані з файлу
                    for entry in data:  # Проходимо по кожному запису
                        person = Person(entry['first_name'], entry['last_name'], entry['middle_name'],
                                        entry['birth_date'], entry['death_date'], entry['gender'])  # Створюємо об'єкт особи
                        self.add_person(person)  # Додаємо особу до бази даних
