from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.current_direction = RIGHT # Keep track of current direction

    def create_snake(self):
        """Creates the initial snake segments."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment to the snake."""
        new_segment = Turtle("square")
        new_segment.color("limegreen") # Nicer color for the snake
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Adds a new segment to the end of the snake."""
        # Add a new segment at the position of the last segment
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake forward."""
        # Move all segments from tail to head to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Move the head forward
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        """Resets the snake to its initial state for a new game."""
        for seg in self.segments:
            seg.goto(1000, 1000) # Move segments off-screen
            seg.clear()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.current_direction = RIGHT # Reset to initial direction

    # Direction controls, preventing immediate reverse turns
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.current_direction = UP

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.current_direction = DOWN

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.current_direction = LEFT

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.current_direction = RIGHT