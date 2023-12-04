# Read the file and split it into lines
with open('input.txt', 'r') as file:
    content = file.read().splitlines()

# Initialize a list to store the separated lists of numbers
lists_of_numbers = []
winning_card = []

# Iterate through each line in the content
for line in content:
    # Split the line using "|" as a delimiter
    parts = line.split('|')
    first_number = parts[0].split(":")[1].strip()
    second_number = parts[1]
    # Split the strings into lists of integers and sort them
    list1_int = sorted([int(num) for num in first_number.split()])
    list2_int = sorted([int(num) for num in second_number.split()])
    winning_card.append(list1_int)    
    # Add the list of numbers to the result list
    lists_of_numbers.append(list2_int)

total_points = 0
for sublist1, sublist2 in zip(winning_card, lists_of_numbers):
    common_numbers = sorted(set(sublist1) & set(sublist2))
    if len(common_numbers) == 0:
        total_points += 0
    else:
        total_points += 2**(len(common_numbers)-1)

print(f"Answer Part I: {total_points}")

## Part 2
f = open("input.txt").readlines()

s = 0
cards = [1 for _ in f]

for index, line in enumerate(f):
    line = line.split(":")[1]
    a, b = line.split("|")
    a, b = a.split(), b.split()

    n = len(set(a) & set(b))

    if n > 0:
        s += 2 ** (n - 1)

    for i in range(n):
        cards[index + i + 1] += cards[index]

print(f"Answer Part II: {sum(cards)}")