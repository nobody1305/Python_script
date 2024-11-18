# sorting list manual 
my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

#sorting list auto
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

#reverse list
a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()

print(lst)

#operating list 
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Write your code here.
my_list2 = []
for number in my_list:
    if number not in my_list2:
        my_list2.append(number)
my_list = my_list2
print("The list with unique elements only:")
print(my_list)

#or
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Write your code here.
my_list2 = []
for i in range(len(my_list)):
    if my_list[i] not in my_list2:
        my_list2.append(my_list[i])
my_list = my_list2
print("The list with unique elements only:")
print(my_list)

#the inner life of list 
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

#powerful slices
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)


