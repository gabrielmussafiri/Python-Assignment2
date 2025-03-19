#1 Create an empty list called my_list
my_list = []

#2 Append the elements to my_list
for i in (10,20,30,40):
    my_list.append(i)
    
#3 Insert the value 15 at the second position in the list
my_list.insert(1, 15)

#4 Extend my_list with another list
my_list.extend([50, 60, 70])

#5 Remove the element at the last position from the list
my_list.pop()

#6 Sort my_list the list in the ascending order
my_list.sort()

#7 find and print the index of the value 30 in my_list
print(my_list.index(30))