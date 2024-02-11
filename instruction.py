import random
import numpy as np
import math
from parameters import Parameters

class Instruction:
    def __init__(self): 
        """
        An instruction defines an operation on a program's registers.
        An instruction may be an addition, subtraction, multiplication, division, cosine, or negation.
        
        :return: A new instruction
        """

        # Defines whether the instruction should read from (program registers or the state/observation space).
        self.mode: str = random.choice(["INPUT", "REGISTERS"])

        # Defines what operation the instruction should execute.
        self.operation: str = random.choice(['+', '-', '*', '/', 'COS', 'NEGATE'])

        if self.mode == "INPUT":
            # Chooses the register the instruction uses as input from the program's registers.
            self.source: int = random.randint(0, Parameters.NUM_OBSERVATIONS - 1)
        elif self.mode == "REGISTERS":
            # Chooses the register the instruction uses as input from the observation/state space.
            self.source: int = random.randint(0, Parameters.NUM_REGISTERS - 1)
        
        # Chooses a register that the instruction should be applied to.
        self.destination: int = random.randint(0, Parameters.NUM_REGISTERS - 1)

    def __str__(self) -> str:
        """
        When the instruction is cast to a string it will return a human-readable format.

        :return: the instruction casted to a string.
        """
        address: str = "STATE" if self.operation == "INPUT" else "R"

        if self.operation == "COS":
            return f"R[{self.destination}] = COS({address}[{self.source}])"
        elif self.operation == "NEGATE":
            return f"IF (R[{self.destination}] < {address}[{self.source}]) THEN R[{self.destination}] = -R[{self.destination}]"
        else:
            return f"R[{self.destination}] = R[{self.destination}] {self.operation} {address}[{self.source}]"

    def __hash__(self) -> int:
        """
        If the hashes of two instructions match, then they are the same.
        
        This is used during mutation to ensure the mutated instruction
        is unique from the original instruction.

        :return: the instruction's hash
        """
        return hash((self.mode, self.operation, self.source, self.destination))

    def execute(self, state: np.array, registers: np.array) -> None:
        """
        Updates a program's registers after executing the instruction.
        If the instruction is a division by zero, the register is set to 0.
        If the instruction causes an overflow/underflow, the register is set to inf/-inf.

        :param state: the feature vector representing the state/observation
        :param registers: the registers belonging to the program executing the instruction
        """
        if self.mode == "INPUT":
            input = state
        elif self.mode == "REGISTERS":
            input = registers
        
        if self.operation == '+': 
            registers[self.destination] = registers[self.destination] + input[self.source]
        elif self.operation == "-":
            registers[self.destination] = registers[self.destination] - input[self.source]
        elif self.operation == "*":
            registers[self.destination] = registers[self.destination] * input[self.source]
        elif self.operation == "/":
            if input[self.source] != 0:
                registers[self.destination] = registers[self.destination] / input[self.source]
            else:
                registers[self.destination] = 0
        elif self.operation == "COS":
            registers[self.destination] = math.cos(input[self.source])
        elif self.operation == "NEGATE":
            if registers[self.destination] < input[self.source]:
                registers[self.destination] = -registers[self.destination]

        if registers[self.destination] == np.inf:
            registers[self.destination] = np.finfo(np.float64).max
        elif registers[self.destination] == np.NINF:
            registers[self.destination] = np.finfo(np.float64).min
