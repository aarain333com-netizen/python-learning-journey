# Tuple practice using plain logic (loops and if only)
# Written with AI help. Understand each line before uploading.

numbers = (12, 7, 25, 4, 18, 9)

# 1. Find the largest number
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest:", largest)

# 2. Find the smallest number
smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n
print("Smallest:", smallest)

# 3. Count even numbers
even_count = 0
for n in numbers:
    if n % 2 == 0:
        even_count += 1
print("Even numbers:", even_count)

# 4. Sum of all numbers
total = 0
for n in numbers:
    total += n
print("Sum:", total)

# 5. Reverse the tuple (tuples cannot change, so build a new one)
reversed_tuple = ()
for n in numbers:
    reversed_tuple = (n,) + reversed_tuple
print("Reversed:", reversed_tuple)

# 6. Search for a value
target = 25
found = False
for n in numbers:
    if n == target:
        found = True
if found:
    print(target, "is in the tuple")
else:
    print(target, "is not in the tuple")
