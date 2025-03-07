def calorie_counter(date):
    calorie = []
    print('This is the calorie function.')
    week = 7

    for i in range(week):
        try:
            get_calories = int(input('Enter your calories for last week.'))
            calorie.append(get_calories)
            while 0 in calorie:
                calorie.remove(0)
                print('Oh no! did you mean to enter 0? Let\'s try again')
                get_calories = int(input('Enter your calories for last week.'))
                calorie.append(get_calories)
        except ValueError:
            print('Oh no! that wasn\'t a number baby!')
    return calorie