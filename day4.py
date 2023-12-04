file = open('inputs/day4_sample.txt', 'r')
#file = open('inputs/day3.txt', 'r')
lines = file.read().split('\n')

def get_winning_numbers_and_cards():
    winning_numbers_and_cards = []
    for line in lines:
        
        winning=[i for i in line[9:].split(" | ")[0].split(" ") if i]
        scratchcard=[i for i in line[9:].split(" | ")[1].split(" ") if i]
        card = line.split(": ")[0].split("Card ")[1]
     
        winning_numbers_and_cards.append([winning,scratchcard,card])
    return winning_numbers_and_cards


def calculate_points(winning_numbers,scratchcard):
    print("----------")
    score=0
    for number in scratchcard:
        if(number in winning_numbers):
            print(number, " is in winnings!")
            if(score==0):
                score += 1
            else:
                score *= 2
                
    return score
def calculate_copies(cardnumber,winning_numbers,scratchcard):
    score=0
    copies=[]
    hand=[]
    for number in scratchcard:
        if(number in winning_numbers):
            score+=1
    for i in range(0,score):
        copies.append(cardnumber+1+i)

    print(copies)
    for copy in copies:
        numbers = get_winning_numbers_and_cards()[copy-1][1]
        for number in numbers:
            hand.append(number)
    return hand


winning_numbers_and_cards = get_winning_numbers_and_cards()

total_score = 0
for row in winning_numbers_and_cards:
    total_score += calculate_points(row[0],row[1])
print("part 1: ", total_score)


print(calculate_copies(2,winning_numbers_and_cards[0][0],winning_numbers_and_cards[0][1]))











