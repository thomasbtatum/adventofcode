f = open("Puzzle1-sample.in")
rules = {}
for line in f:
    k,v = line.strip('\n').split(" contain ")
    rules[k] = v

print(rules)