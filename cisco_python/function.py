#two parameter function
def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")

#three parameter function
def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)

# wrong way to place default argument
# def add_numbers(a, b=2, c):
#     print(a + b + c)

# add_numbers(a=1, c=3)

# correct way to place default argument
def add_numbers(a, c, b=2):
    print(a + b + c)

add_numbers(a=1, c=3)

#leap year Function
def is_year_leap(year):
    #
    # Write your code here.
    if year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#how many days 
def is_year_leap(year):
    #
    # Your code from the previous LAB.
    if year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    return False

def days_in_month(year, month):
    #
    # Write your new code here.
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    if month in months_31:
        return 31
    elif month in months_30:
        return 30
    elif month == 2 and is_year_leap(year) == True:
        return 29
    elif month == 2 and is_year_leap(year) == False:
        return 28


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


#day in year 
def is_year_leap(year):
    #
    # Your code from the previous LAB.
    if year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    return False

def days_in_month(year, month):
    #
    # Write your new code here.
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    if month in months_31:
        return 31
    elif month in months_30:
        return 30
    elif month == 2 and is_year_leap(year) == True:
        return 29
    elif month == 2 and is_year_leap(year) == False:
        return 28

def day_of_year(year, month, day):
    #
    # Write your new code here.
    days = 0
    if month <= 12:
        if day <= days_in_month(year, month):
            for i in range(1, month):
                days += days_in_month(year,i)
            days += day
            return(days)
        else:
            return(None)
    else:
        return(None)

print(day_of_year(2000, 12, 32))

#prime number
def is_prime(num):
    # Write your code here.
    for i in range(2, num):
        number = num
        if number % i == 0:
            return False
            break
        else:
            for i in range(3, num):
                number = num
                if number % i == 0:
                    return False
    return True
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

#prime number another solution
def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

#prime number another solution
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(1, 100):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

#conversion fuel consumption
def liters_100km_to_miles_gallon(liters):
    #
    # l = 1/3.785411784 g
    # m = 1/1609.344 miles
    
    # Write your code here.
    # l/100km = x/100000 l/m = x/100000 (1/3.785411784)*(1609.344) = x * 1609.344/(100000*3.785411784) gpm 
    # 100km/l = (100000*3.785411784)/(x * 1609.344) mpg

    result = (100000*3.785411784)/(liters*1609.344)
    return result

def miles_gallon_to_liters_100km(miles):
    #
    # Write your code here.
    # m/g = x*1609.344/(3.785411784*100000) 100km/l 
    # g/m = (3.785411784*100000)/(x*1609.344) l/100km
    result =(3.785411784*100000)/(miles*1609.344)
    return result

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


