# A program for a game called ALU hangman where the user is asked 10 questions about ALU, and each time they get a
# a question wrong, they are hanging a man. If they get 6 questions wrong the man dies but if they get all questions
# right or get less than 6 questions wrong the man lives.

# Welcoming the player and explaining to them how the game works.

print("Welcome to the ALU hangman game, hope you're readyyyy? Let's see if you really know ALU.")
print("Each time you give a wrong answer you are hanging a man."
      " 6 questions wrong the man dies. Let's gooo....")

# Questions section
# initializing variables which will count the number of correct, wrong answers entered by the user and the number
# of the questions the user has answered so far.
correct = 0
wrong = 0
answered_questions = 0

# this while loop will allow the user to enter answers only 10 times and to exit the loop (end the game) if the
# user reaches the limit of allowed wrong answers (6)
while answered_questions <= 9:
    a = int(input("When was ALU founded? "))
    # Each time the user answers the answered_questions variable will count by incrementing by one.
    answered_questions += 1
    if a == 2015:
        # Each time the user gives a correct answer the correct variable will count by incrementing by one.
        correct += 1
        print("correct")
    else:
        # Each time the user gives a wrong answer the wrong variable will count by incrementing by one.
        wrong += 1
        print(f"Wrong. You are hanging the man and if you get {6-wrong} more questions wrong the man dies")

    b = input("Who is the CEO of ALU? ")
    answered_questions += 1
    # this will convert the user's response to upper case and then check if it is correct.
    if b.upper() == "FRED SWANIKER":
        correct += 1
        print("correct")
    else:
        wrong += 1
        print(f"Wrong. You are hanging the man and if you get {6-wrong} more questions wrong the man dies")

    c = input("Where are ALU campuses? ")
    answered_questions += 1
    if c.upper() == "RWANDA AND MAURITIUS":
        correct += 1
        print("correct")
    else:
        wrong += 1
        print(f"Wrong. You are hanging the man and if you get {6-wrong} more questions wrong the man dies")

    d = int(input("How many campuses does ALU have? "))
    answered_questions += 1
    if d == 2:
        correct += 1
        print("correct")
    else:
        wrong += 1
        print(f"Wrong. You are hanging the man and if you get {6-wrong} more questions wrong the man dies")

    e = input("What is the name of ALU Rwanda’s Dean? ")
    answered_questions +=1
    if e.upper() == "GAIDI FARAJ":
        correct += 1
        print("correct")
    else:
        wrong += 1
        print(f"Wrong. You are hanging the man and if you get {6-wrong} more questions wrong the man dies")

    f = input("Who is in charge of Student Life? ")
    answered_questions +=1
    if f.upper() == "SILA OGIDI":
        correct += 1
        print("correct")
    else:
        wrong += 1
        # since we have reached six questions there is a possibility that the user gave wrong answers from the
        # beginning therefore the program must begin to check after every wrong answer if it's the sixth and if
        # true end end the loop
        if wrong == 6:
            print("The man dies. Game over!!!")
            break
        else:
            print(f"Wrong. You are hanging the man and if you get {6 - wrong} more questions wrong the man dies")

    g = input("What is the name of our Lab? ")
    answered_questions +=1
    if g.upper() == "MALI":
        correct += 1
        print("correct")
    else:
        wrong += 1
        if wrong == 6:
            print("The man dies. Game over!!!")
            break
        else:
            print(f"Wrong. You are hanging the man and if you get {6-wrong} more questions wrong the man dies")

    h = int(input("How many students do we have in Year 2 CS? "))
    answered_questions +=1
    if h == 57:
        correct += 1
        print("correct")
    else:
        wrong += 1
        if wrong == 6:
            print("The man dies. Game over!!!")
            break
        else:
            print(f"Wrong. You are hanging the man and if you get {6-wrong} more questions wrong the man dies")

    i = int(input("How many degrees does ALU offer? "))
    answered_questions +=1
    if i == 8:
        correct += 1
        print("correct")
    else:
        wrong += 1
        if wrong == 6:
            print("The man dies. Game over!!!")
            break
        else:
            print(f"Wrong. You are hanging the man and if you get {6-wrong} more questions wrong the man dies")

    j = input("Where are the headquarters of ALU? ")
    answered_questions +=1
    if j.upper() == "MAURITIUS":
        correct += 1
        print("correct")
    else:
        wrong += 1
        if wrong == 6:
            print("The man dies. Game over!!!")
            break
        else:
            print(f"Wrong. You are hanging the man and if you get {6-wrong} more questions wrong the man dies")
# This will be printed if the user makes it to the last question with less than 6 wrong answers.
if correct == 10:
    print("Congratulations you got everything right. The man lives. The game is over!!!")
elif correct != 10 and wrong < 6:
    print(f"The man lives, you got {wrong} questions wrong. The game is over!!")
