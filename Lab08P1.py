# Jacob Bridges
# 3/8/2024
# Error Log Counter

def main():
    # Try to open the file
    try:
        file = open('program.log', 'r')
        # Pass file object to error count function
        error_count(file)
        # close the file
        file.close()
    # if the file is not found, print error message
    except FileNotFoundError:
        print('File program.log not found')


def error_count(file):
    # Initialize five counters to zero
    critical = 0
    info = 0
    unknown_error = 0
    warning = 0
    error = 0
    # for each line in the file
    for line in file:
        # create a list and split the lines by space
        error_type = line.split(' ')
        # if the element in list at index 3 is equal to the error type
        if error_type[3] == 'CRITICAL':
            # increment the count by one
            critical += 1
        elif error_type[3] == 'INFO':
            info += 1
        elif error_type[3] == 'WARNING':
            warning += 1
        elif error_type[3] == 'ERROR':
            error += 1
        else:
            unknown_error += 1
    # Pass error counters to the print error count function
    print_error_count(critical, info, unknown_error, warning, error)


def print_error_count(critical, info, unknown_error, warning, error):
    # print the total error counts for each error type
    print(f'CRITICAL: {critical}')
    print(f'ERROR: {error}')
    print(f'WARNING: {warning}')
    print(f'INFO: {info}')
    print(f'UNKNOWN: {unknown_error}')


main()
