# Snake Game
import time
# Create Snake Body

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen = Screen()
screen.setup(width=1500, height=1000)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()
    # Detect collision from food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect Collision with Wall
    if snake.head.xcor() > 730 or snake.head.xcor() < -730 or snake.head.ycor() > 480 or snake.head.ycor() < -480:
        game_is_on = False
        scoreboard.game_over()
    # Detect collisions with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
