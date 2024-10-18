#string + end
print("My name is", "Python.", end="_")
print("Monty Python.")

#separator
print("My", "name", "is", "Monty", "Python.", sep="-")
print("    *","   * *","  *   *"," *     *","***   ***","  *   *","  *   *","  *****",sep="\n")

#hexadecimal number 0000 0110 0001
print(0x061)

#octal number 000 110 001
print(0o061)

print("\"I'm\"","\"\"learning\"\"","\"\"\"Python\"\"\"", sep="\n")

#exponentiation
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#multiplication
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#division
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

#integer division (floor division)
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

#positive floor division (always come to lessser value)
print(6 // 4)
print(6. // 4)

#negative floor division (always come to lessser value)
print(-6 // 4)
print(6. // -4)

#modulo 
print(14 % 4) # 14 // 4 = 3, 3 * 4 = 12, 14 - 12 (integer)
print(12 % 4.5) # 12 // 4.5 = 2.0, 2.0 * 4.5 = 9.0, 12 - 9.0 = 3.0 (float)

#addition and substraction
print(-4 + 4)
print(-4. + 8)
print(-4 - 4)
print(4. - 8)

#operator and their bindings
print(9 % 6 % 2) #left side binding
#from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1;
#from right to left: first 6 % 2 gives 0, and then 9 % 0 causes a fatal error.

print(2 ** 2 ** 3) #right side binding
#2 ** 2 → 4; 4 ** 3 → 64
#2 ** 3 → 8; 2 ** 8 → 256

#prove that exponentiation is right side binding
print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))

# priority list of operator python
# the ** operator (exponentiation) has the highest priority;
# then the unary + and - (note: a unary operator to the right of the exponentiation operator binds more strongly, for example 4 ** -1 equals 0.25)
# then: *, /, and %,
# and finally, the lowest priority: binary + and -.

# variable
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=',')

total_apples = john + mary + adam
print("Total number of apples:", total_apples)

peter = 12.5
suzy = 2
print(peter / suzy)
print("Total number of apples:", total_apples)

# shortcut variable
sheep = 1
x = 2
sheep = sheep + 1
x = x * 2

x *= 2
sheep += 1
print(x, sheep)

#conversion 
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.60934
kilometers_to_miles = kilometers * 0.621371

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#Operators and expressions
x = -1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)

#user input 
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

#user input with argument 
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

#user input with data type conversion
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

#string operator
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

#replication
#comutative rule
#string * number
#number * string
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#type data
x = input("Enter a number: ") 
print(type(x))

### test
# input a float value for variable a here
a = float(input("Enter number a here: "))
# input a float value for variable b here
b = float(input("Enter number b here: "))

# output the result of addition here
addition = a + b
print(addition)
# output the result of subtraction here
substraction = a - b
print(substraction)
# output the result of multiplication here
multiplication = a * b
print(multiplication)
# output the result of division here
division = a / b
print(division)

print("\nThat's all, folks!")

### test 2
x = float(input("Enter value for x: "))

# Write your code here.
y = 1 / (x + (1 / (x + (1 / (x + 1/x)))))


print("y =", y)

### test 3
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
mins = mins + dura
hour = hour + mins // 60
mins = mins % 60
hour = hour % 24

print(hour,":",mins,sep=" ")

