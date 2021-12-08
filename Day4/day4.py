numbers = open("input2.txt").readline().replace("\n", "").split(",")
lst = [str(x).replace("\n", "") for x in open("input.txt").readlines()[2:]]

def clean_string(string):
    lista = string.split(" ")
    for i in range(len(lista)):
        if lista[i] == "":
            lista.remove("")
    return lista

class bingo_board:
    null_lst = [[0] * 5 for i in range(5)]

    def __init__(self, lst):
        self.lst = lst

    def check_number(self, num):
        for i in range(5):
            for j in range(5):
                if int(lst[i][j]) == num:
                    print("number found")
                    self.null_lst[i][j] = 1
                    break
        return

    def check_bingo(self):
        bingo = False
        for i in range(5):
            bingo = (self.null_lst[i][0] == 1 and self.null_lst[i][1] == 1 and self.null_lst[i][2] == 1 and self.null_lst[i][3] == 1 and self.null_lst[i][4] == 1)
            if bingo:
                return True
        for i in range(5):
            bingo = (self.null_lst[0][i] == 1 and self.null_lst[1][i] == 1 and self.null_lst[2][i] == 1 and self.null_lst[3][i] == 1 and self.null_lst[4][i] == 1)
            if bingo:
                return True
        return False

    def print_board(self):
        print(self.lst)
        print(self.null_lst)

    def result(self, last_num):
        sum = 0
        for i in range(5):
            for j in range(5):
                if self.null_lst[i][j] == 0:
                    sum += int(self.lst[i][j])
        return sum * last_num

bingo_list = []
parts = []
br = 0
for el in lst:
    if el == "":
        print(parts)
        bingo_list.append(bingo_board(parts))
        parts = []
        br += 1
        continue
    parts.append(clean_string(el))

for num in numbers:
    bingo = False
    for board in bingo_list:
        board.print_board()
        board.check_number(num)
        if board.check_bingo():
            bingo = True
            print("BINGO!")
            print(board.result(num))
            break
    if bingo:
        break