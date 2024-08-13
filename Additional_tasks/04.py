import string
from collections import namedtuple

# Географ хоче знаходити відстань між двома точками на карті. Напишіть для
# нього програму, яка запитує у користувача координати двох точок у
# двовимірному просторі (x1, y1) та (x2, y2), а потім обчислює та виводить
# відстань між цими точками за формулою:
# distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

# де sqrt – функція вилучення квадратного кореня. Не використовуйте вбудовану
# математичну функцію sqrt для обчислення кореня. Не забувайте, що
# sqrt(x)==x**0.5. Результат слід вивести за допомогою команди print.

# Приклад:
# Введіть координати першої точки (x1, y1): 2, 3
# Введіть координати другої точки (x2, y2): 5, 7

# Відстань між точками: 5.0

first_point_coordinate = input('Введіть координати першої точки (x1, y1):')
second_point_coordinate = input('Введіть координати другої точки (x2, y2):')


Point = namedtuple('Point', 'x y')


first_point_coordinate = first_point_coordinate.split(',')
second_point_coordinate = second_point_coordinate.split(',')

p1 = Point(int(first_point_coordinate[0]), int(second_point_coordinate[0]))
p2 = Point(int(first_point_coordinate[-1]), int(second_point_coordinate[-1]))


def sqrt(value):
    value ** 0.5

    return value


distance_between_points = sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

print(float(distance_between_points))
