lst = [i for i in open("input.txt").readlines()] #opcija da se stavi list(i)
#prvi dio
bit_map1, bit_map0 = {i : 0 for i in range(len(lst[0]) - 1)}, {i : 0 for i in range(len(lst[0]) - 1)}

gamma_rate, epsilon = "", ""

for num in lst:
    for j in range(len(num) - 1):
        if num[j] == "1":
            bit_value = bit_map1[j]
            bit_map1.update({j : bit_value + 1})
        else:
            bit_value = bit_map0[j]
            bit_map0.update({j : bit_value + 1})

for i in range(len(lst[0]) - 1):
    if bit_map1[i] > bit_map0[i]:
        gamma_rate += "1"
        epsilon += "0"
    else:
        gamma_rate += "0"
        epsilon += "1"
print(int(epsilon, 2) * int(gamma_rate, 2))

#Drugi dio
def common(list, i, comm=True):
    br0, br1 = 0, 0
    for el in list:
        if el[i] == "1":
            br1 += 1
        else:
            br0 += 1
    if comm:
        return 1 if br1 >= br0 else 0
    else:
        return 1 if br1 < br0 else 0

lstO, lstCO2 = lst, lst
for i in range(len(lst[0]) - 1):
    if len(lstO) != 1:
        comm = common(lstO, i)
        lstO = filter(lambda x: int(x[i]) == comm, lstO)

    if len(lstCO2) != 1:
        comm = common(lstCO2, i, comm=False)
        lstCO2 = filter(lambda x: int(x[i]) == comm, lstCO2)

print(int(lstCO2[0], 2) * int(lstO[0],  2))