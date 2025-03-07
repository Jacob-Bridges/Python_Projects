def carb_counter(date):
    carbs = []
    print('This is the carbs function')
    print(f'I am tracking your carb intake for {date.strftime('%m/%d/%Y')}')

    for i in range(7):
        try:
            get_carbs = int(input('Enter your total carbs for today '))
            carbs.append(get_carbs)
            while 0 in carbs:
                carbs.remove(0)
                print('Oh no! did you mean to enter 0? Let\'s try again')
                get_carbs= int(input('Enter your total carbs for today '))
                carbs.append(get_carbs)
        except ValueError:
            print('Oh no! that wasn\'t a number baby!')
    print('Thanks! Time to calculate your total and average for the week! ILY Baby :)')
    print()
    return carbs