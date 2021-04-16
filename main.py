from turtle import Turtle, Screen
import time
from random import randint

COORDINATE_SIZE = 20

ARENA_WIDTH_AND_HEIGHT = 600

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

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__(shape='circle')
        self.color('blue')
        self.penup()
        self.setposition(
            float(self._generate_random_coordinate_in_game_arena()),
            float(self._generate_random_coordinate_in_game_arena())
        )
        print(self.position())
        
    def _generate_random_coordinate_in_game_arena(self):
        max_coordinate = ARENA_WIDTH_AND_HEIGHT / 2 / COORDINATE_SIZE - 1
        min_coordinate = max_coordinate * -1
        return randint(min_coordinate, max_coordinate) * COORDINATE_SIZE

def add_event_listeners(screen, snake):
    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

def generate_food(number_of_food):
    foods = []
    for _ in range(number_of_food):
        foods.append(Food())
    return foods

def detect_collisions(snake, foods):
    for food in foods:
        print(food.position())
        if snake.segments[0].distance(food) <= COORDINATE_SIZE:
            food.hideturtle()

screen = Screen()
screen.bgcolor('black')
screen.setup(ARENA_WIDTH_AND_HEIGHT, ARENA_WIDTH_AND_HEIGHT)

screen.tracer(0)

snake = Snake()

foods = generate_food(5)

add_event_listeners(screen, snake)

game_on = True
while game_on:
    snake.move()
    screen.update()
    detect_collisions(snake, foods)
    time.sleep(0.2)

screen.exitonclick()

