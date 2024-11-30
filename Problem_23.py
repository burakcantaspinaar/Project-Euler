numbers = list(range(1, 28123))
numbers_set = set(numbers)


def sum_of_divisors(n):
    divisor_sum = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != 1 and i != n // i:
                divisor_sum += n // i
    return divisor_sum


divisor_sums = []
for num in numbers:
    divisor_sums.append(sum_of_divisors(num))

abundant_numbers = []
for index, value in enumerate(divisor_sums):
    if value > numbers[index]:
        abundant_numbers.append(numbers[index])

abundant_numbers_set = set(abundant_numbers)
abundant_sums = set()

for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        abundant_sum = abundant_numbers[i] + abundant_numbers[j]
        if abundant_sum < 28123:
            abundant_sums.add(abundant_sum)

last_result = numbers_set - abundant_sums

answer = sum(last_result)
print(answer)
