from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Press Start 2P", 18, "normal") # A more pixel-art friendly font

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 260) # Slightly lower for better visibility with high score
        self.hideturtle()
        self.update_scoreboard()

    def load_high_score(self):
        """Loads the high score from a file."""
        try:
            with open("data.txt") as data:
                return int(data.read())
        except FileNotFoundError:
            with open("data.txt", "w") as data:
                data.write("0")
            return 0
        except ValueError: # Handle cases where data.txt might be empty or malformed
            with open("data.txt", "w") as data:
                data.write("0")
            return 0

    def save_high_score(self):
        """Saves the current high score to a file."""
        with open("data.txt", "w") as data:
            data.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """Resets the score and updates high score if applicable."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.clear() # Clear the "GAME OVER" message if it was displayed
        self.goto(0, 260) # Move back to score position
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        self.goto(0, -30)
        self.write("Press 'R' to Play Again", align=ALIGNMENT, font=("Press Start 2P", 14, "normal"))
        self.reset() # Call reset to update high score if current score is higher