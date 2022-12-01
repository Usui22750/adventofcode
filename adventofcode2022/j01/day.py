import sys
from dataclasses import dataclass


@dataclass
class Elves:
    fruits: []
    total: int

    def __repr__(self):
        return f"total calories {self.total}"


elves = []


def build_sort_elves(path):
    with open(path, "r") as input:
        calories = []
        for line in input:
            if line == "\n":
                elves.append(Elves(fruits=calories, total=sum(calories)))
                calories = []
                continue
            value = int(line)
            calories.append(value)
    sort_elves = sorted(elves, key=lambda o: o.total, reverse=True)
    return sort_elves


if __name__ == "__main__":
    path = sys.argv[1]
    sort_elves = build_sort_elves(path)
    print(sort_elves[0])
    print(sum([e.total for e in sort_elves[0:3]]))
