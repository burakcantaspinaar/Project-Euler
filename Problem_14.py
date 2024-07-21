max_length = 0
starting_number = 0

for i in range(1, 1000000):

    length = 1
    n = i

    while n != 1:

        if n % 2 == 0:
            n = n//2

        else:
            n = 3*n+1

        length += 1

    if length > max_length:
        max_length = length
        starting_number = i

print("Starting number:", starting_number, "and its length", max_length)