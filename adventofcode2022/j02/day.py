import sys
import typing as T
from dataclasses import dataclass

SCORES = dict(A=1, B=2, C=3)
# X = ROCK
# Y = Paper
# Z = SCISSOR
# X > Z
# Z > Y
# Y > X

ROUND_SCORE = {
    "A": {
        "A": 3,
        "B": 0,
        "C": 6,
    },
    "B": {
        "A": 6,
        "B": 3,
        "C": 0,
    },
    "C": {
        "A": 0,
        "B": 6,
        "C": 3,
    },
}


@dataclass
class RockPaperScissor:
    input: str

    @property
    def score(self):
        return SCORES[self.input]


@dataclass
class SmartRockPaperScissor:
    instruction: str
    elve: RockPaperScissor

    @property
    def played(self):
        elve_scoring = ROUND_SCORE[self.elve.input]
        if self.instruction == "X":
            played = max(elve_scoring, key=elve_scoring.get)
        elif self.instruction == "Y":
            played = self.elve.input
        else:
            played = min(elve_scoring, key=elve_scoring.get)
        return played

    @property
    def score(self):
        return SCORES[self.played]


@dataclass
class Round:
    elve: RockPaperScissor
    me: SmartRockPaperScissor

    @property
    def total_score(self):
        return self.me.score + self.score

    @property
    def score(self):
        return ROUND_SCORE[self.me.played][self.elve.input]


def build_strategic_plan(path: str) -> T.List[Round]:
    plan = []
    with open(path, "r") as input:
        for line in input:
            elve, instruction = line.strip("\n").split(" ")
            elve_played = RockPaperScissor(elve)
            plan.append(Round(elve_played, SmartRockPaperScissor(instruction, elve_played)))
    return plan


if __name__ == "__main__":
    path = sys.argv[1]
    plan = build_strategic_plan(path)
    print(sum([r.total_score for r in plan]))
