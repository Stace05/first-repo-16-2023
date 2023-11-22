drink = "coffee"
print(drink)
print()

is_holiday = True
is_workday = False
print(is_holiday and is_workday)
print(is_holiday or is_workday)
print ((is_holiday) ^ (is_workday))
print()

is_sunny = True
is_cloudy = True
print(is_sunny or is_cloudy)
print()

import math
x = 2.34
y = 1.45
def math_task(x, y):
    return pow(math.e, -y) + pow(math.sin(x),2) / math.cos(pow(y, 2)) - 12.1 * math.log(x+y)

print(math_task(x, y))

