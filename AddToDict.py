def main():
    # Create an empty dictionary
    # Ask the user to add a key to the dictionary and a value
    # display the dictionary
    test_dict = {}
    again = ''
    while again != 'q':
        addKey = input('Enter a key for the dictionary, or q to quit: ')
        addValue = input('Enter a value for the dictionary: ')
        again = input('again? press q to quit')
        test_dict[addKey] = addValue
    print(test_dict)


main()
