file1 = open('inputs/day1.txt', 'r')

lines = file1.read().split('\n')

def get_first(list):
    for char in list:
        if(char.isdigit()):
            return char
    return '0'
    
word_to_num ={
  "one": "o1e",
  "two": "t2o",
  "three": "thr3e",
  "four": "fo4ur",
  "five": "fi5ve",
  "six": "s6x",
  "seven": "se7ven",
  "eight": "eig8ht",
  "nine": "n9ine"
}

newlines=[]
for line in lines:
    for key in word_to_num.keys():
        line = line.replace(key,word_to_num[key])
    newlines.append(line)
#evaluate list with pure numbers
sum_1=0
all_nums=[]

for line in newlines:
    nums = [char for char in line if char.isdigit()]
    all_nums.append(eval(get_first(nums)+get_first(reversed(nums))))

print(all_nums)
#print(newlines)
print("part2: ",sum(all_nums))




