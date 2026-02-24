# read inputs
P = float(input())
R = float(input())
T = float(input())

# calculate compound interest
CI = (P * (1 + R / 100), **T) - P

# print result 
print("compound interest is:", CI)