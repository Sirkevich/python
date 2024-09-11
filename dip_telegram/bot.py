from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from database import PeopleDatabase
from person import Person

db = PeopleDatabase()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ['Додати запис', 'Пошук записів'],
        ['Зберегти дані', 'Завантажити дані'],
        ['/restart']  # Додати можливість перезавантаження
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

    await update.message.reply_text("Вітаю! Виберіть дію:", reply_markup=reply_markup)

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    if user_message == 'Додати запис':
        await add(update, context)
    elif user_message == 'Пошук записів':
        await search(update, context)
    elif user_message == 'Зберегти дані':
        await save(update, context)
    elif user_message == 'Завантажити дані':
        await load(update, context)
    else:
        await handle_add_data(update, context)  # Додано для обробки введених даних

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Введіть дані у форматі: Ім'я, Прізвище, По-батькові, дата народження, дата смерті (якщо є), стать (m/f):")
    context.user_data['adding'] = True  # Встановлюємо стан додавання

async def handle_add_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('adding'):
        text = update.message.text
        data = text.split(',')

        try:
            person = Person(
                data[0].strip(),
                data[1].strip() if len(data) > 1 else None,
                data[2].strip() if len(data) > 2 else None,
                data[3].strip(),
                data[4].strip() if len(data) > 4 else None,
                data[5].strip() if len(data) > 5 else None
            )
            db.add_person(person)
            await update.message.reply_text(f"Додано: {person}")

            # Скинути стан після додавання
            context.user_data['adding'] = False
        except Exception as e:
            await update.message.reply_text(f"Помилка: {e}")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введіть запит для пошуку:")

async def handle_search_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    results = db.search(query)

    if results:
        await update.message.reply_text("\n".join([str(p) for p in results]))
    else:
        await update.message.reply_text("Нічого не знайдено.")

async def save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db.save_to_file('people.json')
    await update.message.reply_text("Дані збережено у файл 'people.json'.")

async def load(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db.load_from_file('people.json')
    await update.message.reply_text("Дані завантажено з файлу 'people.json'.")

async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()  # Очищаємо дані користувача
    await update.message.reply_text("Бот перезавантажено. Виберіть дію:", reply_markup=start_keyboard())

def start_keyboard():
    keyboard = [
        ['Додати запис', 'Пошук записів'],
        ['Зберегти дані', 'Завантажити дані'],
        ['/restart']
    ]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

app = ApplicationBuilder().token('7104180695:AAEzxjKUW3IKLJIRG6YW9SPGtwvJADx8pUs').build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("restart", restart))  # Додати обробник для перезавантаження
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))  # Оновлено тут
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_add_data))

app.run_polling()
