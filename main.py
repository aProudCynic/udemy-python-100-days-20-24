from turtle import Turtle, Screen

class Snake:

    SNAKE_SEGMENT_SIZE = 20

    def __init__(self, nr_of_segments):
        self.segments = []
        for segment_number in range(nr_of_segments):
            segment = Turtle()
            segment.shape('square')
            segment.color('white')
            segment.penup()
            if(segment_number != 0):
                segment.back(Snake.SNAKE_SEGMENT_SIZE * segment_number)
            self.segments.append(segment)

    def move_forward(self):
        for segment in self.segments:
            segment.forward(Snake.SNAKE_SEGMENT_SIZE)

    def turn_left(self):
        for segment_number in range(len(self.segments)):
            self.segments[segment_number].left(90)
            for segment in self.segments:
                segment.forward(Snake.SNAKE_SEGMENT_SIZE)

screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)

screen.tracer(0)

snake = Snake(3)

game_on = True
while game_on:
    snake.move_forward()
    screen.update()

screen.exitonclick()

