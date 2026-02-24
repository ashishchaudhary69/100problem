def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in s:
        if ch in vowels:
            count += 1
    return count

s = input()
print(count_vowels(s))