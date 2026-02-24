def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Read input
a = int(input())
b = int(input())
c = int(input())

print(find_max(a, b, c))