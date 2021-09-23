# A program that prints the initials of my name in big letters.
# Names: Umubyeyi Evelyne

# This section creates two list which will hold the letters that make up each initial and initializes all list
# items to a blank space. Each list has 5 columns and 10 rows.
u = [[" " for a in range(5)] for b in range(10)]
e = [[" " for a in range(5)] for b in range(10)]

# Assigning letters to some list indexes in order to print the desired output using if condition
for row in range(10):
    for col in range(5):
        if ((col == 0 or col == 4) and row != 9) or (row == 9 and (col != 0 and col != 4)):
            u[row][col] = "U"


for row in range(10):
    for col in range(5):
        if col == 0 or row == 0 or row == 4 or row == 9:
            e[row][col] = "E"

# This section will print the above lists side by side.
for b in range(10):
    for a in range(5):
        print(u[b][a], end="")  # this will print a list item and continue on the same line instead of going to the
        # next line
    for a in range(5):
        # This if condition will check for each list item in the second list, if it's in the first column and leave
        # four white spaces if it is the first, so that the output can have space between two initials.
        if a == 0:
            print("    " + e[b][a], end="")
        else:
            print(e[b][a], end="")
    print()  # This will help to move to the next line after each row. Note: corresponding rows in the two lists
    # will be printed side by side.
