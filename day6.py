file = open('inputs/day6.txt', 'r')
#file = open('inputs/day3.txt', 'r')
lines = file.read().split('\n')

def parse_input(lines):
    all_times=[]
    all_distances=[]

    times = lines[0].split(" ")
    distances = lines[1].split(" ")

    for i in times:
        if(i.isdigit()):
            all_times.append(i)
    for i in distances:
        if(i.isdigit()):
            all_distances.append(i)
    return [all_times,all_distances]

def parse_new_input():
    new_time=""
    new_distance=""
    for time in input[0]:
        new_time+=time
    for distance in input[1]:
        new_distance+=distance
    return [[new_time],[new_distance]]

def get_boat_distance(milliseconds_charge,time):
    runtime = time-milliseconds_charge
    distance = runtime*milliseconds_charge
    return distance

def get_total_number_of_ways_to_win(input):
    total = 1
    for race in range(0,len(input[0])):
        number_of_ways_to_win = 0
        time = input[0][race]
        distance = input[1][race]
        
        for i in range(0,int(time)):
            boat_distance = get_boat_distance(i,int(time))
            if(boat_distance>int(distance)):
                number_of_ways_to_win +=1
        total*=number_of_ways_to_win 
    return total

input = parse_input(lines)
print("part 1: ", get_total_number_of_ways_to_win(input))
new_input = parse_new_input()
print("part 2 ", get_total_number_of_ways_to_win(new_input))















    