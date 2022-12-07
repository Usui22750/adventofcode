import sys
import typing as T

class Node:
    name: str
    children: dict()
    parent: T.Optional["Node"]
    size: int
    type: str

    def __init__(self, name, type, size, parent=None):
        self.parent = parent
        self.children = dict()
        self.type = type
        self.size = int(size)
        self.name = name
    def get_size(self):
        size = self.size
        for node in self.children.values():
            size += node.get_size()
        return size
    def add_node(self, type, name, size=0):
        self.children[name] = Node(name, type, size, self)

    def get_sub_directories(self):
        if self.type != "dir":
            return []
        sub = [self]
        for child in self.children.values():
            if child.type == "dir":
                sub.extend(child.get_sub_directories())
        return sub

    def cd(self, node_name):
        if node_name == "..":
            return self.parent
        return self.children[node_name]

def build_fs(path: str, root: Node):
    current_node = root
    with open(path, "r") as input:
        for line in input:
            line = line.strip("\n")
            instr = line.split(" ")
            if line[0] == "$":
                if instr[1] ==  "cd":
                    if instr[2] == "/":
                        current_node = root
                    else:
                        current_node = current_node.cd(instr[2])
                if instr[1] == "ls":
                    continue
            else:
                if instr[0] == "dir":
                    current_node.add_node("dir", instr[1])
                else:
                    current_node.add_node("file", instr[1], int(instr[0]))



if __name__ == "__main__":
    path = sys.argv[1]
    root = Node(name="/", type="dir", size=0)
    build_fs(path, root)
    root_size = root.get_size()
    directories = [a for a in root.get_sub_directories()]
    print(sum([a.get_size() for a in filter(lambda d: d.get_size() < 100_000, directories)]))
    disk_space = 70000000
    print(root_size)
    free_space = disk_space - root_size
    unused_space = 30000000
    min_free_space = unused_space - free_space
    print(f"free: {free_space}")
    print(f"to free: {min_free_space}")
    print(min([a.get_size() for a in filter(lambda d: d.get_size() > min_free_space, directories)]))
