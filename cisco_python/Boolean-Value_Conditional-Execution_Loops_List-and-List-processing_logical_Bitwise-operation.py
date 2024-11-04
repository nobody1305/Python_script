#more way to def variable
x, y, z = 5, 10, 8
 
print(x > z)
print((y - 5) == x)

#boolean value - Question and answer
n = int(input("Enter your input here: "))
answer = n >= 100
print(answer)

#or 
n = int(input("Enter a number: "))
print(n >= 100)

#if condition 
input_plan = input("please input your plan: ")
if input_plan == "Spathiphyllum" :
    print("Yes - Spathiphyllum is the best plant ever!")
elif input_plan == "spathiphyllum" :
    print("No, I want a big Spathiphyllum!")
else :
    print(f"Spathiphyllum! Not {input_plan} !")

#tax calculator
income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
	if tax < 0.0:
	    tax = 0.0
# Write the rest of your code here.
elif income > 85528:
    tax = 14839.02 + (income - 85528) * 0.32
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
 
#Leap Year Calender
year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")

#or
year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")
	
#loop
#odd even number
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# guess secret number while loop
secret_number = 777
input_number = int(input("Please Enter Number:"))

while input_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    input_number = int(input("Please Enter Number:"))
    
print("Well done, muggle! You are free now.")

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# for loop three arguments
for i in range(2, 8, 3):
    print("The value of i is currently", i)

# more example of for loop 
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

# counting mississippily
import time

# Write a for loop that counts to five.
for i in range(1,6):
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    print(i, "Mississippi")
    # Body of the loop - use: time.sleep(1)
    time.sleep(1)
# Write a print function with the final message.
print("Ready or not, here I come!")

# break - example
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

#largest number v1
while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

#largest number v2
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end the program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

#break statement - stuck in loop 
key = "chupacabra"
user_input = str(input("Please Enter Word to left the loop:"))

while user_input != key:
    if user_input == key:
        break
    user_input = str(input("Please Enter Word to left the loop:"))
print("You've successfully left the loop.")

# continue statement - vowel eater
# Prompt the user to enter a word
input_user = str(input("Please Enter Word:"))
# and assign it to the user_word variable.
user_word = input_user
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop.
    
    if letter in ("A","I","U","E","O"):
        continue
    print(letter)


