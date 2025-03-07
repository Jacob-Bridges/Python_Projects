##
# Jacob Bridges
# 2/1/2024
# Trish's Swap Shop Calculator
#
# Global Constants
BOOK_PRICE = 2.25
DVD_PRICE = 4.35
GAME_PRICE = 5.00
TAX_RATE = 0.065  # Tax Rate of 6.5%


def main():  # DO NOT CHANGE ANY CODE IN THE MAIN ROUTINE
    # NOTE: This program is NOT doing input validation to simplify the
    # program. To do input validation we would need to insert these lines
    # into while loops.
    num_books = int(input('Enter the number of books: '))
    num_dvds = int(input('Enter the number of DVDs: '))
    num_games = int(input('Enter the number of games: '))

    calc_and_display_total(num_books, num_dvds, num_games)


# Create a function called calc_and_display_total. It should take
# 3 parameters. Use the names provided here:
#    books  - Number of books
#    dvds  - Number of dvds
#    games  - Number of games
#
# It should calculate and display the total cost of each item. It should also
# calculate and display the total cost with tax.

# calc_and_display_total Function call passes the user input to 3 parameters
# calc_and_display_total calculates the subtotal cost of the books, dvds, and games first.
# Once the subtotal is calculated, the function calculates the total tax by multiplying the subtotal by the tax rate
# Once the subtotal and tax cost is calculated, the function adds the subtotal and the tax together to get total cost
# Once the calculations are done, the function displays the results rounded to 2 decimal points
def calc_and_display_total(books, dvds, games):
    book_total_cost = books * BOOK_PRICE
    dvd_total_cost = dvds * DVD_PRICE
    game_total_cost = games * GAME_PRICE
    subtotal = book_total_cost + dvd_total_cost + game_total_cost
    tax_cost = subtotal * TAX_RATE
    total_cost = subtotal + tax_cost

    print(f'Books: ${book_total_cost:.2f}')
    print(f'DVDs: ${dvd_total_cost:.2f}')
    print(f'Games: ${game_total_cost:.2f}')
    print(f'Subtotal: ${subtotal:.2f}')
    print(f'Tax: ${tax_cost:.2f}')
    print(f'Total: ${total_cost:.2f}')


main()
