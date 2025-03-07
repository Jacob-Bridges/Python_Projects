# Example of adding, updating, and deleting items; Checking key membership

students = {'Fred': 95, 'Maria': 98, 'Bob': 82}
print(students)

students['Barb'] = 87
print(students)

students['Maria'] = 94
print(students)

del(students['Fred'])
print(students)

del(students['Ted'])
print(students)

if 'Ted' in students:
    del(students['Ted'])
else:
    print('Ted not in dictionary')
print(students)
