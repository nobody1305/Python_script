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

# def function_day(days):
#     condition_check = days > 0
#     print(type(condition_check))
#     if days > 0 :
#       return f"{days} days are {days*day_in_minute} {unit}"
#     elif days == 0 :
#        return "you enter zero, please enter positif number"
#     else :
#       return "you enter negative value"
    
# user_input = input("fill colomn \n")

# if not user_input.isalpha() and '.' not in user_input:
#     user_input_number = int(user_input)
#     var = function_day(user_input_number)
#     print(var)
# else :
#     print("your input is not number. please try again")


# def function_day(user_input):
#     if not user_input.isalpha() and "." not in user_input:
#         days = int(user_input)
#         condition_check = days > 0
#         print(type(condition_check))
#         if days > 0 :
#             return f"{days} days are {days*day_in_minute} {unit}"
#         elif days == 0 :
#             return "you enter zero, please enter positif number"
#         else :
#             return "you enter negative value"
#     elif "." in user_input:
#         return "your input is decimal"
#     else:
#         return "your input is not number. please try again"
    
# user_input = input("fill colomn \n")
# var = function_day(user_input)
# print(var)

def function_day(user_input):
    try:
        days = int(user_input)
        print(type(days))
        if days > 0 :
            return f"{days} days are {days*day_in_minute} {unit}"
        elif days == 0 :
            return "you enter zero, please enter positif number"
        else :
            return "you enter negative value"
    except:
        print(type(user_input))
        if "." in user_input:
            return "your input is decimal"
        return "your input is not number. please try again"

user_input = ""
while user_input != "exit":   
    print(type(user_input.split(", ")))
    print(user_input.split(", "))
    print(type(set(user_input.split(", "))))
    print(set(user_input.split(", ")))
    user_input = input("fill colomn \n")
    for days in set(user_input.split(", ")):
        var = function_day(days)
        print(var)

