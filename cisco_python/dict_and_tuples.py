#dict x tuple
school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

#dict x tuple
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {1 : 5551234567, 2 : 22657854310}
empty_dictionary = {}

mytuple = ()

def check_function(i):
    global mytuple
    for key in range(0,i):
        if key not in phone_numbers:
            print("false")
        elif key in phone_numbers:
            print(phone_numbers[key])
            mytuple = mytuple + (phone_numbers[key],)
    return mytuple
result = check_function(3)
print(result)
