def list_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

lst = list(map(int, input().split()))
print(list_sum(lst))