def tuple_to_list(tup):
    return list(tup)

tup = tuple(map(int, input().split()))
print(tuple_to_list(tup))