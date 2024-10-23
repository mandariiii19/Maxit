import random #импортируем модуль random, который позволяет генерировать случайные числа
#Создаем поле три на три
board = random.sample(range(1,10),9) #генерация 9 уникальных случайных чисел от 1 до 9
board = [board[:3],board[3:6], board[6:]] #разделение на строки
score1 = 0 #счётчик очков игрока 1
score2 = 0 #счётчик очков игрока 2
player = 1 #номер игрока который будет ходить первым
pos = [None,None] #координаты текущего хода: строка, столбец

def getboard(): #создаём функцию для отображения игрового поля
    for row in board:
        print(" | ".join(str(x) if x is not None else " " for x in row))
        print("-" * 9)
        
def avail_moves(player, pos): #создаем функцию,которая будет определять доступные ходы игроков
    moves = []
    if player == 1 and pos[0] is not None:  #Игрок 1 выбирает по строке
        for j in range(3):
            if board[pos[0]][j] is not None:
                moves.append((pos[0], j))
    elif player == 2 and pos[1] is not None:  #Игрок 2 выбирает по столбцу
        for i in range(3):
            if board[i][pos[1]] is not None:
                moves.append((i, pos[1]))
    else:  #Если первый ход или нет ограничений (для первого хода любого игрока)
        for i in range(3):
            for j in range(3):
                if board[i][j] is not None:
                    moves.append((i, j))
    return moves
print("Начнём игру.\nНачинающий игрок ходит по строкам, следующий - по столбцам.")
getboard()
while True: 
    moves = avail_moves(player, pos)
    if not moves:#если ходов нет у текущего игрока
        print(f"У игрока {player} нет ходиков")
        if not avail_moves(2 if player == 1 else 1, pos):#проверка на отсутствие ходов у обоих игроков
            print("Игра окончена!")
            break
        player = 2 if player == 1 else 1
        continue
    #что такое continue: если ходов нет у обоих игроков, игра завершается (break выходит из цикла) 
    #если ходы есть у другого игрока, программа меняет текущего игрока и переходит к следующей итерации цикла с помощью continue
    print(f"\nХод игрока {player}. Доступные ходы: {[(r+1, c+1) for r, c in moves]}")
    while True: #ввод координат и проверка их правильности
        try:
            row,col = map(int,input("Введите координаты ходов (строка,столбец): ").split())
            row-=1
            col-=1
            if (row,col) in moves:
                break
            else:
                print("Неверный ход")
        except ValueError:
            print("Введите два числа через пробел.")
    number = board[row][col]
    board[row][col] = None #вычеркиваем выбранное число
    if player == 1:
        score1 += number
        pos[1] = col #запоминаем столбец для следующего хода игрока 2
    else:
        score2 += number
        pos[0] = row #запоминаем строку для следующего хода игрока 1
    getboard()
    player = 2 if player ==1 else 1 #переход хода
#вывод результата игры
print('\nИгра окончена')
print(f'Очки игрока номер 1: {score1}')
print(f'Очки игрока номер 2: {score2}')
if score1 > score2:
    print('Победитель - игрок номер 1!')
elif score2 > score1:
    print('Победитель - игрок номер 2!')
else:
    print('У вас ничья!')
