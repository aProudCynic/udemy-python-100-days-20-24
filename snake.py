from constants import COORDINATE_SIZE
from turtle import Turtle

class Snake:

    SNAKE_DEFAULT_INITIAL_SEGMENTS = 3

    def __init__(self, nr_of_segments = SNAKE_DEFAULT_INITIAL_SEGMENTS):
        self.segments = []
        for segment_number in range(nr_of_segments):
            segment = Turtle()
            segment.shape('square')
            segment.color('white')
            segment.penup()
            if(segment_number != 0):
                segment.back(COORDINATE_SIZE * segment_number)
            self.segments.append(segment)

    def move(self):
        for segment_number in range(len(self.segments) - 1, -1, -1):
            segment = self.segments[segment_number]
            if segment_number > 0:
                previous_segment = self.segments[segment_number - 1]
                segment.goto(previous_segment.position())
                segment.setheading(previous_segment.heading())
            else:
                segment.forward(COORDINATE_SIZE)

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

    def grow(self):
        last_segment = self.segments[len(self.segments) - 1]
        new_segment = last_segment.clone()
        new_segment.back(COORDINATE_SIZE)
        self.segments.append(new_segment)