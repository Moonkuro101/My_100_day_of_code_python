import random
from turtle import Turtle, Screen
def random_color():
    R = random.random()
    G = random.random()
    B = random.random()
    turtle.color(R, G, B)

def path():
    path = [0,90,180,270]
    return path

def move():
    Turtle_choice = random.choice(path())
    turtle.setheading(Turtle_choice)
    turtle.forward(20)

# def draw_shape(num_shape):
#     angle = 360 / num_shape
#     for _ in range(num_shape):
#         Timmy.forward(100)
#         Timmy.right(angle)

turtle = Turtle()
turtle.shape('turtle')
turtle.pensize(2)
turtle.speed(0)
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        random_color()
        turtle.circle(100)
        turtle.setheading(turtle.heading()+size_of_gap)
draw_spirograph(5)





# for i in range(100):
#     random_color()
#     move()

# for i in range(15):
#     Timmy.pendown()
#     Timmy.color('black')
#     Timmy.forward(10)
#     Timmy.penup()
#     Timmy.forward(10)


# for num_of_side in range(3,11):
#     Timmy.color(random_color())


screen = Screen()
screen.exitonclick()

