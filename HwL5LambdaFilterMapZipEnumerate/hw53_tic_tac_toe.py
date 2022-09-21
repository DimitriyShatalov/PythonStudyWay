# 53. Создайте программу для игры в ""Крестики-нолики"".

print("*" * 10, "Крестики нолики v 1.0", "*" * 10)
board = list(range(1, 10)) # Создаем список из 9 элементов

# Далее из списка припомощи функции def draw_board создаем поле (board)
def draw_board(board):
    print('-' * 13)
    for i in range(3): # Создаем три поля ?
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|') # Рисуем поле
        print('-' * 13)
# draw_board(board)

# При помощи функции def take_input собираем информацию от пользователей
#  и проверяем правильно ли пользователеь вводит необходимые цифры
#  пользователь может вводить цифры от 1 до 9, которые еще не закрыты
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим: " + player_token + '?')

        try:
            player_answer = int(player_answer)
        except:
            print('Некоректный ввод. Вы уверены, что ввели число?')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if(str(board[player_answer - 1]) not in 'XO'):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print('Эта клетка уже занята!')

        else:
            print('Введите число от 1 до 9')

# При помощи функции def check_win прописываем все выигрышные варианты
def check_win(board):
    win_coord =((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

#  Если выигрыш состоялся, то при помощи функции main описываем, как это может происходить

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter +=1

        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, 'Ты выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break
    draw_board(board)
main(board)