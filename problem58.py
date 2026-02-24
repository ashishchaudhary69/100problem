def merge_remove_duplicates(lst1, lst2):
    merged = lst1 + lst2
    result = []
    for num in merged:
        if num not in result:
            result.append(num)
    return result

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
print(*merge_remove_duplicates(lst1, lst2))