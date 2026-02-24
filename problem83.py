n = int(input())
d = {}

for _ in range(n):
    key = input()
    value = int(input())
    d[key] = value

search_key = input()

if search_key in d:
    print("Key exists")
else:
    print("Key does not exist")