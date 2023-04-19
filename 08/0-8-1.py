import numpy as np
import re
import string
import pprint

file = open('C:/Users/Niels/source/repos/aoc-2020/0-8-1/input.txt').readlines()
file = [l.strip() for l in file]


class GameConsole:

    def __init__(self, program):
        self.program = program
        self.program_ptr = 0
        self.acc = 0

        self.history = []

        self.create_function_map()

    def create_function_map(self):
        self.program_map = { 
            "acc": self.modify_accumulator,
            "jmp": self.ptr_jump,
            "nop": self.no_operation
        }

    def modify_accumulator(self, args):
        for arg in args:
            self.acc += arg

    def ptr_jump(self, args):
        for arg in args:
            # - 1 because ptr is increased at the end of every instruction anyway.
            self.program_ptr += arg - 1

    def no_operation(self, args):
        return


    # Executes instruction at program_ptr and increments ptr
    def step(self):
        # Exit condition
        if self.program_ptr in self.history:
            return False

        self.history.append(self.program_ptr)
        instruction, args = self.parse_instruction(self.program[self.program_ptr])
        
        self.program_map[instruction](args)

        self.program_ptr += 1

        return True

    def parse_instruction(self, line):
        spl = line.split()
        
        return spl[0], [int(arg) for arg in spl[1:]]


console = GameConsole(file)
i = 0
while console.step():
    i += 1

print(console.acc)