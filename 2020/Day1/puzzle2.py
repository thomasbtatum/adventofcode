
import itertools

vals=[]
f = open("Puzzle1.in")
for line in f:
    vals.append(int(line.strip('\n')))

print(vals)

for x,y,z in itertools.combinations(vals, 3):
    print(x,y,z)
    print(x+y+z)
    if x+y+z == 2020:
        print(x*y*z)
        quit()