from itertools import cycle
import re
import math
# Read the file
with open("Day8//input.txt", "r") as file:
    file_content = file.read()

# Split the content into lines
lines = file_content.split('\n')

# Extract directions from the first line
directions = lines[0]

# Initialize an empty dictionary to store key-value pairs
data_dict = {}

# Process the rest of the lines and populate the dictionary
for line in lines[1:]:
    if line.strip():  # Skip empty lines
        # Split each line into key and value
        key, value = map(str.strip, line.split('='))
        
        # Convert the value to a tuple
        value = tuple(map(str.strip, value.strip('()').split(',')))
        
        # Add the key-value pair to the dictionary
        data_dict[key] = value

goal = False
key = "AAA"
steps = 0
directions2 = directions

while not goal:
    (left, right) = data_dict[key]
    if directions2[0] == 'L':
        key = left
    else:
        key = right
    
    directions2 = directions2[1:] # Removes the chracter read

    if directions2 == '':
        directions2 = directions

    if key == 'ZZZ':
        goal = True
    steps += 1

print(f"Solution Part I: {steps}")

### Another solution

# with open('Day8//input.txt', 'r') as f:
#     puzzle_input = f.read()

# directions, connections = puzzle_input.split('\n\n')

# directions = cycle(0 if d == 'L' else 1 for d in directions)

# graph = {}
# regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
# for node, left, right in re.findall(regex, connections):
#     graph[node] = [left, right]

# node = 'AAA'
# for steps, d in enumerate(directions, start=1):
#     node = graph[node][d]
#     if node == 'ZZZ':
#         break

with open('Day8//input.txt', 'r') as f:
    puzzle_input = f.read()
directions, connections = puzzle_input.split('\n\n')
directions = [0 if d == 'L' else 1 for d in directions]
graph = {}
regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
for node, left, right in re.findall(regex, connections):
    graph[node] = [left, right]

starting_nodes = [node for node in graph if node[2] == 'A']

cycles = []
for node in starting_nodes:
    for steps, d in enumerate(cycle(directions), start=1):
        node = graph[node][d]
        if node[2] == 'Z':
            cycles.append(steps)
            break

print(f"Solution Part II: {math.lcm(*cycles)}")