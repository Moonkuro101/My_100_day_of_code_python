from turtle import Turtle,Screen,clear
screen = Screen()
tim = Turtle()
# def forwards():
#     tim.forward(10)
# screen.listen()
# screen.onkey( key='space', fun=forwards )
def for_wards():
    tim.fd(10)
def back_wards():
    tim.backward(50)
def counter_clockwise():
    tim.setheading(tim.heading()+10)
def clockwise():
    tim.setheading(tim.heading()-10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
screen.onkey(for_wards, "w")
screen.onkey(back_wards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")


screen.listen()
screen.exitonclick()
