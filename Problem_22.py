with open("0022_names.txt", "r") as file:
    content = file.read()

names = content.replace('"', '').split(",")
names = [name.upper() for name in names]
names.sort()

alphabet = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
    'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

total_list = []
for name in names:
    total = sum(alphabet[char] for char in name if char in alphabet)
    total_list.append(total)

new_list = list(range(1, len(total_list) + 1))

result_list = [total * position for total, position in zip(total_list, new_list)]

result = sum(result_list)
print(result)
