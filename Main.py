numbers = input("Enter comma-separated numbers: ") #asks the user

num_list = numbers.split(',') # split numbers with comma in the list
num_tuple = tuple(num_list) # makes tuple and is also comma seperated by putting num_list

print(f"{num_list} {num_tuple}") # print it out
