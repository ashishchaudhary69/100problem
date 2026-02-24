def is_palindrome(lst):
    return lst == lst[::-1]

lst = list(map(int, input().split()))

if is_palindrome(lst):
    print("Palindrome")
else:
    print("Not Palindrome")