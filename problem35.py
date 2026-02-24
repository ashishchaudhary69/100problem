# Read input
s = input()

# Initialize counter
count = 0

# Check each character
for ch in s:
    if ch.lower() in 'aeiou':
        count += 1

# Print result
print(count)