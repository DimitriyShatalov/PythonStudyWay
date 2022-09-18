# 5.Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('poly1.txt', 'w') as file:
    file.write('8*x**3 + 2*x**5 - 4*y')

with open('poly2.txt', 'w') as file:
    file.write('41*x**4 + 9*y**6')
    
with open('poly1.txt','r') as file:
    poly1 = file.read()
    lst_poly1 = poly1.split()

with open('poly2.txt','r') as file:
    poly_2 = file.read()
    lst_poly2 = poly_2.split()

with open('sum_poly.txt', 'w') as file:
    file.write(f'{lst_poly1} + {lst_poly2}')

print(f'{lst_poly1} + {lst_poly2}')

