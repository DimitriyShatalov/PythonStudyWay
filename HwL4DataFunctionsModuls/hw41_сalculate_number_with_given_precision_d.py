# 1. Вычислить число c заданной точностью d

# Пример:
# при d = 0.001, π = 3.141.$    10^{-1} ≤ d ≤10^{-10}



from math import pi

d = input('What is the number of elements in the pi after the dot to leave? ')
pi=22/7

print('{:.{}f}'.format(pi, d))

# d =  int(input("Enter a number for the specified precision of Pi: "))
# print(f'Specified precision {d}. Pi = {round(pi, d)}')

