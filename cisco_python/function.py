# wrong way to place default argument
def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)

# correct way to place default argument
def add_numbers(a, c, b=2):
    print(a + b + c)

add_numbers(a=1, c=3)
