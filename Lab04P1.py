##
# Jacob Bridges
# 2/1/2024
# Landscape Job Estimator
#
import math

# Global constants for paint job estimator
FEET_PER_BAG = 50
HOURS_PER_BAG = 2
LABOR_CHARGE = 40.00
PROJECT_FEE = 100.00


# main module
def main():
    # Ask the user for the garden space in square feet
    garden_space = float(input('Enter garden space in square feet: '))

    # Ask the user for the mulch price
    mulch_price = float(input('Enter mulch price per bag: '))

    # Calculate number of bags needed
    num_bags = math.ceil(garden_space / FEET_PER_BAG)

    # Calculate labor hours (2 hours labor for every bag of mulch)
    hours_labor = num_bags * HOURS_PER_BAG

    # Calculate labor charge (including project fee)
    cost_labor = (LABOR_CHARGE * hours_labor) + PROJECT_FEE

    # Calculate mulch cost
    mulch_total_cost = num_bags * mulch_price

    # Print cost estimate
    showCostEstimate(num_bags, hours_labor, mulch_total_cost, cost_labor)


# The showCostEstimate function accepts bags_mulch, labor_hours,
# mulch_total, labor_total as arguments and displays the corresponding
# data.
def showCostEstimate(bags_mulch, labor_hours, mulch_total, labor_total):
    # Calculate total cost
    totalCost = mulch_total + labor_total

    # Display results
    print(f'Bags of mulch: {bags_mulch}')
    print(f'Hours of labor: {labor_hours}')
    print(f'Mulch charges: ${mulch_total:.2f}')
    print(f'Labor charges: ${labor_total}')
    print(f'Total cost: ${totalCost:.2f}')


# Call the main function.
main()
