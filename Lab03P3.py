#
# Jacob Bridges
# Jan 28 2024
# This program calculates the cost for books, dvds and games
# This program will capture any data entry mistakes and will limit the number of items being sold
#
#
# Named Constant variables
BOOK = 2.25
DVD = 4.35
GAME = 5.00
TAX_RATE = .065
# Get input from user
books_purchased = int(input('Enter the number of books: '))
# While Books purchased is less than 0 or is greater than 30, tell user input is not valid and get new input
while books_purchased < 0 or books_purchased > 30:
    print('Number of books must be between 0 and 30.')
    books_purchased = int(input('Enter the number of books: '))
dvds_purchased = int(input('Enter the number of DVDs: '))
# While DVDs purchased is less than 0 or is greater than 15, tell user input is not valid and get new input
while dvds_purchased < 0 or dvds_purchased > 15:
    print('Number of DVDs must be between 0 and 15.')
    dvds_purchased = int(input('Enter the number of DVDs: '))
games_purchased = int(input('Enter the number of games: '))
# While Games purchased is less than 0 or is greater than 10, tell user input is not valid and get new input
while games_purchased < 0 or games_purchased > 10:
    print('Number of games must be between 0 and 10.')
    games_purchased = int(input('Enter the number of games: '))

# Processing
sub_total = (BOOK * books_purchased) + (DVD * dvds_purchased) + (GAME * games_purchased)
sales_tax = (sub_total * TAX_RATE)
total = (sub_total + sales_tax)

# Output
print(f'Cost before tax: {sub_total:.2f}')
print(f'Sales tax: {sales_tax:.2f}')
print(f'Cost after tax: {total:.2f}')
