# Example of creating dictionaries and retrieving values

# Example 1
students = {'Fred': 95, 'Maria': 98, 'Bob': 82}

print(students['Maria'])

# Example 2
capitals = {'Virginia': 'Richmond',
            'North Carolina': 'Raleigh',
            'Florida': 'Tallahassee',
            'New Jersey': 'Trenton'}

print(capitals['Virginia'])
print(capitals['Ohio'])  # KeyError!

state = input('Enter a state: ')
if state in capitals:
    print(capitals[state])
else:
    print(f'{state} not in dictionary.')

# Example 3
temperatures = {'Monday': 88.2,
                'Tuesday': 79.1,
                'Wednesday': 83.5,
                'Thursday': 92.4,
                'Friday': 76.8,
                'Saturday': 74.0,
                'Sunday': 80.3}
