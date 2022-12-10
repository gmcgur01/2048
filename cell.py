import random

class Cell:

    def __init__(self):
        self.value = 0
        self.merged = False

    def __str__(self):
        if self.value == 0: 
            return " "
        return str(self.value)

    def __eq__(left, right):
        return left.value == right.value

    def __ne__(left, right):
        return not left == right

    def rand_val(self):
        if random.random() > .75:
            self.value = 4
        else:
            self.value = 2

    def merge(self, other):
        if not self.merged:
            self.value += other.value
            self.merged = True
            other.value = 0
            other.merged = False
    
    def swap(self, other):
        temp = self.value
        self.value = other.value
        other.value = temp

def main():
    cell1 = Cell()
    cell2 = Cell()

    print(cell1 == cell2)
    print(cell1 != cell2)

    cell2.rand_val()

    print(cell1 == cell2)
    print(cell1 != cell2)

if __name__ == "__main__":
    main()