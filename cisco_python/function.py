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

