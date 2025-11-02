n = int(input("Enter the number: "))
p = int(input("Enter the power: "))

result = n
for i in range(1, p):
    result = result * n
print("\nResult =", result)