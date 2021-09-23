# Given
# 1. The guessing game should be written in plain English
# 2. The output messages if the user did not get the right number should either be too small or too large

# Required
# 1.The game should ask the user and allow them to input the number number they have guessed.
# 2.After the user inputs their guess the game should give an output to the user telling them whether their guess
# was too small or too large compared to the real number or whether they guessed the correct number
# 3. If the user guesses the right number, the game should output the number of tries it took them to guess the
# right number or the number of their entries in other words.

# Algorithm
# 1.Generate a random integer number between a certain range like 1 to 100
# 2.Ask the user to input the integer number they guessed between the set range
# 3.Initialize a variable which will count the number of the user's tries to zero and it shall increment by one
# each time the user enters a new number
# 4.Compare the number entered by the user to the generated random number and if the number entered by the user is
# equal to the generated random number print a message telling the user that they got it right. If the number
# entered by the user is smaller than the generated random number print the message to the user telling them that
# the number is too small. If the number is greater than the generated random number print the message to the user
# telling them that the number is too large.
# 5.If the user entered a number equal to the generated random number after telling them that they are correct,
# also print the number stored in the variable which was counting the number of entries(the one which was
# incrementing by one after each entry),telling them that it took them that number of tries to guess the correct
# number.
