import json
from person import Person


class Database:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def search(self, query):
        return [person for person in self.people if Person.matches_query(person, query)]

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([person.__dict__ for person in self.people], file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.people = [Person(**item) for item in data]
