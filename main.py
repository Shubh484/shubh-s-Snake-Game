from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

# Detect collison with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# Detect collision with wall
    if snake.head.xcor() < -295 or snake.head.xcor() > 295 or snake.head.ycor() < -295 or snake.head.ycor() > 295 :
        game_is_on = False
        scoreboard.game_over()


# Detect collision with tail

    for segment in snake.segments :
        if segment == snake.head :
            pass
        elif snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()