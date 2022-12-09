import random
from cell import Cell

class Game:
    can_move_left = True
    can_move_right = True
    can_move_up = True
    can_move_down = True
    grid = [[Cell(), Cell(), Cell(), Cell()] for _ in range(4)]

    @classmethod
    def print_grid(cls):
        for row in cls.grid:
            for cell in row:
                print (cell, end=" ")
            print ("")

    @classmethod
    def generate_random_cell(cls):
        while True:
            x = random.randint(0,3)
            y = random.randint(0,3)
            if cls.grid[y][x].value == 0:
                cls.grid[y][x].rand_val()
                break

    @classmethod
    def init_board(cls):
        for _ in range(2):
            cls.generate_random_cell()

    @classmethod
    def check_board(cls):

        can_move_left = 0
        can_move_right = 0
        can_move_up = 0
        can_move_down = 0

        for i in range(4):
            for j in range(4):
                cls.grid[j][i].merged = False
                if cls.grid[j][i].value == 2048:
                    return True
                if cls.grid[j][i].value == 0:
                    continue
                if j != 0 and (cls.grid[j][i] == cls.grid[j - 1][i] or cls.grid[j - 1][i].value == 0):
                    can_move_up += 1
                if i != 0 and (cls.grid[j][i] == cls.grid[j][i - 1] or cls.grid[j][i - 1].value == 0):
                    can_move_left += 1
                if j != 3 and (cls.grid[j][i] == cls.grid[j + 1][i] or cls.grid[j + 1][i].value == 0):
                    can_move_down += 1
                if i != 3 and (cls.grid[j][i] == cls.grid[j][i + 1] or cls.grid[j][i + 1].value == 0):
                    can_move_right += 1

        print ("left:", can_move_left)
        print ("right:", can_move_right)
        print ("up:", can_move_up)
        print ("down:", can_move_down)

        cls.can_move_left = can_move_left > 0
        cls.can_move_right = can_move_right > 0
        cls.can_move_up = can_move_up > 0
        cls.can_move_down = can_move_down > 0
        return False

    @classmethod
    def play_game(cls):
        while True:
            cls.print_grid()
            try:
                move = input("Next move: ")
            except EOFError:
                break

            if move == "left" and cls.can_move_left:
                cls.move_left()
            elif move == "right" and cls.can_move_right:
                cls.move_right()
            elif move == "up" and cls.can_move_up:
                cls.move_up()
            elif move == "down" and cls.can_move_down:
                cls.move_down()
            else:
                print ("Invalid move")
                continue

            cls.generate_random_cell()

            if cls.check_board():
                print ("You Win!!!")
                return

            print (cls.can_move_left)
            print (cls.can_move_right)
            print (cls.can_move_up)
            print (cls.can_move_down)


            if not (cls.can_move_left or cls.can_move_right or cls.can_move_up or cls.can_move_down):
                print ("Game Over! Better luck next time!")
                return

    @classmethod
    def move_left(cls):

        for i in range(4):
            for j in range(4):
                x = j
                y = i
                if cls.grid[y][x].value == 0:
                    continue
                while True:
                    if x == 0:
                        break
                    elif cls.grid[y][x - 1].value == 0:
                        cls.grid[y][x - 1].swap(cls.grid[y][x])
                        x -= 1
                    elif cls.grid[y][x - 1] == cls.grid[y][x]:
                        cls.grid[y][x - 1].merge(cls.grid[y][x])
                        break
                    else:
                        break

    @classmethod
    def move_right(cls):

        for i in range(4):
            for j in range(4):
                x = 3 - j
                y = i
                if cls.grid[y][x].value == 0:
                    continue
                while True:
                    if x == 3:
                        break
                    elif cls.grid[y][x + 1].value == 0:
                        cls.grid[y][x + 1].swap(cls.grid[y][x])
                        x += 1
                    elif cls.grid[y][x + 1] == cls.grid[y][x]:
                        cls.grid[y][x + 1].merge(cls.grid[y][x])
                        break
                    else:
                        break
    
    @classmethod
    def move_up(cls):

        for j in range(4):
            for i in range(4):
                x = j
                y = i
                if cls.grid[y][x].value == 0:
                    continue
                while True:
                    if y == 0:
                        break
                    elif cls.grid[y - 1][x].value == 0:
                        cls.grid[y - 1][x].swap(cls.grid[y][x])
                        y -= 1
                    elif cls.grid[y - 1][x] == cls.grid[y][x]:
                        cls.grid[y - 1][x].merge(cls.grid[y][x])
                        break
                    else:
                        break

    @classmethod
    def move_down(cls):

        for j in range(4):
            for i in range(4):
                x = j
                y = 3 - i
                if cls.grid[y][x].value == 0:
                    continue
                while True:
                    if y == 3:
                        break
                    elif cls.grid[y + 1][x].value == 0:
                        cls.grid[y + 1][x].swap(cls.grid[y][x])
                        y += 1
                    elif cls.grid[y + 1][x] == cls.grid[y][x]:
                        cls.grid[y + 1][x].merge(cls.grid[y][x])
                        break
                    else:
                        break

def main():

    Game.init_board()

    Game.play_game()

if __name__ == "__main__":
    main()