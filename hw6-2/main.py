
number_of_seconds = int(input('Enter seconds (0 - 8640000): '))

if 0 <= number_of_seconds <= 8640000:
    days = number_of_seconds // 86400
    hours = (number_of_seconds - days * 24 * 60 * 60) // 3600
    minutes = (number_of_seconds - days * 24 * 60 * 60 - hours * 60 * 60) // 60
    seconds = number_of_seconds - days * 24 * 60 * 60 - hours * 60 * 60 - minutes * 60

    if days % 10 == 1 and days != 11:
        days_word = 'день'

    elif days % 10 in [2, 3, 4] and days not in [12, 13, 14]:
        days_word = 'дні'

    else:
        days_word = 'днів'

    print(f'{days} {days_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
else:
    print('Entered value is not correct (0 - 8640000): ')
