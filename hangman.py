# hangman game
import turtle
import time


def draw_head(turtle1):
    turtle1.penup()
    turtle1.goto(-50, 150)
    turtle1.pendown()
    turtle1.right(180)
    turtle1.circle(50)
    turtle1.right(180)


def draw_upper_body(turtle1):
    turtle1.penup()
    turtle1.goto(-50, 50)
    turtle1.pendown()
    turtle1.right(90)
    turtle1.forward(100)
    turtle1.left(90)


def draw_lower_body(turtle1):
    turtle1.penup()
    turtle1.goto(-50, -50)
    turtle1.pendown()
    turtle1.right(90)
    turtle1.forward(100)
    turtle1.left(90)


def draw_left_leg(turtle1):
    turtle1.penup()
    turtle1.goto(-50, -150)
    turtle1.right(60)
    turtle1.pendown()
    turtle1.forward(100)
    turtle1.left(60)


def draw_right_leg(turtle1):
    turtle1.penup()
    turtle1.goto(-50, -150)
    turtle1.right(120)
    turtle1.pendown()
    turtle1.forward(100)
    turtle1.left(120)


def draw_left_hand(turtle1):
    turtle1.penup()
    turtle1.goto(-50, 0)
    turtle1.right(70)
    turtle1.pendown()
    turtle1.forward(100)
    turtle1.left(70)


def draw_right_hand(turtle1):
    turtle1.penup()
    turtle1.goto(-50, 0)
    turtle1.right(110)
    turtle1.pendown()
    turtle1.forward(100)
    turtle1.left(110)


def draw_eyes(turtle1):
    turtle1.penup()
    turtle1.goto(-50-50/4, 100)
    turtle1.left(90)
    turtle1.pendown()
    turtle1.forward(25)
    turtle1.penup()
    turtle1.goto(-50/4*3, 100)
    turtle1.pendown()
    turtle1.forward(25)
    turtle1.right(90)


def draw_dead_eyes(turtle1):
    turtle1.penup()
    turtle1.goto(-75, 125)
    turtle1.pendown()
    turtle1.goto(-75+50/8*3, 100)
    turtle1.penup()
    turtle1.goto(-75+50/8*3, 125)
    turtle1.pendown()
    turtle1.goto(-75, 100)
    turtle1.penup()
    turtle1.goto(-50+50/8, 125)
    turtle1.pendown()
    turtle1.goto(-25, 100)
    turtle1.penup()
    turtle1.goto(-25, 125)
    turtle1.pendown()
    turtle1.goto(-50+50/8, 100)


def draw_mouth(turtle1):
    turtle1.penup()
    turtle1.goto(-50-50/4, 50+50/4*3)
    turtle1.pendown()
    turtle1.forward(25)
    turtle1.right(90)
    turtle1.forward(25/2)
    turtle1.right(90)
    turtle1.forward(25)
    turtle1.right(90)
    turtle1.forward(25/2)
    turtle1.right(90)


def draw_hanger(turtle1):
    turtle1.penup()
    turtle1.goto(-50, 150)
    turtle1.left(90)
    turtle1.pendown()
    turtle1.pensize(4)
    turtle1.forward(100)
    turtle1.left(90)
    turtle1.forward(250)
    turtle1.left(90)
    turtle1.forward(500)
    turtle1.left(90)
    turtle1.forward(150)
    turtle1.backward(300)
    turtle1.pensize(2)


# a function that counts the number of unique character in a string
def count_unique_char(str1):
    unique_char = []
    for char in str1:
        if char not in unique_char:
            unique_char.append(char)
    return len(unique_char)


def hangman():
    # create a turtle
    hanger = turtle.Turtle()
    hm = turtle.Turtle()
    title = turtle.Turtle()
    message = turtle.Turtle()
    word = turtle.Turtle()
    life_left = turtle.Turtle()

    # set background color
    wn = turtle.Screen()
    wn.setup(width=1000, height=600)
    wn.bgcolor("LightCyan2")
    wn.title("Hangman Game!")
    wn.tracer(0, 0)

    # initialize turtles
    hanger.hideturtle()
    hm.hideturtle()
    title.hideturtle()
    message.hideturtle()
    word.hideturtle()
    life_left.hideturtle()
    hm.speed(8)
    hm.color("dim gray")
    hm.pensize(2)
    title.penup()
    title.color("tomato")
    message.color("DarkOrange1")
    message.penup()
    message.goto(0, -50)
    word.penup()
    word.goto(250, -100)
    life_left.penup()
    life_left.goto(400, 250)
    wn.update()

    # initialize screen
    title.write("Hangman", move=False, align="center", font=("Rockwell", 50, "normal"))
    message.write("To Start the Game: Enter the name of Player 1 in the console.", move=False, align="center",
                  font=("Rockwell", 25, "normal"))
    wn.update()

    # initialize the game
    life = 0
    player1 = input("Please enter the name of Player 1: ")
    message.clear()
    message.write("To Start the Game: Enter the name of Player 2 in the console.", move=False, align="center",
                  font=("Rockwell", 25, "normal"))
    wn.update()
    player2 = input("Please enter the name of Player 2: ")
    message.clear()
    message.write("To Start the Game: Enter the game difficulty you want to play.", move=False, align="center",
                  font=("Rockwell", 25, "normal"))
    wn.update()
    mode = input("Please choose the game difficulty (easy: 9 lives, medium: 7 lives, hard: 4 lives): ")
    while mode != "easy" and mode != "medium" and mode != "hard":
        print("Please type in 'easy', 'medium', or 'hard' to select the game difficulty you want to play.")
        mode = input("Please choose the game difficulty (easy: 9 lives, medium: 7 lives, hard: 4 lives): ")
    else:
        print("You have chosen the " + mode + " mode!")
        if mode == "easy":
            life = 9
        elif mode == "medium":
            life = 7
        elif mode == "hard":
            life = 4
        message.clear()
        message.write(player2 + ", you will have " + str(life) + " lives in total.", move=False, align="center",
                      font=("Rockwell", 25, "normal"))
        wn.update()
        print(player2 + ", you will have " + str(life) + " lives in total.")

    time.sleep(3)

    # game start screen
    title.clear()
    title.write("Game Start!", move=False, align="center", font=("Rockwell", 35, "normal"))
    print()
    print("Game Start!")
    message.clear()
    wn.update()

    time.sleep(2)

    # start the game
    # Ask Player 1 to input a word
    title.clear()
    message.goto(0, 0)
    message.write(player1 + ", please type in a word in the console.", move=False, align="center",
                  font=("Rockwell", 25, "normal"))
    title.goto(0, -50)
    title.write("Keep it as a secret! Click the Clear All button after you've finished!", move=False,
                align="center", font=("Rockwell", 20, "normal"))
    print()
    word_to_guess = input(player1 + " - Please input a word for Player 2 to guess: ")
    print("Now, click the Clear All button (i.e. rubbish bin icon) on the right of the console to keep the word "
          "as a secret...")
    time.sleep(10)
    correct_guess = []
    current_state = ""
    len_word = len(word_to_guess)

    # initialize hangman screen
    draw_hanger(hanger)
    title.clear()
    title.goto(250, 100)
    title.write("Save the Hangman!", move=False, align="center", font=("Rockwell", 35, "normal"))
    message.clear()
    message.goto(250, 0)
    life_left.write("Life left: " + str(life), move=False, align="center", font=("Rockwell", 20, "normal"))
    wn.update()
    turtle.tracer(1)

    # print the initial state, show how many letters there are by using an underscore
    print("There are " + str(len_word) + " letters in the word.")
    for i in range(len_word):
        current_state += "_ "
        print("_", end=" ")
    word.write(current_state, move=False, align="center", font=("Rockwell", 35, "normal"))
    print()

    # allows player 2 to guess the letters again and again until life==0 or whole word was guessed correctly
    while count_unique_char(word_to_guess) != len(correct_guess):
        # ask player 2 for a guess
        print(player2 + ": You have " + str(life) + " life left.")
        guessing = input(player2 + ": Please guess a letter: ")
        current_state = ""

        # if the letter that player 2 guess is in word_to_guess and not already in correct_guess list, append it
        # to list
        for i in range(len_word):
            if guessing == word_to_guess[i]:
                if guessing not in correct_guess:
                    correct_guess.append(guessing)

        # print the updated state, show position of letters correctly guessed using the correct_guess list
        for i in range(len_word):
            guessed = False
            for j in range(len(correct_guess)):
                if word_to_guess[i] == correct_guess[j]:
                    guessed = True
            if guessed:
                current_state += word_to_guess[i] + " "
                print(word_to_guess[i], end=" ")
            else:
                current_state += "_ "
                print("_", end=" ")
        word.clear()
        word.write(current_state, move=False, align="center", font=("Rockwell", 35, "normal"))

        # if player 2 guessed wrongly, minus 1 life and update the screen correspondingly
        if guessing not in correct_guess:
            life -= 1
            life_left.clear()
            life_left.write("Life left: " + str(life), move=False, align="center", font=("Rockwell", 20, "normal"))
            wn.update()
            if mode == "easy":
                if life == 8:
                    draw_head(hm)
                elif life == 7:
                    draw_eyes(hm)
                elif life == 6:
                    draw_mouth(hm)
                elif life == 5:
                    draw_upper_body(hm)
                elif life == 4:
                    draw_lower_body(hm)
                elif life == 3:
                    draw_right_hand(hm)
                elif life == 2:
                    draw_left_hand(hm)
                elif life == 1:
                    draw_right_leg(hm)
                elif life == 0:
                    draw_left_leg(hm)
            elif mode == "medium":
                if life == 6:
                    draw_head(hm)
                elif life == 5:
                    draw_eyes(hm)
                    draw_mouth(hm)
                elif life == 4:
                    draw_upper_body(hm)
                    draw_lower_body(hm)
                elif life == 3:
                    draw_right_hand(hm)
                elif life == 2:
                    draw_left_hand(hm)
                elif life == 1:
                    draw_right_leg(hm)
                elif life == 0:
                    draw_left_leg(hm)
            elif mode == "hard":
                if life == 3:
                    draw_head(hm)
                    draw_eyes(hm)
                    draw_mouth(hm)
                elif life == 2:
                    draw_upper_body(hm)
                    draw_lower_body(hm)
                elif life == 1:
                    draw_right_hand(hm)
                    draw_left_hand(hm)
                elif life == 0:
                    draw_right_leg(hm)
                    draw_left_leg(hm)
        print()

        # if no more life left, player 1 wins, and end the game
        if life == 0:
            title.clear()
            title.write("Hangman Died :(", move=False, align="center", font=("Rockwell", 35, "normal"))
            message.write(player1 + " Wins!", move=False, align="center", font=("Rockwell", 50, "normal"))
            word.clear()
            word.write("correct word: " + word_to_guess, move=False, align="center",
                       font=("Rockwell", 20, "normal"))
            hm.pencolor("LightCyan2")
            draw_eyes(hm)
            hm.pencolor("dim gray")
            draw_dead_eyes(hm)
            print("No more lives left...")
            print(player1 + " Wins!")
            print("The correct word is " + word_to_guess + ".")
            turtle.done()
            return
    else:
        # if all letters are guessed correctly, player 2 wins, and end the game
        message.write(player2 + " Wins!", move=False, align="center", font=("Rockwell", 45, "normal"))
        print(player2 + " Wins!")
        turtle.done()


hangman()
