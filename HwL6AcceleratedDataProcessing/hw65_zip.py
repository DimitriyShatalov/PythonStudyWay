
# Вычисление в парах/ Рассчет прибыли
# Пример:
# Нименование/Месяц 	     Январь	     Февраль	     Март
# Всего продано               52,000.00	     51,000.00	     48,000.00
# Производ-ные затраты   	46,800.00	     45,900.00	     43,200.00


total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]

for sales, costs in zip(total_sales, prod_cost):
     profit = sales - costs
     print(f'Total profit: {profit}')
     
# Создание словарей и работа с ними
fields = ['name', 'last_name', 'age', 'job']
values = ['Dir', 'Kirk', '55', 'Product Manager']

a_dict = dict(zip(fields, values))
print(a_dict)

new_job = ['Consultant']
field = ['job']
a_dict.update(zip(field, new_job))
print(a_dict)