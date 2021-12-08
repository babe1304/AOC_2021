class LanternFish:
    def __init__(self, days):
        self.days = days

    def update(self):
        if self.days == 0:
            self.days = 6
            return LanternFish(8)
        else:
            self.days -= 1
            return None

lst = str(open("input.txt").readline()).split(",")

def funk(days):
    fish_list = [LanternFish(int(day)) for day in lst]
    for i in range(days):
        for i in range(len(fish_list)):
            new_fish = fish_list[i].update()
            if new_fish != None:
                fish_list.append(new_fish)
    return len(fish_list)

def cycle(fish_dict):
    new_fish_dict = {}
    for day in range(8):
        new_fish_dict[day] = fish_dict[day + 1]
    new_fish_dict[6] = fish_dict[7] + fish_dict[0]
    new_fish_dict[8] = fish_dict[0]
    for i in range(9):
        fish_dict[i] = new_fish_dict[i]

def new_funk(days):
    fish_list = [int(num) for num in lst]
    fish_dict = {}
    for day in range(9):
        fish_dict[day] = fish_list.count(day)
         
    for i in range(days):
        cycle(fish_dict)

    return sum(fish_dict.values())

print(funk(80))
print(new_funk(80))
print(new_funk(256))
