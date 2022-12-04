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


class RuckSacks:
    compartment_1: str
    compartment_2: str
    item_set_1: set
    item_set_2: set


    def __init__(self, all: str):
        x = len(all)
        mid = int(x/2)
        self.compartment_1 = all[0:mid]
        self.compartment_2 = all[mid:x]
        self.item_set_1 = set([a for a in self.compartment_1])
        self.item_set_2 = set([a for a in self.compartment_2])
        self.item_set = set([a for a in all])

    @property
    def common(self):
        return self.item_set_1 & self.item_set_2

    def badge(self, other):
        return self.item_set & other.item_set


def build_ruksacks(path: str) -> T.List[RuckSacks]:
    bags = []
    groups = []
    with open(path, "r") as input:
        for line in input:
            items = line.strip("\n")
            bags.append(RuckSacks(items))
            if len(bags) == 3:
                groups.append(bags)
                bags = []
    return groups


if __name__ == "__main__":
    path = sys.argv[1]
    groups = build_ruksacks(path)
    badges = []
    for group in groups:
        common = group[0].badge(group[1]) & group[0].badge(group[2]) & group[1].badge(group[2])
        badges.append(list(set(common))[0])
    print(sum([priorities[c] for c in badges]))
