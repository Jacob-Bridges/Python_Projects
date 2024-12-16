# Jacob Bridges
# 2/17/24
# Tuples

import random


def main():
    # Create empty tuple
    t1 = ()
    # convert tuple to a list
    l1 = list(t1)
    # get total elements
    print('Step a:')
    total_elements = int(input('How many values to put in the tuple? '))
    # Get range to generate random numbers
    print('Step b:')
    start = int(input('What is the start of the range? '))
    end = int(input('What is the end of the range? '))
    # for each element in range of the total elements
    # add a random number to the list within the specified range
    for element in range(total_elements):
        l1.append(random.randint(start, end))
    # convert list back to tuple
    t1 = tuple(l1)
    # create new tuple with the first 4 elements of the first tuple
    t2 = (t1[0:4])
    # create a new tuple with the last 2 elements of the first tuple
    t3 = (t1[-2:])

    print(f'Step c: Tuple of 8 random numbers: {t1}')
    print(f'Step d: Tuple of first 4 numbers: {t2}')
    print(f'Step e: Tuple of last 2 numbers: {t3}')
    print(f'Step f: Two tuples concatenated: {t3 + t2}')
    # convert tuple 3 and tuple 2 to a list
    l2 = list(t3 + t2)
    # add 1 for each element in list 2
    for element in range(len(l2)):
        l2[element] += 1
    # convert list 2 to tuple
    t4 = tuple(l2)
    print(f'Step g: Two tuples concatenated and incremented: {t4}')


main()
