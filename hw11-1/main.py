from inspect import isgenerator


def prime_generator(end):

    number_list = [x for x in range(2, end + 1)]
    for elem in number_list:
        i = 1
        count = 0
        while i < elem:
            if elem % i == 0:
                count += 1
            i += 1
        if count == 1:
            yield elem


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
