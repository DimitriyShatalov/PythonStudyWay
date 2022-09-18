# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

num = int(input("Enter number: "))
i = 2
lst = []
figure = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f'The prime factors of the number {figure} are given in the list: {lst}')
