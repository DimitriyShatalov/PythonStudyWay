# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

positions = []

# file = open('file.txt', 'a')


# Открываем файл file.txt для чтения
file = open('file.txt', 'r')

# Считывание и добавление в список positions каждой строки из файла 
for line in file:
	positions.append(int(line))

# Нахождение максимальной позиции в списке
n = max(positions)

# Создание списка из 2 * N элементов
list_n = []
for i in range(2 * n):
	# Заполняем случайными числами от -10 до 10
	list_n.append(randint(-10, 10))

# Произведение элементов списка в указанных позициях
p = 1
for position in positions:
	p *= list_n[position]

# print(list_n)
print(p)

# Закрываем файл file.txt
file.close()