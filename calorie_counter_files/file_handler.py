import subprocess
from datetime import date, time, datetime

def write_baby_file(date, calorie_tracker):
    (cal_sum, cal_avg, pro_sum, pro_avg, carb_sum, carb_avg) = calorie_tracker
    file_date = datetime.now()
    baby_file_write = open("Baby_Calorie_Count.txt", 'a')
    print(f'welcome to the file handler function. Glad you could make it baby.')
    print(f'today is {file_date.strftime('%B/%d/%Y')}')

    baby_file_write.writelines(f'Sums and Averages for {file_date.strftime('%m/%d/%Y')}')
    baby_file_write.writelines('\n')
    baby_file_write.writelines(f'Calorie Sum: {str(cal_sum)}')
    baby_file_write.writelines('\n')
    baby_file_write.writelines(f'Calorie Average: {str(cal_avg)}')
    baby_file_write.writelines('\n')
    baby_file_write.writelines(f'Protein Sum: {str(pro_sum)}')
    baby_file_write.writelines('\n')
    baby_file_write.writelines(f'Protein Average: {str(pro_avg)}')
    baby_file_write.writelines('\n')
    baby_file_write.writelines(f'Carb Sum: {str(carb_sum)}')
    baby_file_write.writelines('\n')
    baby_file_write.writelines(f'Carb Average: {str(carb_avg)}')
    baby_file_write.writelines('\n')
    baby_file_write.writelines('\n')
    baby_file_write.close()
def read_baby_file():
    print("Hey! welcome to the read file function!!")
    name = input('You are no longer the baby! ')
    while name != 'who am I?':
        print('Wrong! Only the baby knows what to say. Try again')
        name = input('You are no longer the baby! ')
    if name =='who am I?':
        print('YOU ARE THE CALORIE COUNTING BABY!! GO BABAYAYA!')
        subprocess.call(['notepad.exe', 'Baby_Calorie_Count.txt'])
