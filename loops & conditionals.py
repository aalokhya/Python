# 1. Loops & Conditionals
'''
# Print all even,odd numbers from 1 to N
n = int(input())

print("even list")
for i in range(1,n+1):
    if i % 2 == 0:
        print(i)
        
print("odd list")
for i in range(1,n+1):
    if i % 2 != 0:
        print(i)


# Check if a number is prime
n = int(input())

for num in range(2, n + 1):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")


n = int(input())

if n == 0 or n == 1:
    print("Not Prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


# Find factorial of a number

n = int(input())
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)



# Sum of first N natural numbers
n = int(input())
sum = 0
for i in range(n+1):
    sum += i
print(sum)


# Print multiplication table of a number
n = int(input())

for i in range(1,11):
    mul = n * i
    print(mul)

n = int(input())
for i in range(1, n + 1):          # Outer loop → which table
    print(f"Multiplication table of {i}:")
    for i in range(1,21):
        print(n, "x", i, "=", n * i)

'''
# Print Fibonacci sequence iteratively

n = int(input(" "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Find GCD of two numbers

a = int(input(" "))
b = int(input(" "))

while b != 0:
    a, b = b, a % b

print("GCD is", a)


# Find LCM of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = a
temp = b
while temp != 0:
    gcd, temp = temp, gcd % temp

lcm = (a * b) // gcd
print("LCM is", lcm)


# Print pattern (like triangle of stars)
'''
n = 5
for i in range(1,n+1):
    for j in range(i):
        print("*", end = " ")
    print()
'''
