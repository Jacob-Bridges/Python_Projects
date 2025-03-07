def protein_counter(date):
    protein =[]
    print('This is the protein function')
    print(f'I am tracking your protein intake for {date.strftime('%m/%d/%Y')}')

    for i in range(7):
        try:
            get_protein = int(input('Enter your total protein for today '))
            protein.append(get_protein)
            while 0 in protein:
                protein.remove(0)
                print('Oh no! did you mean to enter 0? Let\'s try again')
                get_protein = int(input('Enter your total protein for today '))
                protein.append(get_protein)
        except ValueError:
            print('Oh no! that wasn\'t a number baby!')
    return protein