from turtle import Turtle, Screen

class Snake:
    def __init__(self, nr_of_segments):
        self.segments = []
        for segment_number in range(nr_of_segments):
            segment = Turtle()
            segment.shape('square')
            segment.color('white')
            segment.penup()
            if(segment_number != 0):
                segment.back(20 * segment_number)
            self.segments.append(segment)

    def move_forward(self):
        for segment in self.segments:
            segment.forward(20)

screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)

snake = Snake(3)
game_on = True
while game_on:
    snake.move_forward()

screen.exitonclick()

