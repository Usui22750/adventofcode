import string
import typing as T
import sys

lower_priority = {
    k: ord(k) - ord('a') +1 for k in string.ascii_lowercase
}

upper_priority = {
    k: ord(k) - ord('A') + 27 for k in string.ascii_uppercase
}

priorities = lower_priority | upper_priority


class CleaningZone:
    start: int
    end: int
    sections = None

    def __init__(self, input):
        self.start, self.end = [int(a) for a in input.split('-')]
        self.sections = [a for a in range(self.start, self.end + 1)]

    def contains(self, other):
        if self.start <= other.start and self.end >= other.end:
            return True
        return False

    def overlap(self, other):
        if set(other.sections) & set(self.sections):
            return True
        return False

    def __repr__(self):
        return f"{self.start}-{self.end}"


def build_zone(path: str):
    count_contains = 0
    count_overlap = 0
    with open(path, "r") as input:
        for line in input:
            assignement = line.strip("\n")
            zones_ = assignement.split(",")
            zone_1 = CleaningZone(zones_[0])
            zone_2 = CleaningZone(zones_[1])
            if zone_1.contains(zone_2) or zone_1.contains(zone_2):
                count_contains += 1
                count_overlap += 1
            elif zone_1.overlap(zone_2):
                count_overlap += 1

    return count_contains, count_overlap


if __name__ == "__main__":
    path = sys.argv[1]
    count_contains, count_overlap = build_zone(path)
    print(count_contains)
    print(count_overlap)
