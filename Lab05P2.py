# Student Name: Jacob Bridges
# Date: 2/10/2024
# Random Number List Generator
import random


def main():
    # Create empty list
    first_list = []
    second_list = []

    # Step A: Get the total number of elements in each list
    response = int(input('Step A: How many numbers in each list? '))
    # Step B: Get the lowest and highest random number
    lower_bound = int(input('Step B: \nWhat is the lower bound for the random number? '))
    upper_bound = int(input('What is the upper bound for the random numbers? '))
    for fill_list in range(response):
        first_list.append(random.randint(lower_bound, upper_bound))
        second_list.append(random.randint(lower_bound, upper_bound))
    # Step C: Display the first list
    print(f'Step C: First List: {first_list}', end='')
    print()
    # Step D: Display the second list
    print(f'Step D: Second List: {second_list}', end='')
    print()
    # Step E  display the elements in the two lists in pairs using a for loop
    print('Step E: ')
    for index in range(len(first_list)):
        print(first_list[index], end=' ')
        print(second_list[index], end='')
        print()
    # Step F: concatenate and display new list with all the elements
    combine_list = first_list + second_list
    print(f'Step F: Combined list: {combine_list}')
    # Step G: sort the list and display output
    combine_list.sort()
    print(f'Step G: Sorted list: {combine_list} ')
    # Step H: Display the first three and the last three elements in the combined list
    print(f'Step H \nFirst three elements: {combine_list[:3]}')
    print(f'Last three elements: {combine_list[-3:]}')
    # Step I: Calculate and display the sum of the elements in the combined list
    print(f'Step I: Sum: {sum(combine_list)}')
    # Step J: Display the Minimum element in the list
    print(f'Step J: Minimum: {min(combine_list)}')
    # Step K: Display the Maximum element in the list
    print(f'Step K: Maximum: {max(combine_list)}')
    # Step L: Generate 5 random integers in the range specified by the user in step A
    print(f'Step L:')
    for index in range(response):
        random_number = random.randint(lower_bound, upper_bound)
        # Check if each number is in the combined list
        if random_number in combine_list:
            print(f'{random_number} at index {combine_list.index(random_number)}')
            combine_list.remove(random_number)
        elif random_number not in combine_list:
            print(f'{random_number} not found in list')

    # Step M: Print Final List
    print(f'Step M: Final List: {combine_list}')


# call the main function
main()
