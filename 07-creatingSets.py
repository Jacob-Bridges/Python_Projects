# Example of creating sets and retrieving values

# Two ways to define sets
s1 = set([2, 3, 5, 4, 7])
print(s1)

s1 = {2, 3, 9, 8, 12}
print(s1)

# Removing duplicates from a list
numbers = [1, 2, 2, 2, 3, 4, 3, 4, 3, 4]
number_set = set(numbers)
print(number_set)
numbers = list(number_set)
print(numbers)

# strings in sets
s1 = set('Hello')
print(s1)

s1 = {2, 3, 4, 8, 9}
print(s1)
s1.add(7)   # Adds a single element to a set
s1.update([3, 6, 9, 12])   # Adds multiple elements to a set
s1.remove(4)
s1.remove(10)  # Error!!  This method can produce KeyError
if 10 in s1:
    s1.remove(10)
s1.discard(10)  # This method will ignore missing key

for member in s1:
    print(member)


