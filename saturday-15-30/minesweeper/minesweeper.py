# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(a[1][0])

import random

difficulty = input("Select your difficulty: 1- Easy 2- Normal 3- difficult 4- insane 5- hard as heck").trim()

match difficulty:
    case "1":
        print("You selected easy")
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
class Cell:
    def __init__(self):
        self.opened = False     
        self._has_mine = False
    def has_mine(self):
        return self._has_mine
    def set_mine(self):
        self._has_mine = True
    def open(self):
        self.opened = True 

# a = [
#     [Cell, Cell, Cell],
#     [Cell, Cell, Cell],
#     [Cell, Cell, Cell]
# ]


def display_board(board):
    pass
    

def create_board(height, width, mines):
    board = []
    for _ in range(height):
        row = []
        for _ in range(width):      
            row.append(Cell())
        board.append(row)
    place_mines(board, mines)

def place_mines(board, mines):
    height = len(board)
    width = len(board[0])
# len - возвращает количество элементов в объекте
    
    mine_positions = random.sample([(x, y) for x in range(width) for y in range(height)], mines)
    for x, y in mine_positions:
        board[y][x].set_mine() 
# вообще не уверен в правильности
# генератор, котрый создает список всех возможных позиций на доске


