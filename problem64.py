def replace_negative(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = 0
    return lst

lst = list(map(int, input().split()))
print(*replace_negative(lst))