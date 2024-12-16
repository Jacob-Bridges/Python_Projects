# Dictionary methods

def main():
    students = {'Fred': 95, 'Maria': 98, 'Bob': 82, 'Barb': 87, 'Sarah': 78}
    print(students)

    grade = students.get('Hank', 'Not found')
    print(grade)

    grade = students.pop('Barb')  # Remove item and return value (can return KeyError)
    print(grade)
    print(students)


    students.popitem()
    print(students)

    students.clear()
    print(students)


main()
