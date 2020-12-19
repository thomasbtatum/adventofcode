
f = open("Puzzle1.in")

spoken = []

for line in f:
    nums = line.strip('\n')

spoken = list(map(int,nums.split(',')))

print(spoken)

while len(spoken) < 2021:
    lastSpoken = spoken[-1]
    countLastSpoken = spoken.count(lastSpoken)
    if countLastSpoken == 1:
        spoken.append(0)
    else:
        for back in range(len(spoken)-2,-1,-1):
            if(spoken[back] == lastSpoken):
                diff = (len(spoken)-1) - back
                spoken.append(diff)
                break

print(spoken[2019])