from turtle import Turtle,Screen
from random import randint as ri

screen_obj = Screen()
screen_obj.setup(width=1000,height=500)
screen_obj.bgcolor("black")

turtles_colors = ["red","orange","yellow","green","blue","purple"]
turtles_list = []
is_correct_option = False
turtles_positions = [-150, -90, -30, 30, 90, 150]

def start_the_race(user_guessed_color):

    is_game_over = False

    while not is_game_over:

        for i in turtles_list:

            if i.xcor() < 420:

                random_steps = ri(0, 10)
                i.forward(random_steps)

            else:

                is_game_over = True

                if user_guessed_color == i.pencolor():

                    print(f"YOU WON. '{i.pencolor()}' TURTLE WON THE RACE")

                else:
                    print(f"YOU LOST. YOU CHOSE '{user_guessed_color}' BUT '{i.pencolor()}' TURTLE WON THE RACE")


def refree():

    refree = Turtle(shape="arrow")
    refree.color("white")
    refree.pencolor("red")
    refree.pensize(4)
    refree.penup()
    refree.goto(x=450,y=0)
    refree.setheading(270)
    refree.forward(240)
    refree.setheading(90)
    refree.pendown()
    refree.forward(490)
    refree.hideturtle()

def arrange_the_turtles():

    for i in range(len(turtles_list)):

        turtles_list[i].goto(x=-450,y=turtles_positions[i])



def make_turtles(is_correct_option):

    user_guess = ""

    refree()

    for i in turtles_colors:

        tim = Turtle("turtle")
        tim.color(i)
        tim.penup()
        tim.shapesize(stretch_len=2,stretch_wid=2)
        turtles_list.append(tim)

    arrange_the_turtles()

    while not is_correct_option:

        user_guess = screen_obj.textinput(

            title="MAKE YOUR GUESS",
            prompt="WHICH COLOR OF TURTLE WILL WIN THE RACE?: "

        ).lower()

        if user_guess in turtles_colors:

            is_correct_option = True

        else:

            print(f"\nSORRY YOU HAVE CHOSEN THE INVALID OPTION, TRY AGAIN:")

    screen_obj.listen()
    screen_obj.title(titlestring="PRESS THE SPACEBAR KEY TO START THE RACE")
    screen_obj.onkey(lambda : start_the_race(user_guess),key="space")


make_turtles(is_correct_option=is_correct_option)


screen_obj.exitonclick()