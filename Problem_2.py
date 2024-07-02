firstNum = 0
secondNum = 1
number = 0
total = 0
total_list = []

for i in range(32):
    number = firstNum + secondNum
    firstNum = secondNum
    secondNum = number
    total_list.append(number)

for num in total_list:
    if num % 2 == 0:
        total += num
print(total_list)
print(total)