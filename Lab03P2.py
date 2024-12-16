#
# Jacob Bridges
# 01/28/2024
# Pretty Pattern Generator
#
#

# Ask the user for the number of rows
num_rows = int(input('How many rows? '))
# Ask the user for the number of columns
num_columns = int(input('How many columns? '))

# Iterate over the rows.
for row in range(1, num_rows + 1):

    # Iterate over the columns.
    for col in range(1, num_columns + 1):
        # Test if the row and column are even numbered
        if row % 2 == 0 and col % 2 == 0:
            print(' ')
        else:
            print('*')

    # Go to the next row.
    print()
