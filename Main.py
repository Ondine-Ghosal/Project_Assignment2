# Accepting a sequence of lines as input
while True:
    try:
        line = input("Enter a line of text: ")
        print(line.upper())  # Print the line in uppercase
    except KeyboardInterrupt:
        print("\nInput ended.")
        break
