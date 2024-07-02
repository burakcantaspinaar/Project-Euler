total = 0
total_list = []
i = 1
result_list = {}

while i < 42000:
    total += i
    i += 1
    total_list.append(total)

for coefficient in total_list:
    if coefficient not in result_list:
        result_list[coefficient] = []
    for j in range(1, int(coefficient**0.5) + 1):
        if coefficient % j == 0:
            result_list[coefficient].append(j)
            if j != coefficient // j:
                result_list[coefficient].append(coefficient // j)

for key, value in result_list.items():
    if len(value) > 500:
        print(f"{key} sayısının {len(value)} çarpanı var.")
        break