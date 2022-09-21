# 52. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from re import S

# m = 28
# candy = 2021
# quant = (candy % (m + 1))
# print(f'Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты?: ')
# print(quant)


# При помощи функции def take_input собираем информацию от пользователей
#  и проверяем правильно ли пользователеь вводит необходимые цифры
#  пользователь может вводить цифры от 1 до 9, которые еще не закрыты
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Ваш ход: " + player_token + '?')

        try:
            player_answer = int(player_answer)
        except:
            print('Некоректный ввод. Введите число не более 28?')
            continue
        if 1 > player_answer > 28:
        # #     if(str(board[player_answer - 1]) not in 'XO'):
        # #         board[player_answer - 1] = player_token
                valid = True
        else:

            print('Эта клетка уже занята!')

    else:
       
        take_input(player_token)
print('Введите число от 1 до 28')

# def main(candy):
#     counter = 0
#     win = False
#     while not win:
#         # draw_board(board)
#         if counter % 2 == 0:
#             take_input('X')
#         else:
#             take_input('O')
#         counter +=1

#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print(tmp, 'Ты выиграл!')
#                 win = True
#                 break
#         if counter == 9:
#             print('Ничья!')
#             break
#     draw_board(board)
# main(board)