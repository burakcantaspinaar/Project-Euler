multiply = 1
result = 0
for n in range(100, 0, -1):
    multiply = multiply * n

str_multiply = str(multiply)

for add in str_multiply:
    result += int(add)
print(result)
