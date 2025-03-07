# Using a for loop to go through a dictionary

def main():
    temperatures = {'Monday': 88.2,
                    'Tuesday': 79.1,
                    'Wednesday': 74.0,
                    'Thursday': 92.4,
                    'Friday': 76.8,
                    'Saturday': 74.0,
                    'Sunday': 80.3}

    for k in temperatures:
        print(k, temperatures[k])

    print(temperatures.keys())
    print(temperatures.values())

    for v in temperatures.values():
        print(v)

    print(temperatures.items())

    for item in temperatures.items():
        print(item)

    for k, v in temperatures.items():
        print(f'Key: {k}, Value: {v}')


main()
