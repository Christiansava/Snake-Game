from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # Initialize snake object
    def __init__(self):
        # Define segment list that will store all segments of the snake.
        self.segments = []
        # Call create_snake() function that allows us to create the initial snake.
        self.create_snake()
        # Define head variable that will store the head of teh snake.
        self.head = self.segments[0]

    # Define create snake function.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Define add_segment() function that will allow us to automate the snake creation and increase.
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Function that makes the snake move
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=x_cor, y=y_cor)

        self.head.forward(MOVE_FORWARD)

    # Extend function that allows us to increase the snake.
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Move Up.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    # Move Down.
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    # Move Left.
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    # Move Right.
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
