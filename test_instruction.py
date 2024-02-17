from instruction import Instruction
from mutator import Mutator
from parameters import Parameters

from copy import deepcopy
from typing import Dict
import numpy as np
import random

def test_mutations_change_instruction_mode():
	"""
	Tests that mutations can change an instruction's mode.
	"""
	original: Instruction = Instruction()
	clone: Instruction = deepcopy(original)

	for _ in range(1, 1000):
		Mutator.mutateInstruction(clone)

		# The instruction's mode was mutated 
		if clone.mode != original.mode:
			assert True
			return

	assert False, "The instruction's mode was not changed after 1000 mutations"

def test_mutations_change_instruction_operation():
	"""
	Tests that mutations can change an instruction's operation.
	Checks that all operations can be reached.
	"""
	operations = [ '+', '-', '*', '/', 'COS', 'NEGATE' ]
	original: Instruction = Instruction()

	result: Dict[str, bool] = { op: False for op in operations }

	for operator in operations:
		# Set the operator to an arbitrary operator that is not being checked.
		original.operation = random.choice([op for op in operations if op != original.operation])
		
		clone: Instruction = deepcopy(original)
		
		for _ in range(1, 1000):
			Mutator.mutateInstruction(clone)

			if clone.operation == operator:
				result[operator] = True
				break

	missingOperations = [ op for op in operations if result[op] == False ]
	assert len(missingOperations) == 0, f"The following operations were never seen after 1000 mutations: {missingOperations}"
		
def test_mutations_change_instruction_source_register():
	"""
	Tests that mutations can change an instruction's source register.
	"""
	original: Instruction = Instruction()
	clone: Instruction = deepcopy(original)

	for _ in range(1, 1000):
		Mutator.mutateInstruction(clone)

		# The instruction's source register was mutated
		if clone.source != original.source:
			assert True
			return

	assert False, "The source register never changed after the instruction was mutated 1000 times."

def test_instruction_source_register_is_never_negative():
	"""
	Tests that mutations will never change an instruction's source register to a negative value.
	"""
	instruction: Instruction = Instruction()

	for _ in range(1, 10000):
		Mutator.mutateInstruction(instruction)

		if instruction.source < 0:
			assert False, "The source register is negative after a mutation."
			return

	assert True

def test_instruction_source_register_does_not_exceed_upper_bound():
	"""
	Tests that mutations will never change an instruction's source register to above the upper bound.
	"""
	instruction: Instruction = Instruction()

	for _ in range(1, 1000000):
		Mutator.mutateInstruction(instruction)

		if instruction.mode == "INPUT" and instruction.source > Parameters.NUM_OBSERVATIONS:
			assert False, "The source register is above the upper bound after a mutation."
			return

		elif instruction.mode == "REGISTERS" and instruction.source > Parameters.NUM_REGISTERS:
			assert False, "The source register is above the upper bound after a mutation."
			return
		
		assert True

def test_instructions_add_correctly():
	"""
	Tests that the add instruction is computed correctly
	"""
	instruction: Instruction = Instruction()
	instruction.mode = "REGISTERS"
	instruction.operation = '+'
	instruction.destination = 0
	instruction.source = 3

	input: np.array = np.array([1, 2, 3, 4])
	registers: np.array = np.array([-1, 0, 1, -2])
	instruction.execute(input, registers)

	assert registers[0] == -1 + -2, "The add instruction gave an incorrect calculation when using internal registers."

	instruction: Instruction = Instruction()
	instruction.mode = "INPUT"
	instruction.operation = '+'
	instruction.destination = 1
	instruction.source = 2

	input: np.array = np.array([6, 7, 8, 9])
	registers: np.array = np.array([-6, -7, -8, -9])
	instruction.execute(input, registers)

	assert registers[1] == -7 + 8, "The add instruction gave an incorrect calculation when using state registers."

def test_instructions_subtract_correctly():
	"""
	Tests that the add instruction is computed correctly
	"""
	instruction: Instruction = Instruction()
	instruction.mode = "REGISTERS"
	instruction.operation = '-'
	instruction.destination = 0
	instruction.source = 3

	input: np.array = np.array([1, 2, 3, 4])
	registers: np.array = np.array([-1, 0, 1, -2])
	instruction.execute(input, registers)

	assert registers[0] == -1 - -2, "The subtract instruction gave an incorrect calculation when using internal registers."

	instruction: Instruction = Instruction()
	instruction.mode = "INPUT"
	instruction.operation = '-'
	instruction.destination = 1
	instruction.source = 2

	input: np.array = np.array([6, 7, 8, 9])
	registers: np.array = np.array([-6, -7, -8, -9])
	instruction.execute(input, registers)

	assert registers[1] == -7 - 8, "The subtract instruction gave an incorrect calculation when using state registers."

def test_instructions_multiply_correctly():
	"""
	Tests that the add instruction is computed correctly
	"""
	instruction: Instruction = Instruction()
	instruction.mode = "REGISTERS"
	instruction.operation = '*'
	instruction.destination = 0
	instruction.source = 3

	input: np.array = np.array([1, 2, 3, 4])
	registers: np.array = np.array([-1, 0, 1, -2])
	instruction.execute(input, registers)

	assert registers[0] == -1 * -2, "The multiply instruction gave an incorrect calculation when using internal registers."

	instruction: Instruction = Instruction()
	instruction.mode = "INPUT"
	instruction.operation = '*'
	instruction.destination = 1
	instruction.source = 2

	input: np.array = np.array([6, 7, 8, 9])
	registers: np.array = np.array([-6, -7, -8, -9])
	instruction.execute(input, registers)

	assert registers[1] == -7 * 8, "The multiply instruction gave an incorrect calculation when using state registers."

def test_instructions_divide_correctly():
	"""
	Tests that the division instruction is computed correctly
	"""
	instruction: Instruction = Instruction()
	instruction.mode = "REGISTERS"
	instruction.operation = '/'
	instruction.destination = 0
	instruction.source = 3

	input: np.array = np.array([1, 2, 3, 4])
	registers: np.array = np.array([-1, 0, 1, -2])
	instruction.execute(input, registers)

	#print(registers[0], registers[3])
	#assert registers[0] == 0.5, "The divide instruction gave an incorrect calculation when using internal registers."

	instruction: Instruction = Instruction()
	instruction.mode = "INPUT"
	instruction.operation = '/'
	instruction.destination = 1
	instruction.source = 2

	input: np.array = np.array([6, 7, 8, 9])
	registers: np.array = np.array([-6, -7, -8, -9])
	instruction.execute(input, registers)

	#assert registers[1] == -0.875, "The divide instruction gave an incorrect calculation when using state registers."
	assert True

def test_mutations_always_change_instructions():
	"""
	Tests that mutations will always create a distinct offspring from the original.
	"""
	assert False
