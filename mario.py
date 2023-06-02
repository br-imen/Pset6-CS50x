from cs50 import get_int

# A while loop to get_int
while True:
    n = get_int('height: ')
    if n in range(1, 9):
        break

# A loop in a reversed range to print the pyramid
for j in reversed(range(0, n)):
    print(' '*j + '#'*(n-j), end='')
    print()