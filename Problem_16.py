value = 2 ** 1000
value_str = str(value)

result = 0

for i in value_str:
    result += int(i)

print("Result =", result)
