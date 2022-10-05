# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: # [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


from random import random

data = []
for j in range(10):
    data.append(int(random()*10))
print(data)

s = []
for i in data:
    if data.count(i) == 1:
        s.append(i)

print(s)









exit()
from random import randint
def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unic_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10

origin = create_list(size, m, n)
print(origin)
print(get_unic_value(origin))