import json
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name='', patronymic='', birth_date=None, death_date=None, gender=''):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date)
        self.gender = gender

    @staticmethod
    def parse_date(date_str):
        if date_str:
            for fmt in ("%d.%m.%Y", "%d %m %Y", "%m/%d/%Y", "%d-%m-%Y"):
                try:
                    return datetime.strptime(date_str, fmt)
                except ValueError:
                    continue
        return None

    def age(self):
        today = datetime.now()
        if self.death_date:
            return (self.death_date - self.birth_date).days // 365
        return (today - self.birth_date).days // 365

    def __str__(self):
        death_info = f" Помер: {self.death_date.strftime('%d.%m.%Y')}" if self.death_date else ''
        return f"{self.first_name} {self.last_name} {self.patronymic} {self.age()} років, {self.gender}. Народився: {self.birth_date.strftime('%d.%m.%Y')}.{death_info}"

class PeopleManager:
    def __init__(self, data_file='data.json'):
        self.data_file = data_file
        self.people = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                return [Person(**person) for person in json.load(f)]
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump([person.__dict__ for person in self.people], f)

    def add_person(self, person):
        self.people.append(person)
        self.save_data()

    def search_people(self, query):
        return [person for person in self.people if query.lower() in (person.first_name + ' ' + person.last_name + ' ' + person.patronymic).lower()]
