import math # imports the module math


C = 50
H = 30

D_values = input("Enter values of D (comma-separated): ")
D_list = map(int, D_values.split(',')) # Splits words based on where a comma is

results = [str(int(math.sqrt((2 * C * D) / H))) for D in D_list] # Does the calculations in intergers then converts to a string

print("Calculated values of Q:", ",".join(results)) # Prints the values and joining the results toghether
