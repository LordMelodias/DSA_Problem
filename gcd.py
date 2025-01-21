def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example
num1 = 56
num2 = 98
print(f"GCD of {num1} and {num2} is:", gcd(num1, num2))


'''
GCD (Greatest Common Divisor)
Definition: Finds the largest number that divides two numbers without leaving a remainder.
Objective: Simplify fractions or find common factors.
Diagram:
GCD(56, 98)
Step 1: 98 % 56 = 42
Step 2: 56 % 42 = 14
Step 3: 42 % 14 = 0 (GCD = 14)
'''