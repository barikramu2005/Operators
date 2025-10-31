# LOGICAL OPERATORS IN PYTHON
print("=== LOGICAL OPERATORS ===\n")

# Initialize boolean variables
a = True
b = False

print(f"a = {a}, b = {b}\n")

# Logical AND
print(f"AND: {a} and {b} → {a and b}")
print(f"AND: {a} and {a} → {a and a}")

# Logical OR
print(f"OR: {a} or {b} → {a or b}")
print(f"OR: {b} or {b} → {b or b}")

# Logical NOT
print(f"NOT: not {a} → {not a}")
print(f"NOT: not {b} → {not b}")

# Practical examples with conditions
print("\n--- Practical Examples ---")
age = 20
has_license = True

print(f"Age: {age}, Has License: {has_license}")
print(f"Can drive? {age >= 18 and has_license}")

score = 85
print(f"Score: {score}, Is distinction? {score >= 80 or score <= 100}")