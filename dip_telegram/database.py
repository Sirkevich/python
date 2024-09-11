import json
from person import Person

class PeopleDatabase:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def search(self, query):
        return [p for p in self.people if query.lower() in (p.first_name + (p.last_name or '') + (p.middle_name or '')).lower()]

    def save_to_file(self, filename):
        data = [{"first_name": p.first_name, "last_name": p.last_name, "middle_name": p.middle_name,
                 "birth_date": p.birth_date.strftime("%d.%m.%Y"),
                 "death_date": p.death_date.strftime("%d.%m.%Y") if p.death_date else None, "gender": p.gender}
                for p in self.people]
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for entry in data:
                person = Person(entry['first_name'], entry['last_name'], entry['middle_name'],
                                entry['birth_date'], entry['death_date'], entry['gender'])
                self.add_person(person)
