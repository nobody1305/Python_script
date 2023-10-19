import datetime

user_input = input("please input goal and deadline \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
deadline_time = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today = datetime.datetime.today()
time_till = deadline_time - today
#print(deadline_time)
#print(deadline_time - today)
#print(type(datetime.datetime.strptime(deadline, "%d.%m.%Y")))
in_hours = int(time_till.total_seconds()/60/60)
print(f"Dear User! time remaining until your goal : {goal} is {in_hours} hours")
print(input_list)
