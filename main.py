from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
WIDTH = 600
HEIGHT = 600


# Define Screen dimensions and characteristics
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

# Define snake object
snake = Snake()

# Prepare screen to listen to keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Initialize food
food = Food()

# Initialize Score Board
score = ScoreBoard()

game_is_on = True

# While loop that allows us to play the game until is game over.
while game_is_on:
    # Reduce the speed to allow us to see the snake moving.
    time.sleep(0.1)
    # Update screen.
    screen.update()
    # Call the function that allows the snake to move.
    snake.move()

    # If we eat a food we will refresh the food location, increase the score and extend the snake.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Conditions to see if the head has reached a wall. If yes, then we call game over function to finish the game.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # Condition to see if teh head has hit a part of the tail. If yes, then it is game over as well.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

# Screen closes on click.
screen.exitonclick()
