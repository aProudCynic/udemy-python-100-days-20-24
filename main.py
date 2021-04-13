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
        self.turning = False

    def move_forward(self):
        for segment in self.segments:
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
        opposite_of_current_heading = 180 - int(self.segments[0].heading())
        if not self.turning and opposite_of_current_heading != new_heading:
            self.turning = True
            for segment_number in range(len(self.segments)):
                self.segments[segment_number].setheading(new_heading)
                for segment in self.segments:
                    segment.forward(Snake.SNAKE_SEGMENT_SIZE)
                screen.update()
                time.sleep(1)
            self.turning = False


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
    snake.move_forward()
    screen.update()
    time.sleep(1)

screen.exitonclick()

