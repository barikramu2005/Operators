# ASSIGNMENT OPERATORS IN PYTHON
print("=== ASSIGNMENT OPERATORS ===\n")

# Simple Assignment (=)
name = "Python"
age = 25
score = 95.5

print("Simple Assignment:")
print(f"name = 'Python'  → name = {name}")
print(f"age = 25         → age = {age}")
print(f"score = 95.5     → score = {score}")

# Multiple Assignment
print("\nMultiple Assignment:")
x = y = z = 10
print(f"x = y = z = 10 → x={x}, y={y}, z={z}")

# Parallel Assignment
print("\nParallel Assignment:")
a, b, c = 5, 10, 15
print(f"a, b, c = 5, 10, 15 → a={a}, b={b}, c={c}")

# Swapping values using assignment
print("\nValue Swapping:")
p, q = 100, 200
print(f"Before: p={p}, q={q}")
p, q = q, p  # Swap values
print(f"After swap: p={p}, q={q}")

# Variable reassignment
print("\nVariable Reassignment:")
counter = 1
print(f"Initial: counter = {counter}")
counter = counter + 5
print(f"After counter = counter + 5: counter = {counter}")