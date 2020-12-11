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

#Dynamic Programming credit goes to: Jonathan Paulson! - https://www.youtube.com/watch?v=cE88K2kFZn0
DP = {}
def dp(i):
    if i==len(numbers)-1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(numbers)):
        if numbers[j]-numbers[i] <= 3:
            ans += dp(j)
    DP[i] = ans
    return ans

print(dp(0))