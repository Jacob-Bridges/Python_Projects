# set comprehension example

s1 = {2, 3, 9, 8, 12}
print(s1)

# Example 1
s2 = set()
for num in s1:
    s2.add(num ** 2)
print(s2)

s2 = {num ** 2 for num in s1}
print(s2)

# Example 2
s2 = set()
for num in s1:
    if num < 9:  # Filter Condition
        s2.add(num ** 2)
print(s2)

s2 = {num**2 for num in s1 if num < 9}
print(s2)
