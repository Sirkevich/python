import tkinter as tk
from tkinter import messagebox, filedialog
from person import Person
from database import Database

db = Database()

def add_person():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    middle_name = entry_middle_name.get()
    birth_date = entry_birth_date.get()
    death_date = entry_death_date.get()
    gender = gender_var.get()

    try:
        person = Person(first_name, last_name, middle_name, birth_date, death_date, gender)
        db.add_person(person)
        messagebox.showinfo("Успіх", "Запис додано.")
    except ValueError as e:
        messagebox.showerror("Помилка", str(e))

def search_person():
    query = entry_search.get()
    results = db.search(query)
    result_text.delete(1.0, tk.END)
    if results:
        for person in results:
            result_text.insert(tk.END, f"{person}\n")
    else:
        result_text.insert(tk.END, "Записів не знайдено.\n")

def save_data():
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filename:
        db.save_to_file(filename)
        messagebox.showinfo("Успіх", "Дані збережено.")

def load_data():
    filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if filename:
        db.load_from_file(filename)
        messagebox.showinfo("Успіх", "Дані завантажено.")

# Створення головного вікна
root = tk.Tk()
root.title("Робота з даними про людей")

# Поля для введення даних
tk.Label(root, text="Ім'я:").grid(row=0, column=0)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1)

tk.Label(root, text="Прізвище:").grid(row=1, column=0)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1)

tk.Label(root, text="По-батькові:").grid(row=2, column=0)
entry_middle_name = tk.Entry(root)
entry_middle_name.grid(row=2, column=1)

tk.Label(root, text="Дата народження:").grid(row=3, column=0)
entry_birth_date = tk.Entry(root)
entry_birth_date.grid(row=3, column=1)

tk.Label(root, text="Дата смерті:").grid(row=4, column=0)
entry_death_date = tk.Entry(root)
entry_death_date.grid(row=4, column=1)

tk.Label(root, text="Стать:").grid(row=5, column=0)
gender_var = tk.StringVar(value='m')
tk.Radiobutton(root, text="Чоловік", variable=gender_var, value='m').grid(row=5, column=1, sticky="w")
tk.Radiobutton(root, text="Жінка", variable=gender_var, value='f').grid(row=5, column=1, sticky="e")

# Кнопка додати людину
tk.Button(root, text="Додати людину", command=add_person).grid(row=6, column=0, columnspan=2)

# Поле для пошуку
tk.Label(root, text="Пошук:").grid(row=7, column=0)
entry_search = tk.Entry(root)
entry_search.grid(row=7, column=1)

# Кнопка пошуку
tk.Button(root, text="Шукати", command=search_person).grid(row=8, column=0, columnspan=2)

# Поле для відображення результатів
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=9, column=0, columnspan=2)

# Кнопки для збереження і завантаження даних
tk.Button(root, text="Зберегти у файл", command=save_data).grid(row=10, column=0)
tk.Button(root, text="Завантажити з файлу", command=load_data).grid(row=10, column=1)

# Запуск головного циклу
root.mainloop()
