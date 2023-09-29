# print(1) #integer number
# print(1.5) #float number
# print(20*24*60) #multiplication
# print("my job is great") #string
#string concatenation
day = 20
day_in_minute = 24*60
unit = "minute"
# print("20 days are", day*day_in_minute , "minute")
# print(f"20 days are {day*day_in_minute} {unit}")

#def function_day(days, customized_text):
#    print(f"{days} days are {days*day_in_minute} {unit}")
#    print(customized_text)
#    return f"{days} days are {days*day_in_minute} {unit}"
    
# def function_day(days, customized_text):
#     print(f"{days} days are {days*day_in_minute} {unit}")
#     if days > 0 :
#       print(days > 0)
#       print(customized_text)
#       return f"{days} days are {days*day_in_minute} {unit}"
#     else:
#       return "you enter negative value"
# function_day(5, "True")
# function_day(6, "True")
# user_input = input("fill colomn \n")
# user_input_number = int(user_input)
# print(user_input)

# var = function_day(user_input_number, "try")
# print(var)

def function_day(days):
    print(days > 0)
    if days > 0 :
      return f"{days} days are {days*day_in_minute} {unit}"
    else:
      return "you enter negative value"
user_input = input("fill colomn \n")
user_input_number = int(user_input)
print(user_input)

var = function_day(user_input_number)
print(var)