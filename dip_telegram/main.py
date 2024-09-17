from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from database import PeopleDatabase
from person import Person

db = PeopleDatabase()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ['Додати запис', 'Пошук записів'],
        ['Зберегти дані', 'Завантажити дані'],
        ['/restart']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("Вітаю! Виберіть дію:", reply_markup=reply_markup)


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    if context.user_data.get('searching'):  # Перевіряємо, чи бот у стані пошуку
        await handle_search_data(update, context)
    elif user_message == 'Додати запис':
        await add(update, context)
    elif user_message == 'Пошук записів':
        await search(update, context)
    elif user_message == 'Зберегти дані':
        await save(update, context)
    elif user_message == 'Завантажити дані':
        await load(update, context)
    else:
        await handle_add_data(update, context)


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введіть ім'я:")
    context.user_data['adding_step'] = 'first_name'


async def handle_add_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # Якщо текст порожній, перевіряємо на запит підтвердження
    if text == "":
        if context.user_data.get('adding_step') in ['last_name', 'middle_name']:
            await update.message.reply_text("Ви впевнені, що хочете пропустити це поле? (так/ні)")
            context.user_data['adding_step'] = 'confirm_skip'
            return
        else:
            text = None

    # Додаємо перевірку для заміни '-' на None
    if text == "-":
        text = None

    if context.user_data.get('adding_step') == 'first_name':
        context.user_data['first_name'] = text
        await update.message.reply_text("Введіть прізвище (можна пропустити, ввівши '-'):")  # Оновлено повідомлення
        context.user_data['adding_step'] = 'last_name'

    elif context.user_data.get('adding_step') == 'last_name':
        context.user_data['last_name'] = text
        await update.message.reply_text("Введіть по-батькові (можна пропустити, ввівши '-'):")  # Оновлено повідомлення
        context.user_data['adding_step'] = 'middle_name'

    elif context.user_data.get('adding_step') == 'middle_name':
        context.user_data['middle_name'] = text
        await update.message.reply_text("Введіть дату народження:")
        context.user_data['adding_step'] = 'birth_date'

    elif context.user_data.get('adding_step') == 'birth_date':
        context.user_data['birth_date'] = text
        await update.message.reply_text("Введіть дату смерті (можна пропустити, ввівши '-'):")  # Оновлено повідомлення
        context.user_data['adding_step'] = 'death_date'

    elif context.user_data.get('adding_step') == 'death_date':
        context.user_data['death_date'] = text
        await update.message.reply_text("Введіть стать (m/f):")
        context.user_data['adding_step'] = 'gender'

    elif context.user_data.get('adding_step') == 'gender':
        context.user_data['gender'] = text

        # Після збору всіх даних створюємо об'єкт Person
        try:
            person = Person(
                context.user_data['first_name'],
                context.user_data['last_name'],
                context.user_data['middle_name'],
                context.user_data['birth_date'],
                context.user_data['death_date'],
                context.user_data['gender']
            )
            db.add_person(person)

            # Формуємо правильне повідомлення
            birth_word = "народилася" if person.gender == 'f' else "народився"
            death_word = "померла" if person.gender == 'f' else "помер"
            birth_date = person.birth_date.strftime("%d.%m.%Y")
            death_date = person.death_date.strftime("%d.%m.%Y") if person.death_date else ""

            age = person.calculate_age()
            gender_str = "жінка" if person.gender == 'f' else "чоловік"

            # Формуємо правильне закінчення слова "рік"
            if age % 10 == 1 and age % 100 != 11:
                age_str = f"{age} рік"
            elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
                age_str = f"{age} роки"
            else:
                age_str = f"{age} років"

            # Формуємо повне ім'я
            full_name = person.first_name
            if person.middle_name:
                full_name += f" {person.middle_name}"
            if person.last_name:
                full_name += f" {person.last_name}"

            # Формуємо фінальне повідомлення
            response = f"Додано: {full_name}, {age_str}, {gender_str}. {birth_word.capitalize()}: {birth_date}."
            if person.death_date:
                response += f" {death_word.capitalize()}: {death_date}."

            await update.message.reply_text(response)
            context.user_data['adding_step'] = None  # Скидаємо крок додавання
        except Exception as e:
            await update.message.reply_text(f"Помилка: {e}")

    elif context.user_data.get('adding_step') == 'confirm_skip':
        if text.lower() == "так":
            # Пропускаємо поле
            context.user_data['adding_step'] = 'middle_name' if context.user_data.get('last_name') is None else 'birth_date'
            await update.message.reply_text("Введіть дату народження:")
        elif text.lower() == "ні":
            # Запитуємо знову
            await update.message.reply_text("Будь ласка, введіть значення або залиште порожнім:")
        else:
            await update.message.reply_text("Невірний ввід. Введіть 'так' або 'ні'.")



async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введіть запит для пошуку:")
    context.user_data['searching'] = True  # Встановлюємо стан пошуку


async def handle_search_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    results = db.search(query)

    if results:
        response_messages = []
        for person in results:
            age = person.calculate_age()  # Викликаємо метод на об'єкті person
            gender = "чоловік" if person.gender == 'm' else "жінка"
            birth_date = person.birth_date.strftime("%d.%m.%Y")

            # Отримуємо правильне слово для віку через метод get_year_word
            def get_year_word(age):
                if 11 <= age % 100 <= 19:  # Вік від 11 до 19 років
                    return "років"
                last_digit = age % 10
                if last_digit == 1:
                    return "рік"
                elif 2 <= last_digit <= 4:
                    return "роки"
                else:
                    return "років"

            year_word = get_year_word(age)

            # Формуємо повне ім'я
            full_name = person.first_name
            if person.middle_name:
                full_name += f" {person.middle_name}"
            if person.last_name:
                full_name += f" {person.last_name}"

            # Перевіряємо, чи є дата смерті
            death_info = ""
            if person.death_date:
                death_word = "померла" if person.gender == 'f' else "помер"
                death_info = f". {death_word.capitalize()}: {person.death_date.strftime('%d.%m.%Y')}."
            else:
                death_info = "."

            birth_word = "народилася" if person.gender == 'f' else "народився"

            response_messages.append(
                f"{full_name} {age} {year_word}, {gender}. {birth_word.capitalize()}: {birth_date}{death_info}"
            )

        await update.message.reply_text("\n".join(response_messages))
    else:
        await update.message.reply_text("Нічого не знайдено.")

    context.user_data['searching'] = False


async def save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db.save_to_file('people.json')
    await update.message.reply_text("Дані збережено у файл 'people.json'.")

async def load(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db.load_from_file('people.json')
    await update.message.reply_text("Дані завантажено з файлу 'people.json'.")

async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
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
app.add_handler(CommandHandler("restart", restart))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_search_data))

app.run_polling()
