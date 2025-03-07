# len, acceptable keys and values, empty dicts

capitals = {'Virginia': 'Richmond',
            'North Carolina': 'Raleigh',
            'Florida': 'Tallahassee',
            'New Jersey': 'Trenton'}

size = len(capitals)
print(f'The dictionary has {size} items.')

# mixing key types

stuff = {3: "three",
         "apple": 8.9,
         (1, 2, 3): "That's a tuple!"}

print(stuff[3])
print(stuff[(1, 2, 3)])

stuff = {3: "three",
         "apple": 8.9,
         (1, 2, 3): "That's a tuple!",
         [1, 2, 3]: "This is illegal!!"}

# empty dicts

e1 = {}
e2 = dict()

print(e1)
print(e2)
