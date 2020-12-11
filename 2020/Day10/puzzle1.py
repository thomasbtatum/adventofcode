f = open("Puzzle1.in")

numbers = []
for line in f:
    numbers.append(int(line.strip('\n')))

numbers.append(0)
numbers.append(max(numbers)+3)
print(numbers)
numbers.sort()
print(numbers)

idx = 0
count = {1:0, 3:0}
while idx < len(numbers)-1:
    result = numbers[idx+1] - numbers[idx]
    count[result]+=1
    idx+=1

print(count)
print(count[1]*count[3])