from model import Model

import random
from typing import List
from environment import GymEnvironment
from debugger import Debugger
import sys
from instruction import Instruction
from program import Program
from parameters import Parameters

def main():

    environment: Environment = GymEnvironment()
    model: Model = Model()
    debugger: Debugger = Debugger()

    try:
        model.fit(environment, 200, 1000)
        #print(debugger.getInformation(model))
        #debugger.screenshot(model)
    except RuntimeError as e:
        raise e

if __name__ == "__main__":
    main()
