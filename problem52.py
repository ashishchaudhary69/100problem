def find_smallest(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

lst = list(map(int, input().split()))
print(find_smallest(lst))