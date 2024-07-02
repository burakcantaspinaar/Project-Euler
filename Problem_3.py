total_list = []
userNumber = int(input("Enter a number: "))
for i in range(2, 100000):
    if userNumber % i == 0:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime and i not in total_list and i != userNumber:
           total_list.append(i)
print(total_list)
print(max(total_list))