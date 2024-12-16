#
# Jacob Bridges
# 2/8/2024
# Module to help process item data
#

# Global Constants - Use these in your program where it makes sense
TAX_RATE = 0.065  # 6% sales tax
VOLUME_DISCOUNT = 0.95  # 95% of total is 5% off


# The get_item_count function takes three parameters:
#    item_name - Name of item being prompted about
#    max_allowed - Maximum number of items the user can enter
#    discount_threshold - Minimum number of items eligible for 5% discount
#
# This function will ask the user to enter the number of items and
# validate the number entered is between 0 and the max_allowed
# inclusive. The number of items the user enters is returned.
def get_item_count(item_name, max_allowed, discount_threshold):
    print(f'Enter the number of {item_name}. ')
    items = int(input(f'\t{discount_threshold} or more receive a discount: '))
    while items < 0 or items > max_allowed:
        if item_name == 'books':
            print('\tNumber of items must be between 0 and 40. ')
            items = int(input(f'\tEnter the number of {item_name}. '))
        elif item_name == 'DVDs':
            print('\tNumber of items must be between 0 and 15. ')
            items = int(input(f'\tEnter the number of {item_name}. '))
        else:
            print('\tNumber of items must be between 0 and 25. ')
            items = int(input(f'\tEnter the number of {item_name}. '))
    return items


# The get_item_total function takes two parameters:
#     num_items - Number of items
#     unit_price - The cost of each item
#     discount_threshold - Minimum number of items eligible for 5% discount
#
# This function calculates the total cost for the items and
# returns that value.
def get_item_total(num_items, unit_price, discount_threshold):
    if num_items >= discount_threshold:
        return (num_items * unit_price) * VOLUME_DISCOUNT
    else:
        return num_items * unit_price


# The calc_and_display_receipt function will calculate all the
# necessary values and display the receipt. It takes three parameters:
#    book_total - Total cost of books
#    dvd_total - Total cost of DVDs
#    game_total  - Total cost of games
#
# This function will calculate total before tax, the tax on the total,
# and the total after tax is added.
#
# The receipt should display the total cost of books, DVDs, and
# games IF the item cost is greater than 0. The receipt should also
# include the subtotal, tax, and total.
def calc_and_display_receipt(book_total, dvd_total, game_total):
    sub_total = book_total + dvd_total + game_total
    tax = sub_total * TAX_RATE
    total = sub_total + tax
    if book_total > 0:
        print(f'Books: ${book_total:.2f}')
    if dvd_total > 0:
        print(f'DVDs: ${dvd_total:.2f}')
    if game_total > 0:
        print(f'Games: ${game_total:.2f}')
    # Create divider line
    for line in range(21):
        print('-', end='')
    print()
    # print subtotal, tax and total
    print(f'Subtotal: ${sub_total:.2f}')
    print(f'Tax: ${tax:.2f}')
    print(f'Amount Due: ${total:.2f}')
