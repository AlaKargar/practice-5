num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 < num2:
    min = num1
else:
    min = num2

gcd = 1
for i in range(1, min+1):
    if (num1 % i == 0) and (num2 % i == 0):
        gcd = i

print("The greatest common divisor of", num1, num2, "is:", gcd)
