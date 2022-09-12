# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Решение 1 - встроенная функция в Python
# n = int(input())
# print(bin(n))

# Решение 2
from msvcrt import kbhit


n = int(input('Please input integer: ')) 
k = ''
while n > 0:
    k = str(n % 2) + k
    n = n // 2
    print(n%2)
    print(str(n % 2) + k)
print(f'Binary number: {k}')



