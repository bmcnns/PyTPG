from model import Model
import random
from typing import List
from environment import ALEEnvironment, GymEnvironment
from debugger import Debugger
import sys
from instruction import Instruction
from program import Program
from parameters import Parameters
from team import Team

import matplotlib.pyplot as plt

def main():
	model = Model()
	environment = GymEnvironment()
	
	model.fit(environment, 50, 500)

	model.save()

if __name__ == "__main__":
	main()
