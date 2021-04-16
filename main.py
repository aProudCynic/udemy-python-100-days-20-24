from snake import Snake
from food import Food
from constants import ARENA_WIDTH_AND_HEIGHT, COORDINATE_SIZE
from turtle import Screen
import time

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
        if snake.segments[0].distance(food) <= COORDINATE_SIZE / 2:
            food.hideturtle()
            snake.grow()

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

