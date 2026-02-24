def max_in_tuple(tup):
    maximum = tup[0]
    for num in tup:
        if num > maximum:
            maximum = num
    return maximum

tup = tuple(map(int, input().split()))
print(max_in_tuple(tup))