total_list = []
number = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        number = i * j
        if str(number) == str(number)[::-1]:
            total_list.append(number)
print(max(total_list))