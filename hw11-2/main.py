from inspect import isgenerator


def generate_cube_numbers(end):

    current_number = 2
    while True:
        if current_number ** 3 > end:
            return
        yield current_number ** 3

        current_number += 1

    # current_number = 2
    # while current_number ** 3 <= end:
    #     yield current_number ** 3
    #     current_number += 1


gen = generate_cube_numbers(1000)

for elem in gen:
    print(elem)

assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

print('ok')
