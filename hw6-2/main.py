
number_of_seconds = int(input('Enter seconds (0 - 8640000): '))

if 0 <= number_of_seconds <= 8640000:
    days = number_of_seconds // 86400
    hours = (number_of_seconds - days * 24 * 60 * 60) // 3600
    minutes = (number_of_seconds - days * 24 * 60 * 60 - hours * 60 * 60) // 60
    seconds = number_of_seconds - days * 24 * 60 * 60 - hours * 60 * 60 - minutes * 60

    if days == 1 or str(days)[-1] == '1' and days != 11:
        print(f'{days} день, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')

    elif str(days)[0] in '234' or str(days)[0] in '234':
        print(f'{days} дні, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')

    else:
        print(f'{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
else:
    print('Enter correct value (0 - 8640000): ')
