total_list = []
number = 0
for i in range(2, 2000001):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0 and i != j:
            is_prime = False
            break
    if is_prime and i not in total_list:
        total_list.append(i)
print(total_list)
print(max(total_list))
for i in total_list:
    number += i
print(number)