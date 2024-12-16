# Methods and operations with sets

s1 = {3, 4, 5, 6}
s2 = {5, 6, 7, 8}

s3 = s1.union(s2)
s3 = s1 | s2
print(s3)

s3 = s1.intersection(s2)
s3 = s1 & s2
print(s3)

s3 = s1.difference(s2)
s3 = s1 - s2
print(s3)

s3 = s1.symmetric_difference(s2)
s3 = s1 ^ s2
print(s3)

s1 = {2, 4}
s2 = {1, 2, 3, 4}

if s1.issubset(s2):
    print('s1 is a subset of s2.')

if s2.issuperset(s1):
    print('s2 is a superset of s1.')
