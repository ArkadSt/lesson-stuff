# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(a[1][0])

import random
        
class Cell:
    def __init__(self):
        self._opened = False     
        self._has_mine = False
    def has_mine(self):
        return self._has_mine
    def set_mine(self):
        self._has_mine = True
    def open(self):
        self._opened = True 
    def is_opened(self):
        return self._opened


# create_board(10, 20, 10)
# board = [
#     [Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell,],
#     [Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell,],
#     [Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell,],
#     [Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell,],
#     [Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell,],
#     [Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell,],
#     [Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell,],
#     [Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell,],
#     [Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell,],
#     [Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell, Cell,Cell, Cell,]
# ]
# print(board[1][2])

# print ("что-то там") - выводит что-то там и переносит курсор на новую строку
# print ("что-то там", end = "") - выводит что-то там и не переносит курсор на новую строку
def display_board(board):

    for row in board:
        for cell in row:
            if cell.is_opened():
                print(" ", end = " ")
            elif cell.has_mine():
                print("*", end = " ")
            else:
                print("-", end = " ")
        print()


def create_board(height, width, mines):
    board = []
    for _ in range(height): # range(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        row = []
        for _ in range(width):      
            row.append(Cell())
        board.append(row)
    place_mines(board, mines)
    return board



def place_mines(board, mines):
    height = len(board)
    width = len(board[0])
# len - возвращает количество элементов в объекте
    
    mine_positions = random.sample([(x, y) for x in range(width) for y in range(height)], mines)
    for (x, y) in mine_positions:
        board[y][x].set_mine() 
# вообще не уверен в правильности
# генератор, котрый создает список всех возможных позиций на доске
#https://youtu.be/dQw4w9WgXcQ

# a = []
# for y in range(height):
#     for x in range(width):
#         a.append((x, y))

difficulty = input("Select your difficulty: 1- Easy 2- Normal 3- difficult 4- insane 5- hard as heck").strip()

match difficulty:
    case "1":
        print("You selected easy")
        board = create_board(10, 10, 10)
        display_board(board)
    case "2":
        print("You selected normal")
    case "3":
        print("You selected difficult")
    case "4":
        print("You selected insane")
    case "5":
        print("You selected hard as heck")
    case _:
        print("Invalid selection")
        exit()