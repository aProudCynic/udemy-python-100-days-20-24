from random import randint
from scoreboard import Scoreboard
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

def generate_random_coordinate_in_game_arena() :
        max_coordinate = ARENA_WIDTH_AND_HEIGHT / 2 / COORDINATE_SIZE - 1
        min_coordinate = max_coordinate * -1
        return randint(min_coordinate, max_coordinate) * COORDINATE_SIZE

def generate_food(number_of_food):
    foods = []
    
    for _ in range(number_of_food):
        coordinates_of_food = (
            float(generate_random_coordinate_in_game_arena()),
            float(generate_random_coordinate_in_game_arena()),
        )
        foods.append(Food(coordinates_of_food))
    return foods

def detect_game_ending_collision(snake, foods):
    if _detect_collision_with_walls(snake):
        return True
    return _detect_collision_of_snake_with_itself(snake)

def calculate_score(snake):
    return len(snake.segments) - Snake.SNAKE_DEFAULT_INITIAL_SEGMENTS

def consume_food_at_head(snake, foods):
    for food in foods:
        if snake.segments[0].distance(food) <= COORDINATE_SIZE / 2:
            food.hideturtle()
            snake.grow()

def _detect_collision_with_walls(snake):
    head_position = snake.segments[0].position()
    upper_boundary = ARENA_WIDTH_AND_HEIGHT / 2 - COORDINATE_SIZE
    lower_boundary = upper_boundary * -1
    for coordinate in head_position:
        if coordinate > upper_boundary or coordinate < lower_boundary:
            return True
    return False

def _detect_collision_of_snake_with_itself(snake):
    snake_segments = snake.segments
    snake_head_coordinates = snake_segments[0].position()
    for segment_index in range(1, len(snake_segments) -1):
        if snake_segments[segment_index].position() == snake_head_coordinates:
            return True
    return False

screen = Screen()
screen.bgcolor('black')
screen.setup(ARENA_WIDTH_AND_HEIGHT, ARENA_WIDTH_AND_HEIGHT)

screen.tracer(0)

snake = Snake()

foods = generate_food(5)

add_event_listeners(screen, snake)

game_on = True
scoreboard = Scoreboard()
while game_on:
    snake.move()
    screen.update()
    game_on = not detect_game_ending_collision(snake, foods)
    consume_food_at_head(snake, foods)
    current_score = calculate_score(snake)
    scoreboard.set_score(current_score)
    time.sleep(0.2)

screen.exitonclick()

