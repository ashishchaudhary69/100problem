def reverse_list(lst):
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]
    return lst

lst = list(map(int, input().split()))
print(*reverse_list(lst))