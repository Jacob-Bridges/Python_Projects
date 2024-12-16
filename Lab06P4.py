# Jacob Bridges
# 2/18/24
# Matplot lib


import matplotlib.pyplot as plt


def main():
    title = input('Enter the bar graph title: ')
    x_axis_label = input('Enter the label for the x-axis: ')
    y_axis_label = input('Enter the label for the y-axis: ')

    data_points = int(input('Enter the number of data points: '))
    tick_name: list[str] = [input(f'Enter the name for tick {i + 1}: ') for i in range(data_points)]
    tick_data = [float(input(f'Enter the value for tick {i + 1}: ')) for i in range(data_points)]

    plt.title(title)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.bar(tick_name, tick_data)
    plt.show()


# Call the main function
main()
