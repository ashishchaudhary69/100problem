def count_occurrence(tup, element):
    count = 0
    for num in tup:
        if num == element:
            count += 1
    return count

tup = tuple(map(int, input().split()))
element = int(input())
print(count_occurrence(tup, element))