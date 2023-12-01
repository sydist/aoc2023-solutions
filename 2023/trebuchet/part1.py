lines: list[str] = []
with open("input.txt") as file:
    lines = file.readlines()

digits: list[int] = []
for line in lines:
    numbers_in_line = [letter for letter in line if letter.isdigit()]

    if numbers_in_line:
        first_number = numbers_in_line[0]
        last_number = numbers_in_line[-1]
        digits.append(int(first_number + last_number))

print(sum(digits))
