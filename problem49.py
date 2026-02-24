def unique_elements(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    return unique

lst = list(map(int, input().split()))
result = unique_elements(lst)
print(*result)