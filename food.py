from turtle import Turtle
import random
FOOD_COLOR = "blue"


class Food(Turtle):
    # Initialize food object.
    def __init__(self):
        super().__init__()
        # The food has a circular shape.
        self.shape("circle")
        # We do not need to draw anything.
        self.penup()
        # Define the color of the food.
        self.color(FOOD_COLOR)
        # Define the shape of the food.
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        # Call refresh() function to generate new coordinates for the food.
        self.refresh()

    # Generate new coordinates for the food and add the food to the screen.
    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x=x_cor, y=y_cor)
