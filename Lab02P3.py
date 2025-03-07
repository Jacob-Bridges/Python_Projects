#
# 1/20/2024
# Jacob Bridges
#
#
# The purpose of this program is to demonstrate Bargain Swap Shop's gift card program
#
# Get total purchased
total_purchased = float(input('Enter the total purchase amount: '))
# Get loyalty program status
LP_Status = input('Is the customer a loyalty program member (y/n): ')
# Calculate sales tax on total purchased
sales_tax = total_purchased * .065
# Calculate the total purchased after tax
order_total = sales_tax + total_purchased
# Determine which gift card the customer gets
gift_card = 0


# if total purchased is less than $50 and LP Status is yes, customer does not get a gift card
if total_purchased < 50.00 and LP_Status == 'y':
    gift_card = 0
# If total purchased is less than or equal to 100 and LP Status is yes, gift card is $15
elif total_purchased <= 100.00 and LP_Status == 'y':
    gift_card = 15
# If total purchased is greater than 100 and LP Status is yes, gift card is $25
elif total_purchased > 100.00 and LP_Status == 'y':
    gift_card = 25
# If total purchased is greater than 100 and LP Status is no, gift card is $5
elif total_purchased > 100.00 and LP_Status == 'n':
    gift_card = 5
else:
    gift_card = 0

# Output Sales Tax
print(f'Sales tax: ${sales_tax:.2f}')
# Output total purchased with sales tax
print(f'Total after tax: ${order_total:.2f}')
# If gift card is 0, Output customer is not eligible for gift card
if gift_card == 0:
    print('You are not eligible for a gift card.')
# Output Gift Card Awarded
print(f'Gift Cart Awarded: ${gift_card}')
