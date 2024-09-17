from telegram import Update, ReplyKeyboardMarkup  # Імпортуємо класи для роботи з Telegram API
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes  # Імпортуємо необхідні класи для обробки команд
from database import PeopleDatabase  # Імпортуємо клас PeopleDatabase для роботи з базою даних
from person import Person  # Імпортуємо клас Person для створення об'єктів особи

db = PeopleDatabase()  # Створюємо екземпляр бази даних


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Обробник команди /start
    await update.message.reply_text("Привіт! Я бот для роботи з даними про людей. Використовуйте команди для управління даними.")  # Відповідаємо на команду


async def add_person(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Обробник команди /add
    await update.message.reply_text("Введіть дані про людину (ім'я, прізвище, по-батькові, дата народження, дата смерті, стать):")  # Запитуємо дані


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Обробник повідомлень
    message = update.message.text  # Отримуємо текст повідомлення

    # Логіка для парсингу даних людини з повідомлення
    parts = message.split(",")  # Розбиваємо повідомлення на частини

    if len(parts) >= 5:  # Перевіряємо, чи достатньо частин
        first_name = parts[0].strip()  # Ім'я
        last_name = parts[1].strip() if len(parts) > 1 else None  # Прізвище (необов'язкове)
        middle_name = parts[2].strip() if len(parts) > 2 else None  # По-батькові (необов'язкове)
        birth_date = parts[3].strip() if len(parts) > 3 else None  # Дата народження
        death_date = parts[4].strip() if len(parts) > 4 else None  # Дата смерті
        gender = parts[5].strip() if len(parts) > 5 else None  # Стать (необов'язкове)

        person = Person(first_name, last_name, middle_name, birth_date, death_date, gender)  # Створюємо об'єкт особи
        db.add_person(person)  # Додаємо особу до бази даних
        await update.message.reply_text(f"Додано: {person}")  # Підтвердження

    else:
        await update.message.reply_text("Неправильний формат. Спробуйте ще раз.")  # Повідомлення про помилку


async def search_person(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Обробник команди /search
    await update.message.reply_text("Введіть запит для пошуку:")  # Запитуємо запит для пошуку


async def main():
    # Головна функція для запуску бота
    application = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()  # Створюємо екземпляр бота
    application.add_handler(CommandHandler("start", start))  # Додаємо обробник для команди /start
    application.add_handler(CommandHandler("add", add_person))  # Додаємо обробник для команди /add
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Додаємо обробник для текстових повідомлень
    application.add_handler(CommandHandler("search", search_person))  # Додаємо обробник для команди /search

    await application.run_polling()  # Запускаємо бота


if __name__ == "__main__":
    import asyncio  # Імпортуємо модуль asyncio
    asyncio.run(main())  # Запускаємо головну функцію