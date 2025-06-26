# Task 1: Check if the number is positive, negative, or zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
# Task 2: Multiplication Table from 1 to 10
num = int(input("Enter a number: "))
print(f"Multiplication table for {num}:")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
  # Task 3: Fibonacci series up to N terms
n = int(input("How many Fibonacci terms? "))

a, b = 0, 1
count = 0

while count < n:
    print(a)
    a, b = b, a + b
    count += 1
