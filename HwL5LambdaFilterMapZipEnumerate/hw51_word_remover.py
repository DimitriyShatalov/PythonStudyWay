# 54.Напишите программу, удаляющую из текста все слова, содержащие "abv".
from http.client import NOT_FOUND


try:
    with open('file_abv.txt') as f:
        content = f.read()
except FileNotFoundError:
    content = '<<<NOT_FOUND>>>'

print(f'Исходный текст:\n {content}')
find_txt = 'abv'
lst = [i for i in content.split() if find_txt not in i]
print(f'Результат:\n {" ".join(lst)}')

