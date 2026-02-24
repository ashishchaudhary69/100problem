def rotate_list(lst, k):
    n = len(lst)
    k = k % n
    return lst[-k:] + lst[:-k]

lst = list(map(int, input().split()))
k = int(input())

print(*rotate_list(lst, k))