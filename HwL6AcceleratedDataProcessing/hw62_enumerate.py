# 62 Заменить в списке все двузначные элементы, например, на ноль или другой символ, используюя функцию enumerate

digs = [4, -45, 3, 100, 53, 30, 1, -8]

for i, d in enumerate(digs):
    if 10 <= abs(d) <= 99:
        digs[i] = 'a'

print(digs)

exit()
#  Без функции enumerate данный код мог бы выглядеть так:
digs = [4, -45, 3, 100, 53, 30, 1, -8]

for i in range(len(digs)):
    if 10 <= abs(digs[i]) <= 99:
        digs[i] = 0

print(digs)