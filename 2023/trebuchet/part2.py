from re import findall

number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

lines: list[str] = []
with open("input.txt") as file:
    lines = file.readlines()

digits: list[int] = []
for line in lines:
    numbers_in_line = [
        number_map[num] if num in number_map else num
        for num in findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line)
    ]

    if numbers_in_line:
        first_number = numbers_in_line[0]
        last_number = numbers_in_line[-1]

        digits.append(int(first_number + last_number))

print(sum(digits))
