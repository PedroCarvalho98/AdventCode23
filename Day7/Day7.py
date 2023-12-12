# def custom_sort(item):
#     # Define the order of characters
#     order = "AKQJT98765432"
    
#     # Define a function to get the value of a character
#     def get_char_value(char):
#         return order.index(char)
    
#     # Define a key function for sorting
#     def key_function(entry):
#         cards, _ = entry
#         return [get_char_value(card_char) for card_char in cards]
    
#     # Sort the list using the custom key function
#     sorted_list = sorted(item, key=key_function, reverse=False)
    
#     return sorted_list

# def custom_sort2(item):
#     # Define the order of characters
#     order = "AKQT98765432J"
    
#     # Define a function to get the value of a character
#     def get_char_value(char):
#         return order.index(char)
    
#     # Define a key function for sorting
#     def key_function(entry):
#         cards, _ = entry
#         return [get_char_value(card_char) for card_char in cards]
    
#     # Sort the list using the custom key function
#     sorted_list = sorted(item, key=key_function, reverse=False)
    
#     return sorted_list

# def max_repeated_chars(t):
#     # Helper function to calculate the maximum number of repeated characters
#     # and check if there are 2 other characters that repeat
#     s, _ = t
#     counts = {char: s.count(char) for char in set(s)}
#     max_count = max(counts.values())
#     other_chars_repeat = sum(count == 2 for count in counts.values())
#     return (max_count, other_chars_repeat)

# def max_repeated_chars2(t):
#     # Helper function to calculate the maximum number of repeated characters
#     # and check if there are 2 other characters that repeat
#     s, _ = t
#     counts = {char: s.count(char) for char in set(s)}
#     counts2 = {char: s.count(char) for char in set(s)}
#     # Find the key with the maximum value
#     max_key = max(counts, key=counts.get)
#     if 'J' in counts2:
#         # Check if 'J' is the only key in the dictionary
#         if len(counts2) != 1:
#             counts2[max_key] += counts2['J']
#             del counts2['J']  # Remove the 'J' key

#     max_count = max(counts2.values())
#     other_chars_repeat = sum(count == 2 for count in counts2.values())


#     return (max_count, other_chars_repeat)

# def sort_by_max_repeated_chars(tuple_list):
#     # Sort the list of tuples based on the specified criteria
#     return sorted(tuple_list, key=max_repeated_chars, reverse=True)

# def sort_by_max_repeated_chars2(tuple_list):
#     # Sort the list of tuples based on the specified criteria
#     return sorted(tuple_list, key=max_repeated_chars2, reverse=True)

# with open("Day7//input.txt", 'r') as file:
#     content = file.read().splitlines()

# hands_and_bids = []
# for line in content:
#     hand, bid = line.split()
#     hands_and_bids.append((hand, int(bid)))

# # Sort the list using the custom sorting function
# sorted_list = custom_sort(hands_and_bids)
# sorted_list2 = custom_sort2(hands_and_bids)

# sorted_list_of_tuples = sort_by_max_repeated_chars(sorted_list)
# sorted_list_of_tuples2 = sort_by_max_repeated_chars2(sorted_list2)

# print(sorted_list_of_tuples2)

# sum = 0
# i = 0
# for _, bid in sorted_list_of_tuples:
#     sum += (len(sorted_list_of_tuples) - i) * bid
#     i += 1

# print(f"Solution Part I: {sum}")

# sum = 0
# i = 0
# for _, bid in sorted_list_of_tuples2:
#     sum += (len(sorted_list_of_tuples2) - i) * bid
#     i += 1

# print(f"Solution Part II: {sum}")
from collections import Counter

def hand_type(hand):
    c = Counter(hand)
    counts = [0] if (jokers := c.pop("*", 0)) == 5 else sorted(c.values())
    # The most efficient use of a joker is always as the most common non-joker card
    counts[-1] += jokers
    match counts:
        case *_, 5:
            return 7
        case *_, 4:
            return 6
        case *_, 2, 3:
            return 5
        case *_, 3:
            return 4
        case *_, 2, 2:
            return 3
        case *_, 2:
            return 2
    return 1


def solve(data):
    ws = [l.split() for l in data.split("\n")]
    return sum(
        rank * bid
        for rank, (*_, bid) in enumerate(
            sorted(
                (hand_type(hand), *map("*23456789TJQKA".index, hand), int(bid))
                for hand, bid in ws
            ),
            1,
        )
    )

with open("Day7//input.txt") as f:
    data = f.read().strip()
print(solve(data.replace("J", "*")))