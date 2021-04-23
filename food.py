from typing import Tuple
from turtle import Turtle

class Food(Turtle):

    def __init__(self, coordinates: Tuple) -> None:
        super().__init__(shape='circle')
        self.color('blue')
        self.penup()
        self.setposition(coordinates)
