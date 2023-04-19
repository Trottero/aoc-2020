import numpy as np

file = open('C:/Users/Niels/source/repos/aoc-2020/0-8-1/input.txt').readlines()
file = [l.strip() for l in file]


class GameConsole:
    """
        Exit codes:
        0: Normal exit
        1: Normal step
        2: Exit with loop
    """

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
        # Regular exit condition
        if self.program_ptr >= len(self.program):
            return 0

        # Looping exit condition
        if self.program_ptr in self.history:
            return 2

        self.history.append(self.program_ptr)
        instruction, args = self.program[self.program_ptr]
        
        self.program_map[instruction](args)

        self.program_ptr += 1

        return 1

    def parse_instruction(line):
        spl = line.split()
        
        return spl[0], [int(arg) for arg in spl[1:]]


program = [GameConsole.parse_instruction(l) for l in file]

i = 0

switch_map = {
    "nop": "jmp",
    "jmp": "nop"
}

for index, tuple in enumerate(program):
    instruction, args = tuple
    if instruction == "nop" or instruction == "jmp":
        instruction = switch_map[instruction]
        mod_program = program.copy()
        mod_program[index] = (instruction, args)

        # Test the new program
        console = GameConsole(mod_program)
        
        exit_code = 1
        while exit_code == 1:
            exit_code = console.step()
            if exit_code == 0: # Normal exit
                print(console.acc)
                exit()