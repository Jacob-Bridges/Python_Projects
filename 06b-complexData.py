# Dealing with table data

# Car data using two dictionaries
car_year = {"Toyota RAV4": 2019,
            "Ford Ranger": 2015,
            "Honda CR-V": 2018,
            "Lincoln Towncar": 2013,
            "Chevy Volt": 2020}

car_price = {"Toyota RAV4": 22695.00,
             "Ford Ranger": 14325.00,
             "Honda CR-V": 19832.00,
             "Lincoln Towncar": 12289.00,
             "Chevy Volt": 20395.00}

car = input('Enter a car to find: ')
if car in car_year and car in car_price:
    print(f'{car}: Year {car_year[car]}, Price {car_price[car]}')
else:
    print(f'{car} not found.')


# Car data using nested dictionaries
cars = {"Toyota RAV4": {"year": 2019, "price": 22695.00},
        "Ford Ranger": {"year": 2015, "price": 14325.00},
        "Honda CR-V": {"year": 2018, "price": 19832.00},
        "Lincoln Towncar": {"year": 2013, "price": 12289.00},
        "Chevy Volt": {"year": 2020, "price": 20395.00}}

car = input('Enter a car to find: ')
if car in cars:
    print(f'{car}: Year {cars[car]["year"]}, Price {cars[car]["price"]}')
else:
    print(f'{car} not found.')
