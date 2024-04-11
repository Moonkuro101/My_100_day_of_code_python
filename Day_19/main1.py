from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make Your bet", "Which turtle will win ?").lower()
is_race_on = False
color = ['red','blue','green','purple','orange','yellow']
y_coodinates = [-100,-70,-40,-10,20,50,80]
all_turtle = []
for index in range(0,6):
    tim = Turtle(shape='turtle')
    tim.color(color[index])
    tim.penup()
    tim.goto(x=-230,y=y_coodinates[index])
    all_turtle.append(tim)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print('You won the bet')
            else:
                print(f'You lost the bet the winner is {winning_color}')
        random_distance = random.randint(0,100)
        turtle.fd(random_distance)
screen.exitonclick()