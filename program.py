from instruction import Instruction

import random
from uuid import uuid4
from typing import List, Dict
import numpy as np
from parameters import Parameters

class Program:
    def __init__(self):
        self.id: UUID = uuid4()
        self.registers: np.array = np.zeros(Parameters.NUM_REGISTERS)
        self.action: str = random.choice(Parameters.ACTIONS)
        self.instructions: List[Instruction] = []

        # Generate a list of instructions ranging from 1 to the maximum number of instructions
        for _ in range(random.randint(1, Parameters.MAX_INSTRUCTION_COUNT)):
            self.instructions.append(Instruction())

    def __str__(self) -> str:
        header: str = f"Program {self.id}:\n"
        instructions: str = '\n'.join(map(str, self.instructions))
        return f"{header}{instructions}"

    def __hash__(self) -> int:
        return hash(str(self))
    
    def execute(self, state: np.array) -> None:
        for instruction in self.instructions:
            instruction.execute(state, self.registers)

    def bid(self, state: np.array) -> Dict[float, str]:
        self.execute(state)
        
        return {
            "confidence": self.registers[0],
            "action": self.action
        }
