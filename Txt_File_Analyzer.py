#
# Jacob Bridges
# Date 08/24/2025
# This program prompts the user for the filename of a file to analyze.
# It will then output the total number of words, the number of times each
# word appears in the file, and the list of words with that appear the
# most.
#


def read_file(filename):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")


def word_count(text):
    """Counts the total number of words in the text."""
    # Initialize total_count variable to hold total word count
    total_count = 0
    # Use Split method to split the text by spaces; otherwise, it counts the characters
    split_text = text.split()
    # Set value of total_count to length of split_text
    total_count = len(split_text)

    return total_count


def frequency_analysis(text):
    """Analyzes the frequency of each word in the text."""
    # Create an empty dictionary
    # Dict will store each word as the key and count as it's value
    word_dict = {}
    # create a list of words by using the split method to split the text
    words = text.split()
    # use list comprehension to lower each word in words list
    words = [word.lower() for word in words]

    # Use a for loop to iterate through the words list
    # if a word exists, set the key as the word and the value to the times its repeated
    # else, set the word as the value and the key as 1
    for word in words:
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1

    return word_dict


def most_frequent_word(frequency):
    """Identifies the most frequently used word(s) in the text."""
    # create an empty list to store the top 3 most frequent words
    frequent_words = []
    # run a for loop 3 times
    # append the most frequent word to frequent_words
    # pop the word from the frequency dictionary after appending to frequent_words
    for i in range(3):
        frequent_words.append(max(frequency, key=frequency.get))
        frequency.pop(max(frequency, key=frequency.get))
    return frequent_words


def main():
    """Main function to run the text file analyzer."""
    filename = input("Enter the name of the file to analyze: ")
    text = read_file(filename)

    if text is not None:
        print("\nAnalyzing text...\n")
        print("Total Word Count:", word_count(text))

        frequency = frequency_analysis(text)
        print("\nWord Frequency Analysis:")
        for word, count in frequency.items():
            print(f"{word}: {count}")

        most_frequent = most_frequent_word(frequency)
        print("\nMost Frequent Word(s):", ", ".join(most_frequent))


if __name__ == "__main__":
    main()
