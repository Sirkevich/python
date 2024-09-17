from flask import Flask, render_template, request, redirect
from models import PeopleManager, Person

app = Flask(__name__)
manager = PeopleManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name', '')
    patronymic = request.form.get('patronymic', '')
    birth_date = request.form.get('birth_date')
    death_date = request.form.get('death_date', None)
    gender = request.form.get('gender', '')

    person = Person(first_name, last_name, patronymic, birth_date, death_date, gender)
    manager.add_person(person)

    return redirect('/')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    results = manager.search_people(query)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
