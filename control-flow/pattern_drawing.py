size = int(input("Enter the size of the pattern: "))

row = 0  # Start row index
while row < size:
    # Print a row of asterisks using a for loop
    for col in range(size):
        print("*", end="")  # Print stars side by side without newline
    print()  # After each row, go to the next line
    row += 1  # Move to the next row