# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N
# Пример: 
# пусть N = 4, тогда [1, 2, 6, 24]

import math

def fact(n: int) -> list:
    lst = [i for i in range(1, n+1)]
    fact = list(map(lambda x: math.factorial(x), lst))
    return fact

print(fact(4))