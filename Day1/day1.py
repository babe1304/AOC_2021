lst = [int(x) for x in open("AOC/Day1/input.txt", "r")]

#prvi dio
b = 0
for br in range(len(lst) - 1):
    if lst[br] < lst[br + 1]:
        b += 1
print(b)

#drugi dio
b = 0
sum = lst[0] + lst[1] + lst[2]

for br in range(len(lst) - 2):
    sum2 = lst[br] + lst[br + 1] + lst[br + 2] 
    if sum < sum2:
        b += 1
    sum = sum2
print(b)
