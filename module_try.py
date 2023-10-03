import python_script
# import python_script as p (rename module)
# from module_try import python_script (call a function from module)

user_input = ""
while user_input != "exit":   
    user_input = input("fill colomn \n")
    for user_input in user_input.split(", "):
        days_and_unit = user_input.split(":")
        print(days_and_unit)
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit":days_and_unit[1]}
        print(days_and_unit_dictionary)
        var = python_script.function_day(days_and_unit_dictionary)
        #var = function_day(days_and_unit_dictionary) (use it when only call one function from modules)
        print(var)