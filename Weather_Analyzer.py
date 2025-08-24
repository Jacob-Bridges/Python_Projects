#
# Jacob Bridges
# Date 08/24/2025
# This program prompts the user to enter daily temperature information
# and then provides analysis of the data.
#


def collect_data(days):
    """Collects temperature data for a given number of days."""
    temperatures = []
    # Enter code here that will ask the user for the temperature for
    # Each of the days and add that data to the temperature list.
    # Temperature data is a number so make sure to catch if the user
    # doesn't enter a proper floating point number.
    for i in range(days):
        # Use try/excpet to catch value errors
        # Cast user input to float
        try:
            get_temp = float(input(f"Enter temperature for day {i+1} : "))
            temperatures.append(get_temp)
        except ValueError:
            # Pring the invalid input statement
            # Ask the user to enter temps for the day again
            # Append value to temperatures list
            print("Invalid input. Please enter a numeric value.")
            get_temp = float(input(f"Enter temperature for day {i+1} : "))
            temperatures.append(get_temp)

    return temperatures


def calculate_average(temperatures):
    """Calculates and returns the average temperature."""
    # Initialize average_temp
    average_temp = 0
    # for each element in range of the length of temperatures list
    # sum each element and divide by the length of the list
    for i in range(len(temperatures)):
        average_temp += temperatures[i] / len(temperatures)

    return average_temp


def find_max(temperatures):
    """Finds and returns the highest temperature."""
    # sort list in decesending order
    temperatures.sort(reverse=True)
    # set max_temp to list item at index 0
    max_temp = temperatures[0]

    return max_temp


def find_min(temperatures):
    """Finds and returns the lowest temperature."""
    # Sort temps in ascending order and return the element at index 0
    temperatures.sort()
    min_temp = temperatures[0]

    return min_temp


def above_threshold(temperatures, threshold):
    """Returns a list of temperatures above the given threshold."""
    new_temps = []
    for i in range(len(temperatures)):
        if temperatures[i] > threshold:
            new_temps.append(temperatures[i])

    return new_temps


def main():
    days = int(input("How many days of temperature data do you want to analyze? "))
    temps = collect_data(days)

    print("\nWeather Data Analysis")
    print("1. Average Temperature")
    print("2. Highest Temperature")
    print("3. Lowest Temperature")
    print("4. Temperatures Above Threshold")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice: ")
        if choice == "1":
            print(f"Average Temperature: {calculate_average(temps)}")
        elif choice == "2":
            print(f"Highest Temperature: {find_max(temps)}")
        elif choice == "3":
            print(f"Lowest Temperature: {find_min(temps)}")
        elif choice == "4":
            threshold = float(input("Enter the temperature threshold: "))
            print(
                f"Temperatures above {threshold}: {above_threshold(temps, threshold)}"
            )
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
