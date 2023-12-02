import re
#file = open('inputs/day2_sample.txt', 'r')
file = open('inputs/day2.txt', 'r')
games = file.read().split('\n')

rgb_max = [12,13,14]

def check_possible(real,max):
    if(real[0] <= max[0] and real[1] <= max[1] and real[2] <= max[2]):
        return True
    else:
        return False

possible=0
sum_ids=0
all_fewest = []
for game in games:
    
    fewest=[0,0,0]
    id = int(game.split(" ")[1].split(":")[0])
    draws = [x.strip(' ') for x in game.split(": ")[1].split(";")]
    all_draws = []
    for draw in draws: 
        sets = draw.split(", ")
        rgb_real=[0,0,0]
        for set in sets:
            amount=int(set.split(' ')[0])
            color=set.split(' ')[1]
            match color:
                case "red":
                    rgb_real[0] +=amount
                    if(fewest[0] < rgb_real[0]):
                        fewest[0] = rgb_real[0]
                case "green":
                    rgb_real[1] +=amount
                    if(fewest[1] < rgb_real[1]):
                        fewest[1] = rgb_real[1]                    
                case "blue":
                    rgb_real[2] +=amount
                    if(fewest[2] < rgb_real[2]):
                        fewest[2] = rgb_real[2]
            
        all_draws.append(rgb_real)
    possible=True
    for set in all_draws:
        if(not check_possible(set,rgb_max)):
            possible=False
    
    if(possible):
        sum_ids += id

    all_fewest.append(fewest)
    
sum_power_fewest_sets = 0

for set in all_fewest:
    sum_power_fewest_sets += set[0]*set[1]*set[2]
    
print(sum_power_fewest_sets)
            



