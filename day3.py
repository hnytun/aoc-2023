import re
file = open('inputs/day3.txt', 'r')
#file = open('inputs/day3.txt', 'r')
lines = file.read().split('\n')

def is_symbol(char):
    if not char.isdigit() and char != '.':
        #print(char, " is a symbol!")
        return True
    else:
        return False
    
def is_part_number(pos,list):
    
    if(pos[1]-1 >= 0):
        left=list[pos[0]][pos[1]-1]
    else:
        left=None
    if(pos[1]+1 < len(list[1])):       
        right=list[pos[0]][pos[1]+1]
    else:
        right=None
    if(pos[0]-1 >= 0):
        up=list[pos[0]-1][pos[1]]
    else:
        up=None
    if(pos[0]+1 < len(list)):
        down = list[pos[0]+1][pos[1]]
    else:
        down=None
    if(pos[0]-1 >= 0 and pos[1]-1 >= 0):
        top_left = list[pos[0]-1][pos[1]-1]
    else:
        top_left=None
    if(pos[0]-1 >= 0 and pos[1]+1 < len(list[1])):
        top_right = list[pos[0]-1][pos[1]+1]
    else:
        top_right=None
    if(pos[0]+1 < len(list) and pos[1]-1 >= 0):
        down_left = list[pos[0]+1][pos[1]-1]
    else:
        down_left=None
    if(pos[0]+1 < len(list) and pos[1]+1 < len(list)):
        down_right = list[pos[0]+1][pos[1]+1]
    else:
        down_right=None
    
    neighbours=[left,right,up,down,top_left,top_right,down_left,down_right]
    
    for neighbour in [x for x in neighbours if x != None]:
        if(is_symbol(neighbour)):
            return True
    return False

def get_numbers_and_position(list):
    numbers=[]
    current_number=["",[]]
    found_number=False
    for x in range(0,len(list)):
        for y in range(0,len(list[x])):
            if(list[x][y].isdigit()):
                found_number=True
                current_number[0] += list[x][y]
                current_number[1].append((x,y))

            if(found_number and x==len(list)-1 and y==len(list[x])-1):
                print("found number ", list[x][y])
                print("current number: ", current_number)
                numbers.append(current_number)
                found_number=False
                current_number = ["",[]]
                
            if(not list[x][y].isdigit() and found_number):
                numbers.append(current_number)
                current_number = ["",[]]
                found_number=False
                
            if(found_number and y == len(list[x])-1):
                numbers.append(current_number)
                found_number=False
                current_number = ["",[]]

    return numbers
    

def get_gear_positions(list):
    allGears=[]
    for x in range(0,len(list)):
        for y in range(0,len(list[x])):
            if(list[x][y] == '*'):
                allGears.append([x,y])
    return allGears

def get_gear_neighbours(pos,list):
    
    if(pos[1]-1 >= 0):
        left=(pos[0],pos[1]-1)
    else:
        left=None
    if(pos[1]+1 < len(list[1])):       
        right=(pos[0],pos[1]+1)
    else:
        right=None
    if(pos[0]-1 >= 0):
        up=(pos[0]-1,pos[1])
    else:
        up=None
    if(pos[0]+1 < len(list)):
        down = (pos[0]+1,pos[1])
    else:
        down=None
    if(pos[0]-1 >= 0 and pos[1]-1 >= 0):
        top_left = (pos[0]-1,pos[1]-1)
    else:
        top_left=None
    if(pos[0]-1 >= 0 and pos[1]+1 < len(list[1])):
        top_right = (pos[0]-1,pos[1]+1)
    else:
        top_right=None
    if(pos[0]+1 < len(list) and pos[1]-1 >= 0):
        down_left = (pos[0]+1,pos[1]-1)
    else:
        down_left=None
    if(pos[0]+1 < len(list) and pos[1]+1 < len(list)):
        down_right = (pos[0]+1,pos[1]+1)
    else:
        down_right=None
    
    neighbours=[left,right,up,down,top_left,top_right,down_left,down_right]
    return neighbours




sum=0
for number in get_numbers_and_position(lines):
    part=False
    for position in number[1]:
        if(is_part_number(position,lines)):
            part=True
    if(part):        
        sum+=int(number[0])

print("part1: ",sum)

all_gears=get_gear_positions(lines)
numbers = get_numbers_and_position(lines)
testGear=(1,3)
sum_gear_ratios=0

for gear in all_gears:
    gearNeighbours = get_gear_neighbours(gear,lines)
    all_part_number_neighbours=[]
    for neighbour in gearNeighbours:
        for number in numbers:
            if(neighbour in number[1]):
                all_part_number_neighbours.append(number[0])
    all_part_number_neighbours = list(set(all_part_number_neighbours))
    
    if(len(all_part_number_neighbours) == 2):
        sum_gear_ratios+= int(all_part_number_neighbours[0])*int(all_part_number_neighbours[1])
    
print("part2: ", sum_gear_ratios)
    


