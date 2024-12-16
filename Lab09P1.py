#
# Jacob Bridges
# 3/21/2024
# Word counting in dictionaries
#

# DO NOT UPDATE ANY PART OF THE MAIN FUNCTION
def main():
    input_file = open('words.txt', 'r')  # Open a file for reading
    file_text = input_file.read().upper()  # Read all contents and convert to uppercase
    process_file(file_text)
    input_file.close()


def process_file(text):
    # Create an empty Dictionary
    text_dict = {}
    # Use the split method to get a list of words from the input parameter
    key_list = text.split()

    # TODO: Use a for loop to go through the list 1-by-1
    #  and count the occurrence of each word. Add or update
    #  the entries in the dictionary with the word/count pairs.
    for element in key_list:
        text_dict[element] = key_list.count(element)

    # Print the dictionary
    print(text_dict)
    # TODO: Create a list of words with the maximum count
    max_words = []

    max_words.append(max(text_dict.keys()))

    # and print the list.
    print(f'Words with max count of {max(text_dict.values())}: {max_words}')
    # TODO: Remove the words with max count from the dictionary
    for element in max_words:
        if element in max_words:
            del text_dict[element]

    #  and print the dictionary.
    print(f'Dictionary with max removed: {text_dict}')
    # TODO: Put all the words in the dictionary in a list, sort it,
    sort_list = list(text_dict.keys())

    #  and print the list of sorted words.
    print(f'Words sorted: {sorted(sort_list)}')


main()
