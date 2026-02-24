def count_frequency(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

lst = list(map(int, input().split()))
result = count_frequency(lst)
for key in result:
    print(key, result[key])