
import itertools

vals=[]
f = open("Puzzle1.in")
for line in f:
    vals.append(int(line.strip('\n')))

print(vals)

for x,y in itertools.combinations(vals, 2):
    print(x,y)
    print(x+y)
    if x+y == 2020:
        print(x*y)
        quit()