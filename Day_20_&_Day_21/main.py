import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreborad import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)
snake = Snake()
screen.update()
food = Food()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

score_board = ScoreBoard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # Detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score_board.game_over()
    #dectect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
    #if head collision with any segment in the tail
        #trigger game over

screen.exitonclick()