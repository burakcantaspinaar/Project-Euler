from math import factorial

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_result = []
mod_number = 999999

for i in range(9, -1, -1):
    group_factorial = factorial(i)
    selected_number = mod_number // group_factorial
    mod_number %= group_factorial
    my_result.append(numbers.pop(selected_number))

result_number = int(''.join(str(digit) for digit in my_result))
print(result_number)
