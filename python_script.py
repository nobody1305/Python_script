# print(1) #integer number
# print(1.5) #float number
# print(20*24*60) #multiplication
# print("my job is great") #string
#string concatenation
# day = 20
# day_in_minute = 24*60
# unit = "minute"
# print("20 num_of_days are", day*day_in_minute , "minute")
# print(f"20 num_of_days are {day*day_in_minute} {unit}")

#def function_day(num_of_days, customized_text):
#    print(f"{num_of_days} num_of_days are {num_of_days*day_in_minute} {unit}")
#    print(customized_text)
#    return f"{num_of_days} num_of_days are {num_of_days*day_in_minute} {unit}"
    
# def function_day(num_of_days, customized_text):
#     print(f"{num_of_days} num_of_days are {num_of_days*day_in_minute} {unit}")
#     if num_of_days > 0 :
#       print(num_of_days > 0)
#       print(customized_text)
#       return f"{num_of_days} num_of_days are {num_of_days*day_in_minute} {unit}"
#     else:
#       return "you enter negative value"
# function_day(5, "True")
# function_day(6, "True")
# user_input = input("fill colomn \n")
# user_input_number = int(user_input)
# print(user_input)

# var = function_day(user_input_number, "try")
# print(var)

# def function_day(num_of_days):
#     condition_check = num_of_days > 0
#     print(type(condition_check))
#     if num_of_days > 0 :
#       return f"{num_of_days} num_of_days are {num_of_days*day_in_minute} {unit}"
#     elif num_of_days == 0 :
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
#         num_of_days = int(user_input)
#         condition_check = num_of_days > 0
#         print(type(condition_check))
#         if num_of_days > 0 :
#             return f"{num_of_days} num_of_days are {num_of_days*day_in_minute} {unit}"
#         elif num_of_days == 0 :
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

# def function_day(user_input):
#     try:
#         num_of_days = int(user_input)
#         print(type(num_of_days))
#         if num_of_days > 0 :
#             return f"{num_of_days} num_of_days are {num_of_days*day_in_minute} {unit}"
#         elif num_of_days == 0 :
#             return "you enter zero, please enter positif number"
#         else :
#             return "you enter negative value"
#     except:
#         print(type(user_input))
#         if "." in user_input:
#             return "your input is decimal"
#         return "your input is not number. please try again"
def days_to_unit(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days*24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else:
        return "unsupported unit"
    
def function_day(days_and_unit_dictionary):
    try:
        num_of_days = int(days_and_unit_dictionary["days"])
        print(type(num_of_days))
        if num_of_days > 0 :
            return days_to_unit(num_of_days, days_and_unit_dictionary["unit"])
        elif num_of_days == 0 :
            return "you enter zero, please enter positif number"
        else :
            return "you enter negative value"
    except:
        print(type(days_and_unit_dictionary))
        if "." in user_input:
            return "your input is decimal"
        return "your input is not number. please try again"

# user_input = ""
# while user_input != "exit":   
#     print(type(user_input.split(", ")))
#     print(user_input.split(", "))
#     print(type(set(user_input.split(", "))))
#     print(set(user_input.split(", ")))
#     user_input = input("fill colomn \n")
#     for num_of_days in set(user_input.split(", ")):
#         var = function_day(num_of_days)
#         print(var)

user_input = ""
while user_input != "exit":   
    user_input = input("fill colomn \n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit":days_and_unit[1]}
    print(days_and_unit_dictionary)
    var=function_day(days_and_unit_dictionary)
    print(var)

# mylist = ["20", "30", "40"]
# print(mylist[0])
# mydictionary = {"num_of_days": 20, "unit": "minute"}
# print(mydictionary["unit"])