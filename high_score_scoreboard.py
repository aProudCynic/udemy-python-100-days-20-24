from scoreboard import Scoreboard


class HighScoreScoreboard(Scoreboard):

    HIGH_SCORE_FILE = 'data.txt'

    def __init__(self, start_position, alignment):
        super().__init__(start_position, 'High score', alignment)
        with open(HighScoreScoreboard.HIGH_SCORE_FILE, mode='r') as high_score_file:
            high_score_from_file = int(high_score_file.read())
            # TODO this will save it again
            self.set_score(high_score_from_file)

    def set_score(self, score: int):
        super().set_score(score)
        self.save_new_high_score(score)

    def save_new_high_score(self, score):
        with open(HighScoreScoreboard.HIGH_SCORE_FILE, mode='w') as high_score_file:
            high_score_file.write(str(score))