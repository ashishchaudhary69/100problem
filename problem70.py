def is_unique(tup):
    return len(tup) == len(set(tup))

tup = tuple(map(int, input().split()))

if is_unique(tup):
    print("Unique")
else:
    print("Not Unique")