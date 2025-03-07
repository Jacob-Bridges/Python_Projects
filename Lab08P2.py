# Jacob Bridges
# 3/9/2024
# daily sales report
def main():
    # Try to open the file
    try:
        file = open('sales.txt', 'r')
        # Pass file object to the total sales function
        total_sales(file)
        # Close the file
        file.close()
    # except if the file is not found, print error message
    except FileNotFoundError:
        print('File \'sales.txt\' not found')


def total_sales(file):
    # Create variable to count lines in the file
    line_num = 0
    # initialize product total variables
    DVD_total = 0
    GAME_total = 0
    BOOK_total = 0
    # for each line in the file
    for line in file:
        # create a list and split elements by comma
        sales_data = line.split(',')
        # strip space for each element
        for i in range(len(sales_data)):
            sales_data[i] = sales_data[i].strip(' ')
        # increment line accumulator
        line_num += 1
        # try to convert sales_data element at index 2 from a string to a float
        try:
            price = float(sales_data[2])
            # if sales_data list at index 1 is equal to the item category
            if sales_data[1] == 'DVD':
                # add price to item total variable
                DVD_total += price
            elif sales_data[1] == 'Game':
                GAME_total += price
            elif sales_data[1] == 'Book':
                BOOK_total += price
            # pass each total price to the sales_report function
            sales_report(DVD_total, GAME_total, BOOK_total)
        # except if sales_type_list at index 2 contains a ValueError.
        # Print a line to the console program could not convert to price format
        except ValueError:
            print(f'Error on line {line_num}: Could not convert "{sales_data[2].strip()}" to price format.')


def sales_report(DVD, GAME, BOOK):
    # create daily report file and set to write mode
    daily_report = open('daily_report.txt', 'w')
    # Use an f string to convert float variables to strings and write each price to the txt file
    daily_report.write(f'Books: ${BOOK:.2f}\n')
    daily_report.write(f'DVDs: ${DVD:.2f}\n')
    daily_report.write(f'Games: ${GAME:.2f}\n')
    # close the file
    daily_report.close()


main()
