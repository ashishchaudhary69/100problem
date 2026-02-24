n = int(input())
d = {}

for _ in range(n):
    key = input()
    value = int(input())
    d[key] = value

for key in sorted(d.keys()):
    print(key, d[key])