import random
import numpy as np
import math
from parameters import Parameters

class Instruction:
    def __init__(self): 
        self.mode: str = random.choice(["INPUT", "REGISTERS"])
        self.operation: str = random.choice(['+', '-', '*', '/', 'COS', 'NEGATE'])

        if self.mode == "INPUT":
            self.source: int = random.randint(0, Parameters.NUM_OBSERVATIONS - 1)
        elif self.mode == "REGISTERS":
            self.source: int = random.randint(0, Parameters.NUM_REGISTERS - 1)
            
        self.destination: int = random.randint(0, Parameters.NUM_REGISTERS - 1)

    def __str__(self) -> str:
        address: str = "STATE" if self.operation == "INPUT" else "R"

        if self.operation == "COS":
            return f"R[{self.destination}] = COS({address}[{self.source}])"
        elif self.operation == "NEGATE":
            return f"IF (R[{self.destination}] < {address}[{self.source}]) THEN R[{self.destination}] = -R[{self.destination}]"
        else:
            return f"R[{self.destination}] = R[{self.destination}] {self.operation} {address}[{self.source}]"

    def __hash__(self) -> int:
        return hash((self.mode, self.operation, self.source, self.destination))

    def execute(self, state: np.array, registers: np.array) -> None:
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
