import math
from functools import reduce

with open("input.txt", 'r') as file:
    content = file.read().splitlines()

Time = content[0].split(':')[1].split()
Distance = content[1].split(':')[1].split()

sum = [0] * len(Time)

for i in range(len(Time)):
    time_holding = list(range(int(Time[i]) + 1))
    for t in time_holding:
        if ((int(Time[i]) - t) * t) > int(Distance[i]):
            sum[i] += 1

# Use reduce to multiply all elements
product = reduce(lambda x, y: x * y, sum)

print(f"Solution Part I: {product}")

## Part II:

# Use the join method to concatenate the characters into a string
Time_part2 = ''.join(Time)
Distance_part2 = ''.join(Distance)


sum = 0
time_holding = list(range(int(Time_part2) + 1))
for t in time_holding:
    if ((int(Time_part2) - t) * t) > int(Distance_part2):
        sum += 1

print(f"Solution Part II: {sum}")