numbers = input("Enter comma-separated numbers: ")

num_list = numbers.split(',')
num_tuple = tuple(num_list)

print(f"{num_list} {num_tuple}")
