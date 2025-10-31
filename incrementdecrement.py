# INCREMENT AND DECREMENT IN PYTHON
print("=== INCREMENT & DECREMENT ===\n")

# Python doesn't have ++ and -- operators
# We use += and -= instead

# Increment examples
counter = 5
print(f"Initial value: counter = {counter}")

# Increment by 1
counter += 1
print(f"After counter += 1: counter = {counter}")

# Increment by other values
counter += 3
print(f"After counter += 3: counter = {counter}")

# Decrement examples
countdown = 10
print(f"\nInitial value: countdown = {countdown}")

# Decrement by 1
countdown -= 1
print(f"After countdown -= 1: countdown = {countdown}")

# Decrement by other values
countdown -= 2
print(f"After countdown -= 2: countdown = {countdown}")

# Practical examples
print("\n--- Practical Examples ---")

# Loop with increment
print("Counting up:")
number = 1
while number <= 5:
    print(f"  Number: {number}")
    number += 1  # Increment

# Loop with decrement
print("\nCounting down:")
timer = 3
while timer > 0:
    print(f"  Time: {timer}")
    timer -= 1  # Decrement
print("  Go!")

# Multiple increments
print("\n--- Multiple Operations ---")
value = 10
print(f"Start: value = {value}")
value += 2  # Increment by 2
print(f"After += 2: value = {value}")
value -= 5  # Decrement by 5
print(f"After -= 5: value = {value}")