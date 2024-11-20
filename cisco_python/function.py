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
