from dataclasses import dataclass
import sys
import re

def build_stacks(lines):
    stacks = []
    number_of_stacks = re.findall(r'\d+', lines[-1])
    number_of_stacks = len(number_of_stacks)
    for _ in range(0, number_of_stacks):
        stacks.append([])
    del lines[-1]
    for line in lines:
        line = re.sub(r" (   )", lambda o: " [ ]", line)
        characters = re.findall(r"\[.]", line)
        print(characters)
        characters = [c[1] for c in characters]
        number_of_char = len(characters)
        for i in range(0, number_of_stacks):
            if i < number_of_char:
                char = characters[i]
                if char == " ":
                    char = None
            else:
                char = None
            if char:
                stacks[i].append(char)
    return stacks

@dataclass
class Instructions:
    number_of_item: int
    source: int
    destination: int

    def __init__(self, item, s, d):
        self.number_of_item = int(item)
        self.source = int(s)
        self.destination = int (d)
    def play(self, stacks):
        source = stacks[self.source - 1]
        to_move = source[:self.number_of_item]
        # first part uncomment
        # to_move = [a for a in reversed(to_move)]
        to_move.extend(stacks[self.destination - 1])
        stacks[self.destination - 1] = to_move
        stacks[self.source - 1] = source[self.number_of_item:]



def build_instructions(instructions):
    list_of_instruction = []
    for instruction in instructions:
        instr = re.findall(r'\d+', instruction)
        list_of_instruction.append(Instructions(*instr))
    return list_of_instruction

def parse_file(path):
    lines = []
    instructions = []
    current = lines
    with open(path, "r") as input:
        for line in input:
            if line == "\n":
                current = instructions
                continue
            current.append(line)
    stacks = build_stacks(lines)
    instructions = build_instructions(instructions)
    return stacks, instructions

if __name__ == "__main__":
    path = sys.argv[1]
    stacks, instructions = parse_file(path)
    print(stacks)
    for inst in instructions:
        inst.play(stacks)
    top_elt = []
    for stack in stacks:
        top_elt.append(stack[0])
    print("".join(top_elt))
