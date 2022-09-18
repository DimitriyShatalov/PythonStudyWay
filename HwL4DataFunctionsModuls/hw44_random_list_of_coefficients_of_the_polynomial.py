# 4.Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
import itertools

k = randint(3, 5)

def my_ratios(k):
    ratios = [randint(0, 100) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 100) 
    return ratios

def my_poly(k, ratios):
    vario = ['*x**']*(k-1) + ['*x']
    poly = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, vario, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in poly:
        x.append(' + ')
    poly = list(itertools.chain(*poly))
    poly[-1] = ' = 0'
    return "".join(map(str, poly)).replace(' 1*x',' x')

ratios = my_ratios(k)
polynom1 = my_poly(k, ratios)
print(polynom1)

with open('Polynom44_1.txt', 'w') as data:
    data.write(polynom1)
