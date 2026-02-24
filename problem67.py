def min_in_tuple(tup):
    minimum = tup[0]
    for num in tup:
        if num < minimum:
            minimum = num
    return minimum

tup = tuple(map(int, input().split()))
print(min_in_tuple(tup))