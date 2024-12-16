# Dealing with table data

# Grade data using list as dictionary value
grades = {'Fred': [95, 100, 83],
          'Maria': [98, 93, 95],
          'Bob': [82, 78, 75]}

print(grades['Fred'])    # Get all of Fred's grades
print(grades['Maria'][1])  # Get Maria's second test grade

# Get the average grade for all the students
for key, value in grades.items():
    avg = sum(value)/len(value)
    print(f'{key}, Avg: {avg:.1f}')

