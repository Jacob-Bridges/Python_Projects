import os
from traceback import print_tb
import pandas as pd
import subprocess
from datetime import date, time, datetime
import show_numbers, protein_counter, carb_counter, file_handler, calorie_counter

def main():
    date = datetime.today()
    welcome(date)
    print()
    calorie_tracker = show_numbers.show_numbers(date)
    print()
    write_file = input('Hey! welcome back to Main! Do you want me to record this info?')
    if write_file != 'n':
        file_handler.write_baby_file(date, calorie_tracker)
    elif write_file == 'n':
        print('...okaybye')

    read_file = input('Hey! welcome back to Main! Do you want to view your calorie info?')
    if read_file != 'n':
        file_handler.read_baby_file()
    elif read_file == 'n':
        print('...okaybye')

def welcome(date):

        print('Hello Baby! I love you so much and you look very pretty today :D')
        print()
        print('Welcome to your calorie tracker.')
        print('I will track your calorie, protein and carb intake from last week.')
        print(f'Today is {date.strftime('%m/%d/%Y')}')
        start = input('Are you ready? ')

        if start == 'y':
            print('Yay!')
        elif start == 'no':
            print('No baby! You must calculate your snacking!')
            start = input('Are you ready? ')



main()