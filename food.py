from constants import ARENA_WIDTH_AND_HEIGHT, COORDINATE_SIZE
from turtle import Turtle
from random import randint

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