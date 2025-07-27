from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# --- Screen Setup ---
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)  # Turn off screen updates for manual control

# --- Game Objects ---
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# --- Game State Variables ---
game_is_on = False # Start with game off, waiting for user to begin
game_speed = 0.1 # Initial delay for smoother movement

# --- Event Listeners ---
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(scoreboard.reset, "r") # 'R' key to reset/play again
screen.onkey(lambda: start_game(screen, scoreboard, snake, food), "space") # Space to start

# --- Start Screen Message ---
start_message = Turtle()
start_message.hideturtle()
start_message.penup()
start_message.color("white")
start_message.goto(0, 0)
start_message.write("Press SPACE to Start", align="center", font=("Courier", 24, "normal"))
start_message.goto(0, -30)
start_message.write("Press 'R' at Game Over to Play Again", align="center", font=("Courier", 14, "normal"))

def start_game(screen_obj, sb_obj, snake_obj, food_obj):
    """Initializes and starts the game."""
    global game_is_on, game_speed
    if not game_is_on: # Only start if not already running
        start_message.clear() # Clear the start message
        sb_obj.reset() # Reset scoreboard and high score display
        snake_obj.reset_snake() # Reset snake position
        food_obj.refresh() # Place food
        game_is_on = True
        game_speed = 0.1 # Reset speed
        game_loop(screen_obj, sb_obj, snake_obj, food_obj)

def game_loop(screen_obj, sb_obj, snake_obj, food_obj):
    """The main game loop."""
    global game_is_on, game_speed

    if game_is_on:
        screen_obj.update()  # Update the screen after all movements
        time.sleep(game_speed)  # Control game speed

        snake_obj.move()

        # Detect collision with food
        if snake_obj.head.distance(food_obj) < 15:
            food_obj.refresh()
            snake_obj.extend()
            sb_obj.increase_score()
            # Increase game speed slightly for every few points
            if sb_obj.score % 5 == 0 and game_speed > 0.03: # Cap minimum speed
                game_speed -= 0.01

        # Detect collision with wall
        if (snake_obj.head.xcor() > 290 or snake_obj.head.xcor() < -290 or
                snake_obj.head.ycor() > 290 or snake_obj.head.ycor() < -290):
            game_is_on = False
            sb_obj.game_over()

        # Detect collision with tail
        for segment in snake_obj.segments[1:]:
            if snake_obj.head.distance(segment) < 10:
                game_is_on = False
                sb_obj.game_over()

        screen_obj.ontimer(lambda: game_loop(screen_obj, sb_obj, snake_obj, food_obj), 10) # Use ontimer for smoother loop

# Initial call to set up the screen, game starts on 'space' press
screen.update()
screen.exitonclick()