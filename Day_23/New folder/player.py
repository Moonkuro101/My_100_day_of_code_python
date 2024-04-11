STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape('turtle')
        self.penup()
        self.reset_position()

    def move(self):
        self.fd(MOVE_DISTANCE)
    
    def reset_position(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() >= 280:
            self.reset_position()
            return True
        else :
            return False


        
