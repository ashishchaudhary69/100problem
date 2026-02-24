def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Read input
n = int(input())

# Call function
fibonacci(n)