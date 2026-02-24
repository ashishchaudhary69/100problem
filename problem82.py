n = int(input())
d = {}

for _ in range(n):
    key = input()
    value = int(input())
    d[key] = value

remove_key = input()

d.pop(remove_key, None)

for key in d:
    print(key, d[key])