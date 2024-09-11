from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from database import PeopleDatabase
from person import Person

db = PeopleDatabase()


async def start(update: Update, context):
    await update.message.reply_text(
        "Вітаю! Використовуйте /add для додавання нових записів, /search для пошуку або /save для збереження у файл.")


async def add(update: Update, context):
    await update.message.reply_text(
        "Введіть дані у форматі: Ім'я, Прізвище, По-батькові, дата народження, дата смерті (якщо є), стать (m/f):")

    # Приймаємо дані від користувача
    # Викликається після отримання введених даних
    # Приклад: Євген Крут Михайлович 12.10.1980 11.10.2001 m


async def handle_add_data(update: Update, context):
    text = update.message.text
    data = text.split(',')
    try:
        person = Person(data[0], data[1].strip() if len(data) > 1 else None,
                        data[2].strip() if len(data) > 2 else None, data[3].strip(),
                        data[4].strip() if len(data) > 4 else None, data[5].strip() if len(data) > 5 else None)
        db.add_person(person)
        await update.message.reply_text(f"Додано: {person}")
    except Exception as e:
        await update.message.reply_text(f"Помилка: {e}")


async def search(update: Update, context):
    query = ' '.join(context.args)
    results = db.search(query)
    if results:
        await update.message.reply_text("\n".join([str(p) for p in results]))
    else:
        await update.message.reply_text("Нічого не знайдено.")


async def save(update: Update, context):
    db.save_to_file('people.json')
    await update.message.reply_text("Дані збережено у файл 'people.json'.")


async def load(update: Update, context):
    db.load_from_file('people.json')
    await update.message.reply_text("Дані завантажено з файлу 'people.json'.")


app = ApplicationBuilder().token('7104180695:AAEzxjKUW3IKLJIRG6YW9SPGtwvJADx8pUs').build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_add_data))
app.add_handler(CommandHandler("search", search))
app.add_handler(CommandHandler("save", save))
app.add_handler(CommandHandler("load", load))

app.run_polling()
