n1 = int(input())
dict1 = {}
for _ in range(n1):
    key = input()
    value = int(input())
    dict1[key] = value

n2 = int(input())
dict2 = {}
for _ in range(n2):
    key = input()
    value = int(input())
    dict2[key] = value

# Manual merge
merged = {}
for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    merged[key] = dict2[key]

for key in merged:
    print(key, merged[key])