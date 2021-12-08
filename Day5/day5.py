def reduce_to_pairs(string):
    lista = string.split(" -> ")
    lista = map(lambda x: x.replace("\n", ""), lista)
    lista = map(lambda x: x.split(","), lista)
    return int(lista[0][0]), int(lista[0][1]), int(lista[1][0]), int(lista[1][1])
lst = [str(x) for x in open("input.txt").readlines()]

def part1(lst):
    null_list = [[0] * 1000 for i in range(1000)]
 
    for line in lst:
        x1, y1, x2, y2 = reduce_to_pairs(line)
        
        if x1 == x2:
            big = max(y1, y2)
            small = min(y1, y2)
            for i in range(small, big + 1):
                null_list[x1][i] += 1
        elif y1 == y2:
            big = max(x1, x2)
            small = min(x1, x2)
            for i in range(small, big + 1):
                null_list[i][y1] += 1
        else:
            continue
    sum = 0
    for line in null_list:
        for num in line:
            if num >= 2:
                sum += 1
    return sum

def part2(lst):
    null_list = [[0] * 1000 for i in range(1000)]

    for line in lst:
        x1, y1, x2, y2 = reduce_to_pairs(line)

        if x1 == x2:
            big = max(y1, y2)
            small = min(y1, y2)
            for i in range(small, big + 1):
                null_list[x1][i] += 1
        elif y1 == y2:
            big = max(x1, x2)
            small = min(x1, x2)
            for i in range(small, big + 1):
                null_list[i][y1] += 1
        else:
            big_x = max(x1, x2)
            small_x = min(x1, x2)
            if (y1 > y2 and x2 > x1) or (y2 > y1 and x1 > x2):
                big_y = max(y1, y2)
                for i in range(small_x, big_x + 1):
                    null_list[i][big_y] += 1
                    big_y -= 1
            elif (y2 > y1 and x2 > x1) or (y1 > y2 and x1 > x2):
                small_y = min(y1, y2)
                for i in range(small_x, big_x + 1):
                    null_list[i][small_y] += 1
                    small_y += 1
    sum = 0
    for line in null_list:
        for num in line:
            if num >= 2:
                sum += 1
    return sum

print(part1(lst))
print(part2(lst))