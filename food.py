from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle") # Use a circle shape
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7) # Slightly larger food
        self.color("red") # A contrasting color for food
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Moves the food to a new random location."""
        # Ensure food stays well within the visible game area
        random_x = random.randint(-280, 280) # Increased range for food
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)