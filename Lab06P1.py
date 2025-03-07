#
# Jacob Bridges
# 2/15/24
# Test Score calculation program


# Global Named Constant to calculate extra credit
EXTRA_CREDIT = 1.05


def main():
    a_list, b_list, c_list = get_test_scores()
    all_scores = [a_list[:], b_list[:], c_list[:]]

    print(f'All Scores: {all_scores}')
    calc_extra_credit(all_scores)
    print(f'All scores after extra credit: {all_scores}')
    score_spreads = get_score_spread (all_scores)
    print(f'Score spreads: {score_spreads}\n')

    # Step G
    print('Original Scores')
    print(f'Ashley\'s scores: {a_list}')
    print(f'Barb\'s scores:{b_list}')
    print(f'Carl\'s scores: {c_list}')


def get_test_scores():
    ashley = []
    barb = []
    carl = []
    # Step A
    print('Please enter Ashley\'s scores one by one.')
    for i in range(3):
        element = int(input('Enter a score: '))
        ashley.append(element)
    print(f'Ashley\'s scores: {ashley} \n')
    # Step B
    print('Please enter Barb\'s scores one by one.')
    for i in range(5):
        element = int(input('Enter a score: '))
        barb.append(element)
    print(f'Barb\'s scores: {barb} \n')
    # Step C
    print('Please enter Carl\'s scores one by one.')
    for i in range(4):
        element = int(input('Enter a score: '))
        carl.append(element)
    print(f'Carl\'s scores: {carl} \n')

    # Step D
    return ashley, barb, carl


def calc_extra_credit(scores):
    # Step E
    # for each element in all_scores, multiply each subelement by EXTRA_CREDIT
    # Can't figure out how to round each subelement to the nearest whole number
    for element in range(len(scores)):
        for subelement in range(len(scores[element])):
            scores[element][int(subelement)] *= EXTRA_CREDIT




def get_score_spread(scores):
    # Step F
    min_list = []
    max_list = []
    spread_list = []
    # for each element in the all scores list, assign the smallest value to the min list
    # for each element in the all scores list, assign the highest value to the max list
    # Subtract the max value and the min value, and append that to the spread list
    for element in range(len(scores)):
        min_list.append(min(scores[element]))
        max_list.append(max(scores[element]))
        spread_list.append(max(scores[element]) - min(scores[element]))
    print(min_list)
    return spread_list


main()
