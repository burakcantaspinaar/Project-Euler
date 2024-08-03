from num2words import num2words

total_value = ""

for i in range(1, 1001):
    value = num2words(i)
    total_value += value

total_value = total_value.replace(" ", "")
total_value = total_value.replace("-", "")

print("Result value =", len(total_value))
