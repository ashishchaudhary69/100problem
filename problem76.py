n = int(input())
students = {}

for _ in range(n):
    name = input()
    marks = int(input())
    students[name] = marks

topper = max(students, key=students.get)
print(topper)