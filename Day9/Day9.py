import numpy as np
with open("Day9//input.txt", "r") as file:
# with open("input.txt", "r") as file:
    file_content = file.read()

# Split the content into lines
lines = file_content.split('\n')
result = 0
for line in lines:
    aux = []
    aux2 = []
    # Split the string into a list of substrings
    numbers_list_str = line.split()

    # Convert each substring to an integer
    numbers_list = [int(num) for num in numbers_list_str]
    aux.append(numbers_list)
    v = [1]
    while sum(v) != 0:
        v = list(np.diff(numbers_list))
        aux.append(v)
        numbers_list = v

    value = 0
    for i in range(len(aux) - 1, -1, -1):
        value += aux[i][-1] 
        aux2 = [value] + aux2

    result += aux2[0]

print(f"Solution Part I: {result}")

result = 0
for line in lines:
    aux = []
    aux2 = []
    # Split the string into a list of substrings
    numbers_list_str = line.split()

    # Convert each substring to an integer
    numbers_list = [int(num) for num in numbers_list_str]
    aux.append(numbers_list)
    v = [1]
    while sum(v) != 0:
        v = list(np.diff(numbers_list))
        aux.append(v)
        numbers_list = v

    value = 0
    for i in range(len(aux) - 1, -1, -1):
        value = aux[i-1][0] - value 
        aux2 = [value] + aux2

    result += aux2[1]

print(f"Solution Part II: {result}")