current, next_val = 1, 0
index = 0

while True:
    fib_number = current + next_val
    current, next_val = next_val, fib_number
    index += 1
    if len(str(fib_number)) == 1000:
        print(index)
        break
