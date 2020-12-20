
f = open("Puzzle2-sample.in")

spoken = []

for line in f:
    nums = line.strip('\n')

spoke = list(map(int,nums.split(',')))

spoken = {}
spokenBefore = -1
count = 1
new = True
for i in spoke:
        spoken[i] = [count]
        new = True
        count+=1
        spokenBefore = i

print(spoken)

while count < 30000001:
    if new:
        if 0 in spoken:
            spoken[0].append(count)
            new = False
        else:
            spoken[0] = [count]
            new = True
        spokenBefore = 0
    else:
        if spokenBefore >= 0:
            diff = spoken[spokenBefore][-1] - spoken[spokenBefore][-2]
            lastSpoke = diff
            if diff in spoken:
                new = False
                spokenBefore = diff
                spoken[diff].append(count)
            else:
                spoken[diff] = [count]
                spokenBefore = -1
                new = True
            
    count+=1

print(lastSpoke)