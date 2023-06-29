from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ariel", 20, "normal")
X_COR = 0
Y_COR = 270


class ScoreBoard(Turtle):
    # Initialize class with all settings to create the scoreboard.
    def __init__(self):
        super().__init__()
        # Initial score.
        self.score = 0
        # Color of object
        self.color("white")
        # We do not need to draw anything.
        self.penup()
        # We need to hide the object (turtle).
        self.hideturtle()
        # Position the score board on top of the screen.
        self.goto(x=X_COR, y=Y_COR)
        self.define_score()

    # Define score by using the write function.
    def define_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Increase score when the food is eaten.
    def increase_score(self):
        self.score += 1
        self.clear()
        self.define_score()

    # Finish game when colliding with wall or with tail.
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)
