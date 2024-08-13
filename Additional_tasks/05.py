# Написати програму, яка просить ввести 4 числа – кількість днів, годин,
# хвилин і секунд. Програма виводить цей час у секундах.

count_of_days = int(input('Enter days:'))
count_of_hours = int(input('Enter hours:'))
count_of_minutes = int(input('Enter minutes:'))
count_of_seconds = int(input('Enter seconds:'))

print(count_of_days * 24 * 60 * 60 + count_of_hours * 60 * 60 + count_of_minutes * 60 + count_of_seconds, 'seconds')
