def separate_even_odd(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

lst = list(map(int, input().split()))
even, odd = separate_even_odd(lst)

print("Even:", *even)
print("Odd:", *odd)