import re

limits = [
    {"color": "red", "limit": "12"},
    {"color": "green", "limit": "13"},
    {"color": "blue", "limit": "14"},
]

with open("input.txt") as file:
    global games
    games = file.readlines()

passing_games = 0
for game in games:
    results = game.split(": ")[1].rstrip()
    subsets = re.split(r"[;,] ", results)
    pulls = (subset.split(" ") for subset in subsets)

    failed = False
    for pull in pulls:
        for limit in limits:
            if pull[1] == limit["color"] and int(pull[0]) > int(limit["limit"]):
                failed = True

    if not failed:
        passing_games += games.index(game) + 1

print(passing_games)
