import math

C = 50
H = 30

D_values = input("Enter values of D (comma-separated): ")
D_list = map(int, D_values.split(','))

results = [str(int(math.sqrt((2 * C * D) / H))) for D in D_list]

print("Calculated values of Q:", ",".join(results))
