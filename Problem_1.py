total_list = []
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total_list.append(i)
print(sum(total_list))