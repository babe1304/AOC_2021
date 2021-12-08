lst = [x.split("|") for x in open("input.txt").readlines()]

def funk1(list):
    sum = 0
    for line in list:
        int_list = line[1].split()
        for num in int_list:
            if len(num) == 2 or len(num) == 4 or len(num) == 3 or len(num) == 7:
                sum += 1
    return sum

def funk2(list):
    sum = 0
    for line in list:
        nums_to_decode = line[0].split()
        nums_to_get = line[1].split()
        num_dict = dict()
        
        num_dict[1] = ''.join(filter(lambda x: len(x) == 2, nums_to_decode))
        num_dict[4] = ''.join(filter(lambda x: len(x) == 4, nums_to_decode))
        num_dict[7] = ''.join(filter(lambda x: len(x) == 3, nums_to_decode))
        num_dict[8] = ''.join(filter(lambda x: len(x) == 7, nums_to_decode))

        num_dict[3] = ''.join(filter(lambda x: len(x) == 5 and len(set(x).intersection(num_dict[1])) == 2, nums_to_decode)) 
        num_dict[9] = ''.join(filter(lambda x: len(x) == 6 and len(set(x).intersection(num_dict[3])) == 5, nums_to_decode))
        num_dict[2] = ''.join(filter(lambda x: len(x) == 5 and len(set(x).intersection(num_dict[4])) == 2, nums_to_decode))
        num_dict[6] = ''.join(filter(lambda x: len(x) == 6 and len(set(x).intersection(num_dict[1])) == 1, nums_to_decode))

        num_dict[5] = ''.join(filter(lambda x: len(x) == 5 and x not in num_dict[2] and x not in num_dict[3], nums_to_decode))
        num_dict[0] = ''.join(filter(lambda x: len(x) == 6 and x not in num_dict[6] and x not in num_dict[9], nums_to_decode)) 
        
        broj = ""
        for num in nums_to_get:
            for key, value in num_dict.items():
                if sorted(num) == sorted(value):
                    broj += str(key)
        sum += int(broj)
    return sum
                    
print(funk1(lst))
print(funk2(lst))
