n = int(input())

i = 1
sum_even = 0

while i <= n:
    if i % 2 == 0:
        sum_even += i
    i += 1

print(sum_even)