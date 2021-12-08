import math

lst = list(map(int, str(open("input.txt").readline()).split(",")))

def funk1(lista):
    dev = sum(lista) // len(lista)
    weight_list = []
    for i in range(dev - 200, dev + 200):
        weight = sum(abs(x - i) for x in lista)
        weight_list.append(weight)
    return min(weight_list)

def funk2(lista):
    dev = sum(lista) // len(lista)
    weight_list = []
    for i in range(dev - 200, dev + 200):
        weight = sum(int(abs(x - i) * (abs(x - i)) / 2) for x in lista)
        weight_list.append(weight)
    return min(weight_list)

print(funk1(lst))
print(funk2(lst))