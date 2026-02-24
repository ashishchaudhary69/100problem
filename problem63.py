def list_average(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

lst = list(map(int, input().split()))
print(list_average(lst))