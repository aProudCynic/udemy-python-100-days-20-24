from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, start_position, text, alignment):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.setposition(start_position)
        self.alignment = alignment
        self.text = text
        self.score = 0
        self._write_score()

    def set_score(self, score: int):
        self.score = score
        self._write_score()

    def _write_score(self):
        self.clear()
        self.write(f'{self.text}: {self.score}', align=self.alignment, font=('Arial', 24))

    def display_game_finished_message(self):
        self.clear()
        self.write(f'Game over! {self.text}: {self.score}', align=self.alignment, font=('Arial', 24))