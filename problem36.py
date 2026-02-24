# Read input
n = int(input())

# Print divisors
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")