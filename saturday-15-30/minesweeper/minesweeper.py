import random

class Cell:
    def __init__(self):
        self._opened = False     
        self._has_mine = False
        self._neighbouring_mines = 0
        self._display = '-'

    def has_mine(self):
        return self._has_mine
    
    def set_mine(self):
        self._has_mine = True

    def open(self):
        self._opened = True
        self._display = ' '

    def is_opened(self):
        return self._opened
    
    def increment_neighbouring_mines(self):
        self._neighbouring_mines += 1
        self._display = str(self._neighbouring_mines)
        
    def __str__(self):
        return self._display
    
    def get_neighbouring_mines_number(self):
        return self._neighbouring_mines


def display_board(board):
    print(" ", end = " ")
    for x in range(len(board[0])):
        print(x, end = " ")
    print()

    for y, row in enumerate(board):
        print(y, end = " ")
        for cell in row:
            # if cell.has_mine():
            #     print("*", end = " ")
            # else:
            print(cell, end = " ")
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
# генератор, котрый создает список всех возможных позиций на доске

def filter_cords(k):
    return k[0]>=0 and k[1]>=0

def open_space(board, x, y):
        cell = board[y][x]
        if cell.is_opened():
            return
        cell.open()
        neighbours = [
            (y-1, x-1), (y-1, x), (y-1, x+1),
            (y, x-1),             (y, x+1),
            (y+1, x-1), (y+1, x), (y+1,x+1)
        ]
        neighbours = list(filter(lambda k: k[0]>=0 and k[1]>=0, neighbours))

        # cell.neigbouring_mines += 1
        for (r, c) in neighbours:
            try:
                neighbour_cell = board[r][c]
                if neighbour_cell.has_mine():
                    cell.increment_neighbouring_mines()
            except IndexError:
                pass

        if cell.get_neighbouring_mines_number() == 0:
            for (r, c) in neighbours:
                try:
                    neighbour_cell = board[r][c]
                    if not neighbour_cell.has_mine():
                        open_space(board, c, r)
                except IndexError:
                    pass

                
def play(board):
    while True:
        display_board(board)
        while True:
            try:
                x, y = map(int, input("Enter coordinates (x y): ").split())
                cell = board[y][x]
                break
            except ValueError:
                print("Invalid input")
            except IndexError:
                print("Index out of range")

        if cell.has_mine():
            print('Game over! You hit a mine.')
            break
        else:
            open_space(board, x, y)

        if all([board[r][c].has_mine() or board[r][c].is_opened() for r in range(len(board)) for c in range(len(board[0]))]):
            print("You won!")
            break
def init_game(height, width, mines):
    board = create_board(height, width, mines)
    play(board)

difficulty = input("Select your difficulty: 1- Easy 2- Normal 3- difficult 4- insane 5- hard as heck ##- FUN value ").strip()

match difficulty:
    case "1":
        print("You selected easy")
        init_game(10, 10, 10)
    case "2":
        print("You selected normal")
        init_game(10, 10, 20)
    case "3":
        print("You selected difficult")
        init_game(10, 10, 30)
    case "4":
        print("You selected insane")
        init_game(15, 15, 50)
    case "5":
        print("You selected hard as heck")
        init_game(15, 15, 75)
    case "61":
        print("You selected FUN value")
        init_game(16, 16, 100)
    case _:
        print("Invalid selection")
        exit()
        