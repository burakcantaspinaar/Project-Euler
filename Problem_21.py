total_list = []
new_list = {}
result_list = {}

for i in range(1, 10000):
    total_list = []
    for j in range(1, i):
        if i % j == 0:
            total_list.append(j)
    new_list[i] = total_list

for key, value in new_list.items():
    result_list[key] = sum(value)

amicable_numbers = []
for key, value in result_list.items():
    if value in result_list and result_list[value] == key and key != value:
        amicable_numbers.append((key, value))

unique_sums = set(sum(pair) for pair in amicable_numbers)
final_result = sum(unique_sums)

print("Amicable Numbers:", amicable_numbers)
print("Final Result:", final_result)
