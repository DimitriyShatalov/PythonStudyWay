# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

lst = list(map(int, input('Enter numbers separated by a space: ').split()))
print(f"Source list: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"A list of non-repeating elements: {new_lst}")










# v = []
# for i in range(1, n+1):
#     v += [str(i)] * i
# print(" ".join(v[:n]))

# # Используя генераторы списков, всё это можно записать в одну строку:
# print(" ".join([str(i) for i in range(1, n+1) for j in range(i)][:n]))

# # А вот более эффективный код, который генерирует ровно столько данных, сколько нужно
# v = []
# for i in range(1, n+1):
#     c = min(n, i)
#     n = n - c
#     v += [str(i)] * c
#     if n <= 0:
#         break
# print(" ".join(v))

# Не теряя эффективности, но выигрывая в понятности, 
# можно немножко поиграть с генераторами (не путать с генераторами списков!):

# def generator(m):
#     c = 0
#     for i in range(1, m+1):
#         for j in range(i):
#             c += 1
#             if c > m:
#                 return
#             yield str(i)
# print(" ".join(generator(n)))