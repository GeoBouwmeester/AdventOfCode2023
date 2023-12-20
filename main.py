with open("input.txt") as file:
    data = []
    for line in file.readlines():
        item = []
        for character in line:
            if character >= '0' and character <= '9':
                item.append(int(character))
        data.append(item)

total = 0 
for item in data:
    total += (10 * item[0])
    total += item[-1]

print("Part 1 solution: ", total) 