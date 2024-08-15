# Напишіть програму, яка запитує користувача три числа і виводить їх у порядку
# зростання, розділені комою. Використовуйте умовні оператори та вкладені
# умови для вирішення завдання. Передбачається, що це три числа різні.

# Приклад:
# Введіть перше число: 5
# Введіть друге число: 2
# Введіть третє число: 7

# Числа в порядку зростання: 2, 5, 7

first_number = int(input('Введіть перше число: '))
second_number = int(input('Введіть друге число: '))
third_number = int(input('Введіть третє число: '))

if first_number < second_number and first_number < third_number:
    if second_number < third_number:
        print(f'{first_number}, {second_number}, {third_number}')
    else:
        print(f'{first_number}, {third_number}, {second_number}')

elif first_number > second_number and first_number > third_number:
    if second_number < third_number:
        print(f'{second_number}, {third_number}, {first_number}')
    else:
        print(f'{third_number}, {second_number}, {first_number}')

elif second_number > first_number and second_number > third_number:
    if first_number < third_number:
        print(f'{first_number}, {third_number}, {second_number}')
    else:
        print(f'{third_number}, {first_number}, {second_number}')

elif third_number > first_number and third_number > second_number:
    if first_number < second_number:
        print(f'{first_number}, {second_number}, {third_number}')
    else:
        print(f'{second_number}, {first_number}, {third_number}')



