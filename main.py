from turtle import Turtle, Screen
import time

class Snake:

    SNAKE_SEGMENT_SIZE = 20
    SNAKE_DEFAULT_INITIAL_SEGMENTS = 3

    def __init__(self, nr_of_segments = 3):
        self.segments = []
        for segment_number in range(nr_of_segments):
            segment = Turtle()
            segment.shape('square')
            segment.color('white')
            segment.penup()
            if(segment_number != 0):
                segment.back(Snake.SNAKE_SEGMENT_SIZE * segment_number)
            self.segments.append(segment)

    def move(self):
        for segment_number in range(len(self.segments) - 1, -1, -1):
            segment = self.segments[segment_number]
            if segment_number > 0:
                previous_segment = self.segments[segment_number - 1]
                segment.goto(previous_segment.position())
                segment.setheading(previous_segment.heading())
            else:
                segment.forward(Snake.SNAKE_SEGMENT_SIZE)

    def up(self):
        self.rotate(90)

    def left(self):
        self.rotate(180)

    def down(self):
        self.rotate(270)

    def right(self):
        self.rotate(360)

    def rotate(self, new_heading):
        head = self.segments[0]
        opposite_of_current_heading = 180 - int(head.heading())
        if opposite_of_current_heading != new_heading:
            head.setheading(new_heading)

screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)

screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    snake.move()
    screen.update()
    time.sleep(0.2)

screen.exitonclick()

