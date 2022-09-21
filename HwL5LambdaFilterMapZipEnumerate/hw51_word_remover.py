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


exit()

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)

with open("words.txt", "r") as fin:
    for line in fin:
        words = line.split()
for word in words:
    if "абв" in word:
        words.remove(word)
        sentence = " ".join(words)
print(sentence)

with open('tex.txt','r') as n:
    lst = [int(i) for i in n.readline().split()]
    for i in range(1,len(lst)):
        if lst[i] - lst[i - 1] > 1:
            print(lst[i]-1)

