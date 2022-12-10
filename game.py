from tkinter import *
import random
from cell import Cell
import sys

class Game:
    can_move_left = True
    can_move_right = True
    can_move_up = True
    can_move_down = True
    root = Tk()
    label_grid = None
    cells = None
    up_button = None
    down_button = None
    left_button = None
    right_button = None
    

    @classmethod
    def print_cells(cls):
        for row in cls.cells:
            for cell in row:
                print (cell, end=" ")
            print ("")

    @classmethod
    def update_labels(cls):
        for row_num in range(4):
            for col_num in range(4):
                cls.label_grid[row_num][col_num].config(text=cls.cells[row_num][col_num])

    @classmethod
    def generate_random_cell(cls):
        while True:
            x = random.randint(0,3)
            y = random.randint(0,3)
            if cls.cells[y][x].value == 0:
                cls.cells[y][x].rand_val()
                break

    @classmethod
    def init_board(cls):
        cls.cells = [[Cell() for _ in range (4)] for _ in range(4)]

        cls.label_grid = [[Label(cls.root) for _ in range(4)] for _ in range(4)]

        cls.up_button = Button(cls.root, text="^", command=cls.move_up)
        cls.left_button = Button(cls.root, text="<", command=cls.move_left)
        cls.right_button = Button(cls.root, text=">", command=cls.move_right)
        cls.down_button = Button(cls.root, text="v", command=cls.move_down)

        cls.up_button.grid(row=4, column=1, columnspan=2)
        cls.left_button.grid(row=5, column=0, columnspan=2)
        cls.right_button.grid(row=5, column=2, columnspan=2)
        cls.down_button.grid(row=6, column=1, columnspan=2)

        for row_num in range(4):
            for col_num in range(4):
                cls.label_grid[row_num][col_num].grid(row=row_num, column=col_num)

        for _ in range(2):
            cls.generate_random_cell()

        cls.update_labels()

    @classmethod
    def check_board(cls):

        can_move_left = 0
        can_move_right = 0
        can_move_up = 0
        can_move_down = 0

        for i in range(4):
            for j in range(4):
                cls.cells[j][i].merged = False
                if cls.cells[j][i].value == 2048:
                    cls.end_game("you win!")
                if cls.cells[j][i].value == 0:
                    continue
                if j != 0 and (cls.cells[j][i] == cls.cells[j - 1][i] or cls.cells[j - 1][i].value == 0):
                    can_move_up += 1
                if i != 0 and (cls.cells[j][i] == cls.cells[j][i - 1] or cls.cells[j][i - 1].value == 0):
                    can_move_left += 1
                if j != 3 and (cls.cells[j][i] == cls.cells[j + 1][i] or cls.cells[j + 1][i].value == 0):
                    can_move_down += 1
                if i != 3 and (cls.cells[j][i] == cls.cells[j][i + 1] or cls.cells[j][i + 1].value == 0):
                    can_move_right += 1

        cls.can_move_left = can_move_left > 0
        cls.can_move_right = can_move_right > 0
        cls.can_move_up = can_move_up > 0
        cls.can_move_down = can_move_down > 0
        if not (cls.can_move_left or cls.can_move_right or cls.can_move_up or cls.can_move_down):
            cls.end_game("you lose!")

    @classmethod
    def play_game(cls):

        Game.init_board()

        cls.root.mainloop()

    @classmethod
    def move_left(cls):

        if not cls.can_move_left:
            return

        for i in range(4):
            for j in range(4):
                x = j
                y = i
                if cls.cells[y][x].value == 0:
                    continue
                while True:
                    if x == 0:
                        break
                    elif cls.cells[y][x - 1].value == 0:
                        cls.cells[y][x - 1].swap(cls.cells[y][x])
                        x -= 1
                    elif cls.cells[y][x - 1] == cls.cells[y][x]:
                        cls.cells[y][x - 1].merge(cls.cells[y][x])
                        break
                    else:
                        break

        cls.generate_random_cell()
        cls.update_labels()
        cls.check_board()

    @classmethod
    def move_right(cls):

        if not cls.can_move_right:
            return

        for i in range(4):
            for j in range(4):
                x = 3 - j
                y = i
                if cls.cells[y][x].value == 0:
                    continue
                while True:
                    if x == 3:
                        break
                    elif cls.cells[y][x + 1].value == 0:
                        cls.cells[y][x + 1].swap(cls.cells[y][x])
                        x += 1
                    elif cls.cells[y][x + 1] == cls.cells[y][x]:
                        cls.cells[y][x + 1].merge(cls.cells[y][x])
                        break
                    else:
                        break

        cls.generate_random_cell()
        cls.update_labels()
        cls.check_board()
    
    @classmethod
    def move_up(cls):

        if not cls.can_move_up:
            return

        for j in range(4):
            for i in range(4):
                x = j
                y = i
                if cls.cells[y][x].value == 0:
                    continue
                while True:
                    if y == 0:
                        break
                    elif cls.cells[y - 1][x].value == 0:
                        cls.cells[y - 1][x].swap(cls.cells[y][x])
                        y -= 1
                    elif cls.cells[y - 1][x] == cls.cells[y][x]:
                        cls.cells[y - 1][x].merge(cls.cells[y][x])
                        break
                    else:
                        break

        cls.generate_random_cell()
        cls.update_labels()
        cls.check_board()

    @classmethod
    def move_down(cls):

        if not cls.can_move_down:
            return

        for j in range(4):
            for i in range(4):
                x = j
                y = 3 - i
                if cls.cells[y][x].value == 0:
                    continue
                while True:
                    if y == 3:
                        break
                    elif cls.cells[y + 1][x].value == 0:
                        cls.cells[y + 1][x].swap(cls.cells[y][x])
                        y += 1
                    elif cls.cells[y + 1][x] == cls.cells[y][x]:
                        cls.cells[y + 1][x].merge(cls.cells[y][x])
                        break
                    else:
                        break

        cls.generate_random_cell()
        cls.update_labels()
        cls.check_board()

    @classmethod
    def end_game(cls, message):
        Label(cls.root, text=message).grid(row=7, column=1, columnspan=2)

        cls.up_button.config(state=DISABLED)
        cls.down_button.config(state=DISABLED)
        cls.left_button.config(state=DISABLED)
        cls.right_button.config(state=DISABLED)

def main():

    Game.play_game()

if __name__ == "__main__":
    main()