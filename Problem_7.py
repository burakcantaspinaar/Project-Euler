total_list = []
for i in range(2, 200000):
    is_prime = True
    for j in range(2, 200000):
        if i % j == 0 and i != j:
            is_prime = False
            break
    if is_prime and i not in total_list:
        total_list.append(i)
print(len(total_list))
print(total_list[10000])