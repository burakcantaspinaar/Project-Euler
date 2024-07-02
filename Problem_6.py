number1 = 0
number2 = 0
for i in range (1,101):
    number1 += i**2
print(number1)
for i in range (1,101):
    number2 += i
number2 = number2**2
print(number2)
print('Answer:', number2-number1)