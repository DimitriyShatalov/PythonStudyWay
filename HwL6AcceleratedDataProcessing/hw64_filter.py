# При помощи фукции filter отбираем простые, нечетные числа
# *Простое число - это число, которое делится на себя и единицу
# *Четное число кратно 2

def is_simple(x):
    num_d = x - 1
    if num_d < 0 or x % 2 == 0:
        return False

    while num_d > 1:
        if x % 2 == 0:
            return False
        num_d -= 1

    return True

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

value = filter(is_simple, lst)
print(list(value))