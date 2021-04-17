from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.setposition(0, 270)
        self.displayed_score = 0
        self._write_score()

    def set_score(self, score: int):
        self.displayed_score = score
        self._write_score()

    def _write_score(self):
        self.clear()
        self.write(f'Score: {self.displayed_score}', align='center', font=('Arial', 24))

    def display_game_finished_message(self):
        self.clear()
        self.write(f'Game over! Score: {self.displayed_score}', align='center', font=('Arial', 24))