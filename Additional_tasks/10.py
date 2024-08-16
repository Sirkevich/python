# Напишіть програму, яка запитує у користувача ціле позитивне число і перевіряє,
# чи є воно простим. Просте число - це число, яке ділиться тільки на 1 і на само
# себе без залишку. Використовуйте цикл і перевірку поділу числа на всі числа
# від 2 до N-1 для вирішення задачі.
# Виведіть відповідне повідомлення на екран за допомогою print.
#
# Приклад:
# Введіть позитивне число: 17
# Число 17 є простим.

user_number = int(input('Введіть позитивне число: '))

i = 2
count = 0

while i <= user_number:
    if user_number % i == 0:
        count += 1
    i += 1

if count == 1:
    print(f'Число {user_number} є простим.')
else:
    print(f'Число {user_number} не є простим.')
