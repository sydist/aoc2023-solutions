from re import split
from functools import reduce

with open("input.txt") as file:
    global games
    games = file.readlines()

sums = 0
for game in games:
    results = game.split(": ")[1].rstrip()
    subsets = split(r"[;,] ", results)
    pulls = (subset.split(" ") for subset in subsets)

    smallest_possible_size = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }

    for pull in pulls:
        number = int(pull[0])
        current_number = smallest_possible_size[pull[1]]
        if number > current_number:
            smallest_possible_size[pull[1]] = number

    sums += reduce(lambda x, y: x * y, smallest_possible_size.values())


print(sums)
