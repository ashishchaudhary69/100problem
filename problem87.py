s = input()
reversed_string = ""

for ch in s:
    reversed_string = ch + reversed_string

if s == reversed_string:
    print("Palindrome")
else:
    print("Not Palindrome")