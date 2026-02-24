def common_elements(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2 and num not in result:
            result.append(num)
    return result

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

print(*common_elements(lst1, lst2))