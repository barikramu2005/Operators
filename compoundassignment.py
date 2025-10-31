# COMPOUND ASSIGNMENT OPERATORS IN PYTHON
print("=== COMPOUND ASSIGNMENT OPERATORS ===\n")

# Start with initial value
number = 20
print(f"Initial value: number = {number}\n")

# Addition assignment (+=)
number += 5
print(f"After number += 5:  number = {number}")

# Subtraction assignment (-=)
number -= 3
print(f"After number -= 3:  number = {number}")

# Multiplication assignment (*=)
number *= 2
print(f"After number *= 2:  number = {number}")

# Division assignment (/=)
number /= 4
print(f"After number /= 4:  number = {number}")

# Floor division assignment (//=)
number //= 2
print(f"After number //= 2: number = {number}")

# Modulus assignment (%=)
number %= 3
print(f"After number %= 3:  number = {number}")

# Exponentiation assignment (**=)
number **= 3
print(f"After number **= 3: number = {number}")

# String compound assignment
print("\n--- String Operations ---")
text = "Hello"
print(f"Initial text: '{text}'")
text += " World"
print(f"After text += ' World': '{text}'")

# List compound assignment
print("\n--- List Operations ---")
items = [1, 2, 3]
print(f"Initial list: {items}")
items += [4, 5]
print(f"After items += [4, 5]: {items}")