# Read the file and split it into lines
with open('Day2//input.txt', 'r') as file:
    content = file.read()

# Split the content into lines
lines = content.split('\n')

max_num_red = 12
max_num_green = 13
max_num_blue = 14

sum_of_ids = 0
ids = []
# Iterate through each line
for line in lines:
    # Split the line based on the colon (:) to separate the key and value
    parts = line.split(':')
    # Extract the game number from the key
    game_number = int(parts[0].split()[1])
    ids.append(game_number)
    # Extract the values from the second part, split by semicolon (;)
    values_list = parts[1].split(';')
    
    flag = False
    for value in values_list:
        # Split the string by comma (,), extract the numeric part, and check for the color
        parts = [part.strip() for part in value.split(',') if part.strip()]
        # Split the string by comma (,), extract the numeric part, and check for the color
        for part in parts:
            count, color = part.split(' ')
            count = int(count)
            # Update maximum counts based on the color
            if (color == 'red' and count > max_num_red) or (color == 'blue' and count > max_num_blue) or (color == 'green' and count > max_num_green):
                ids.remove(game_number)
                flag = True
                break
        if flag:
            break
# Print the resulting impossible iterations
print(f"Answer of Part I: {sum(ids)}")

## Part 2

power = []
# Iterate through each line
for line in lines:
    # Split the line based on the colon (:) to separate the key and value
    parts = line.split(':')
    # Extract the game number from the key
    game_number = int(parts[0].split()[1])
    # Extract the values from the second part, split by semicolon (;)
    values_list = parts[1].split(';')
    
    # Initialize variables to store maximum counts
    max_red = 0
    max_blue = 0
    max_green = 0
    for value in values_list:
        # Split the string by comma (,), extract the numeric part, and check for the color
        parts = [part.strip() for part in value.split(',') if part.strip()]
        # Split the string by comma (,), extract the numeric part, and check for the color
        for part in parts:
            count, color = part.split(' ')
            count = int(count)
            # Update maximum counts based on the color
            if color == 'red':
                max_red = max(max_red, count)
            elif color == 'blue':
                max_blue = max(max_blue, count)
            elif color == 'green':
                max_green = max(max_green, count)

    power.append(max_blue*max_green*max_red)

# Print the resulting impossible iterations
print(f"Answer of Part II: {sum(power)}")