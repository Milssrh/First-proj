import os
import random
from datetime import datetime

if not os.path.exists('stats'):
    os.makedirs('stats')

statsu_file = 'stats/game_stats.txt'

def save_stats(mode, result, board_size, first_player):
    with open(statsu_file, 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} | Режим: {mode} | Размер поля: {board_size} | "
                f"Первый игрок: {first_player} | Результат: {result}\n")

def print_board(board):
    print("\n    " + " ".join(str(i+1) for i in range(len(board))))  
    
    for i, row in enumerate(board):
        print(f"{i+1}   " + " ".join(row))

def check_win(board):
    size = len(board)
    for i in range(size):
        if all(board[i][j] == 'x' for j in range(size)) or all(board[j][i] == 'x' for j in range(size)):
            return 'x'
        if all(board[i][j] == 'o' for j in range(size)) or all(board[j][i] == 'o' for j in range(size)):
            return 'o'
    
    if all(board[i][i] == 'x' for i in range(size)) or all(board[i][size-1-i] == 'x' for i in range(size)):
        return 'x'
    if all(board[i][i] == 'o' for i in range(size)) or all(board[i][size-1-i] == 'o' for i in range(size)):
        return 'o'
    
    if all(cell != ' ' for row in board for cell in row):
        return 'Ничья'
    
    return None

def get_player_move(board, player):
    size = len(board)
    while True:
        try:
            row = int(input(f"Игрок {player}, введите номер строки (1-{size}): ")) - 1
            col = int(input(f"Игрок {player}, введите номер столбца (1-{size}): ")) - 1
            if 0 <= row < size and 0 <= col < size:
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("Эта клетка уже занята!")
            else:
                print(f"Некорректные координаты! Введите числа от 1 до {size}.")
        except ValueError:
            print("Пожалуйста, вводите только числа.")

def bot_move(board):
    empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == ' ']
    return random.choice(empty_cells)

def play_game():
    try:
        size = int(input("Введите размер игрового поля. Например, 3 для 3x3: "))
        if size < 3:
            print("Минимальный размер поля - 3! Установлен размер 3.")
            size = 3
    except:
        print("Некорректный ввод! Установлен размер 3.")
        size = 3
    
    mode = input("Выберите режим: 1 - два игрока, 2 - против бота: ").strip()
    if mode not in ['1', '2']:
        print("Автоматически выбран режим: два игрока")
        mode = '1'

    current_player = random.choice(['x', 'o'])
    first_player = current_player
    board = [[' ' for _ in range(size)] for _ in range(size)]
    
    print(f"\n Первым ходит: {current_player}")
    
    while True:
        print_board(board)
        
        if current_player == 'x' or mode == '1':
            row, col = get_player_move(board, current_player)
        else:
            print("Ход бота...")
            row, col = bot_move (board)
            print(f"Бот поставил {current_player} на позицию ({row+1}, {col+1})")
        
        board[row][col] = current_player
        
        result = check_win(board)
        if result:
            print_board(board)
            if result == 'Ничья':
                print("\n Ничья!")
                save_stats("Два игрока" if mode == '1' else "Против бота", 
                          "Ничья", size, first_player)
            else:
                print(f"\n Победил {result}!")
                save_stats("Два игрока" if mode == '1' else "Против бота",
                          f"Победил {result}", size, first_player)
            break
        
        current_player = 'o' if current_player == 'x' else 'x'

def menu():
    while True:
        play_game()
        again = input("\n Хотите сыграть еще раз? Да/Нет: ").lower()
        if again != "да":
            print("Спасибо за игру, приходите за следующей победой!")
            break

menu()
