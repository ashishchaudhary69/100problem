def remove_duplicates(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result

lst = list(map(int, input().split()))
print(*remove_duplicates(lst))